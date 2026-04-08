#!/usr/bin/env python3
"""Build static HTML site from markdown chapters."""

import re
import os
import json

BASE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(BASE, 'docs')
BOOK_KO = os.path.join(BASE, 'book', 'ko')
BOOK_EN = os.path.join(BASE, 'book', 'en')

# Chapter metadata
CHAPTERS_KO = {
    1: {"title": "서론 — Agentic Coding에서 Agentic Robotics로", "part": "Part I: 기초 — LLM이 로봇을 만나다", "part_num": 1},
    2: {"title": "LLM as Planner — 제로샷 계획과 그라운딩", "part": "Part I: 기초 — LLM이 로봇을 만나다", "part_num": 1},
    3: {"title": "Code as Policies — 코드로 로봇을 제어하다", "part": "Part I: 기초 — LLM이 로봇을 만나다", "part_num": 1},
    4: {"title": "Vision-Language-Action 모델의 부상", "part": "Part II: VLA 혁명", "part_num": 2},
    5: {"title": "계층적 계획 — 고수준에서 저수준으로", "part": "Part II: VLA 혁명", "part_num": 2},
    6: {"title": "저수준 제어 — Diffusion Policy와 3D 표현", "part": "Part II: VLA 혁명", "part_num": 2},
    7: {"title": "메모리와 세계 표현", "part": "Part III: 에이전틱 로보틱스를 향하여", "part_num": 3},
    8: {"title": "폐루프 에이전틱 시스템", "part": "Part III: 에이전틱 로보틱스를 향하여", "part_num": 3},
    9: {"title": "Sim-to-Real 전이와 평가", "part": "Part III: 에이전틱 로보틱스를 향하여", "part_num": 3},
    10: {"title": "Agentic Coding vs Agentic Robotics — 간극과 미래", "part": "Part IV: 근본적 차이", "part_num": 4},
    11: {"title": "참고 — Agentic Coding 시스템의 구조", "part": "Appendix", "part_num": 2},
}

CHAPTERS_EN = {
    1: {"title": "Introduction — From Agentic Coding to Agentic Robotics", "part": "Part I: Foundations — LLM Meets Robotics", "part_num": 1},
    2: {"title": "LLM as Planner — Zero-Shot Planning and Grounding", "part": "Part I: Foundations — LLM Meets Robotics", "part_num": 1},
    3: {"title": "Code as Policies — Programming Robot Control", "part": "Part I: Foundations — LLM Meets Robotics", "part_num": 1},
    4: {"title": "The Rise of Vision-Language-Action Models", "part": "Part II: The VLA Revolution", "part_num": 2},
    5: {"title": "Hierarchical Planning — From High-Level to Low-Level", "part": "Part II: The VLA Revolution", "part_num": 2},
    6: {"title": "Low-Level Control — Diffusion Policy and 3D Representations", "part": "Part II: The VLA Revolution", "part_num": 2},
    7: {"title": "Memory and World Representation", "part": "Part III: Toward Agentic Robotics", "part_num": 3},
    8: {"title": "Closed-Loop Agentic Systems", "part": "Part III: Toward Agentic Robotics", "part_num": 3},
    9: {"title": "Sim-to-Real Transfer and Evaluation", "part": "Part III: Toward Agentic Robotics", "part_num": 3},
    10: {"title": "Agentic Coding vs Agentic Robotics — The Gap and the Future", "part": "Part IV: Fundamental Differences", "part_num": 4},
    11: {"title": "Appendix — Architecture of Agentic Coding Systems", "part": "Appendix", "part_num": 2},
}

NUM_CHAPTERS = 11


def parse_frontmatter(md):
    """Extract YAML frontmatter and body."""
    meta = {}
    body = md
    if md.startswith('---'):
        parts = md.split('---', 2)
        if len(parts) >= 3:
            fm = parts[1]
            body = parts[2]
            for line in fm.strip().split('\n'):
                if ':' in line and not line.strip().startswith('-'):
                    key, val = line.split(':', 1)
                    meta[key.strip().strip('"')] = val.strip().strip('"')
    return meta, body


def build_citation_map(md_text):
    """Build a mapping from Author-Year citations to sequential numbers."""
    ref_section = None
    for marker in ['## 참고문헌', '## References']:
        idx = md_text.find(marker)
        if idx != -1:
            ref_section = md_text[idx:]
            break

    if not ref_section:
        return {}, []

    refs = []
    for line in ref_section.split('\n'):
        line = line.strip()
        match = re.match(r'^\d+\.\s+(.+)', line)
        if match:
            ref_text = match.group(1)
            refs.append(ref_text)

    cite_map = {}
    for i, ref_text in enumerate(refs, 1):
        year_match = re.search(r'\((\d{4})\)', ref_text)
        if not year_match:
            continue
        year = year_match.group(1)

        author_part = ref_text[:ref_text.find(f'({year})')].strip().rstrip(',').strip()
        first_author = author_part.split(',')[0].strip()

        cite_map[f'{first_author}, {year}'] = i
        cite_map[f'{first_author} ({year})'] = i
        cite_map[f'{first_author} et al., {year}'] = i
        cite_map[f'{first_author} et al. ({year})'] = i

        authors_list = [a.strip() for a in author_part.split(',')]
        last_names = [a for a in authors_list if len(a) > 2 and not re.match(r'^[A-Z]\.\s*$', a.strip())]
        if len(last_names) == 2:
            cite_map[f'{last_names[0]} & {last_names[1]}, {year}'] = i
            cite_map[f'{last_names[0]} and {last_names[1]}, {year}'] = i

        first_author_clean = first_author.replace('**', '').strip()
        if first_author_clean != first_author:
            cite_map[f'{first_author_clean}, {year}'] = i
            cite_map[f'{first_author_clean} et al., {year}'] = i

        org_part = author_part.replace('**', '').strip().rstrip('.')
        if org_part:
            cite_map[f'{org_part}, {year}'] = i
            cite_map[f'{org_part} ({year})'] = i
            cite_map[f'{org_part} [{year}]'] = i

        for keyword in re.findall(
            r'(?:SayCan|SayPlan|PaLM-E|RT-1|RT-2|RT-H|RT-X|OpenVLA|pi0|pi0\.5|'
            r'GR00T|GR00T N1|Octo|TinyVLA|FAST|HAMSTER|Hi Robot|'
            r'AutoTAMP|AutoRT|BUMBLE|REFLECT|PragmaBot|CaP-X|'
            r'Code-as-Symbolic-Planner|Code as Policies|CaP|RL-GPT|'
            r'Diffusion Policy|3D Diffuser Actor|DROID|SIMPLER|'
            r'KARMA|Embodied-RAG|RoboEXP|VeriGraph|3D-Mem|MoMa-LLM|RoboMemory|'
            r'PaLM-E|Open X-Embodiment|X-Embodiment|'
            r'Natural Language as Policies|NLaP|'
            r'LLM as Planners|LLM as Zero-Shot Planners)',
            ref_text, re.IGNORECASE
        ):
            kw_lower = keyword.lower()
            cite_map[f'{keyword} [{year}]'] = i
            cite_map[f'{keyword}, {year}'] = i
            cite_map[f'{keyword} ({year})'] = i
            cite_map[f'_kw_{kw_lower}_{year}'] = i

    year_count = {}
    for ref_text in refs:
        ym = re.search(r'\((\d{4})\)', ref_text)
        if ym:
            yr = ym.group(1)
            year_count[yr] = year_count.get(yr, 0) + 1
    for i, ref_text in enumerate(refs, 1):
        ym = re.search(r'\((\d{4})\)', ref_text)
        if ym:
            yr = ym.group(1)
            if year_count[yr] == 1 and yr not in cite_map:
                cite_map[yr] = i

    return cite_map, refs


def replace_citations_with_links(html_text, cite_map, ch_num, ref_list=None):
    """Replace [Author, Year] citations in HTML with superscript links."""
    if not cite_map:
        return html_text
    if ref_list is None:
        ref_list = []

    year_refs = {}
    for key, num in cite_map.items():
        year_match = re.search(r'\d{4}', key)
        if year_match:
            yr = year_match.group()
            author = key.replace(yr, '').strip(' ,[]()').lower()
            if yr not in year_refs:
                year_refs[yr] = []
            year_refs[yr].append((author, num))

    def make_link(num, title):
        return f'<sup><a class="cite-link" href="#ch{ch_num}-ref-{num}" title="{title}">[{num}]</a></sup>'

    def citation_replacer(match):
        full_match = match.group(0)
        inner = match.group(1)

        end_pos = match.end()
        if end_pos < len(html_text) and html_text[end_pos] == '(':
            return full_match

        if not re.search(r'\d{4}', inner):
            return full_match

        inner_clean = inner.strip()

        if inner_clean in cite_map:
            return make_link(cite_map[inner_clean], inner_clean)

        inner_year = re.search(r'\d{4}', inner_clean)
        if inner_year:
            yr = inner_year.group()
            inner_lower = inner_clean.lower()

            for key, num in cite_map.items():
                key_year = re.search(r'\d{4}', key)
                if key_year and key_year.group() == yr:
                    key_author = key.replace(yr, '').strip(' ,[]()').lower()
                    if key_author and key_author in inner_lower:
                        return make_link(num, inner_clean)
                    if inner_lower.replace(yr, '').strip(' ,[]()') in key_author and len(inner_lower) > 4:
                        return make_link(num, inner_clean)

            if inner_clean == yr and yr in cite_map:
                return make_link(cite_map[yr], inner_clean)

        return full_match

    result = re.sub(r'\[([^\]]+)\](?!\()', citation_replacer, html_text)

    def contextual_replacer(match):
        prefix = match.group(1)
        year = match.group(2)

        if 'cite-link' in prefix:
            return match.group(0)

        prefix_clean = re.sub(r'<[^>]+>', '', prefix).strip()
        prefix_lower = prefix_clean.lower()

        kw_key = f'_kw_{prefix_lower}_{year}'
        if kw_key in cite_map:
            return f'{prefix}{make_link(cite_map[kw_key], prefix_clean + " " + year)}'

        for pattern in [f'{prefix_clean} [{year}]', f'{prefix_clean}, {year}', f'{prefix_clean} ({year})']:
            if pattern in cite_map:
                return f'{prefix}{make_link(cite_map[pattern], prefix_clean + " " + year)}'

        for key, num in cite_map.items():
            if key.startswith('_kw_'):
                continue
            key_year = re.search(r'\d{4}', key)
            if key_year and key_year.group() == year:
                key_lower = key.lower()
                if prefix_lower and len(prefix_lower) > 2 and prefix_lower in key_lower:
                    return f'{prefix}{make_link(num, prefix_clean + " " + year)}'

        if ref_list:
            for idx, ref_text in enumerate(ref_list, 1):
                ref_year = re.search(r'\((\d{4})\)', ref_text)
                if ref_year and ref_year.group(1) == year:
                    ref_lower = ref_text.lower()
                    if prefix_lower and len(prefix_lower) > 2:
                        if prefix_lower in ref_lower:
                            return f'{prefix}{make_link(idx, prefix_clean + " " + year)}'
                        prefix_base = re.sub(r'[\d.]+$', '', prefix_lower)
                        if prefix_base and len(prefix_base) > 1 and prefix_base in ref_lower:
                            return f'{prefix}{make_link(idx, prefix_clean + " " + year)}'

        if year in cite_map:
            return f'{prefix}{make_link(cite_map[year], year)}'

        return match.group(0)

    result = re.sub(r'(\S+)\s*\[(\d{4})\](?!\()', contextual_replacer, result)

    return result


def build_references_list_html(refs, ch_num):
    """Build the chapter-level reference list as a proper numbered list with anchors."""
    if not refs:
        return ''

    items = []
    for i, ref_text in enumerate(refs, 1):
        ref_html = ref_text
        ref_html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', ref_html)
        ref_html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', ref_html)
        items.append(f'  <li id="ch{ch_num}-ref-{i}" value="{i}">{ref_html}</li>')

    return '<ol class="references-list">\n' + '\n'.join(items) + '\n</ol>'


def md_to_html_content(md_text, ch_num, lang):
    """Convert markdown body to HTML sections."""
    lines = md_text.strip().split('\n')
    html_parts = []
    in_table = False
    in_code = False
    in_list = False
    in_blockquote = False
    list_type = None
    current_section_id = None
    bq_lines = []

    def flush_blockquote():
        nonlocal bq_lines, in_blockquote
        if bq_lines:
            content = '\n'.join(bq_lines)
            css_class = 'key-paper' if any(k in content for k in ['핵심 논문', 'Key Paper', '핵심 연구']) else ''
            html_parts.append(f'<blockquote class="{css_class}">{process_inline(content)}</blockquote>')
            bq_lines = []
            in_blockquote = False

    def flush_list():
        nonlocal in_list, list_type
        if in_list:
            tag = 'ol' if list_type == 'ol' else 'ul'
            html_parts.append(f'</{tag}>')
            in_list = False
            list_type = None

    def process_inline(text):
        # Protect inline math $...$ from bold/italic/code transforms
        # Skip currency like $60,000 — math starts with \ or a letter, not a digit
        math_placeholders = []
        def save_math(m):
            inner = m.group(1)
            # If inner starts with a digit, it's likely currency ($600), not math
            if inner and inner[0].isdigit():
                return m.group(0)  # Leave as-is, not math
            math_placeholders.append(m.group(0))
            return f'\x00MATH{len(math_placeholders)-1}\x00'
        text = re.sub(r'\$([^\$]+?)\$', save_math, text)

        text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
        text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)

        def inline_img(m):
            alt = m.group(1)
            src = m.group(2)
            src = src.replace('../../assets/figures/', '../assets/figures/')
            return f'<a href="{src}" target="_blank"><img src="{src}" alt="{alt}" loading="lazy" style="max-height:160px;width:auto;border-radius:8px;cursor:zoom-in"></a>'
        text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', inline_img, text)

        # Post links [#N](URL) → open in new tab
        text = re.sub(r'\[(#\d+)\]\(([^)]+)\)', r'<a href="\2" target="_blank" class="post-link">[\1]</a>', text)
        # Regular markdown links
        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)

        def chapter_ref(m):
            ref_text = m.group(1)
            ch_match = re.search(r'Chapter\s+(\d+)', ref_text)
            if ch_match:
                ch = ch_match.group(1).zfill(2)
                return f'(<a href="ch{ch}.html">{ref_text}</a>)'
            return m.group(0)
        text = re.sub(r'\(→\s*([^)]+)\)', chapter_ref, text)

        # Restore inline math as KaTeX-compatible spans
        def restore_math(m):
            idx = int(m.group(1))
            original = math_placeholders[idx]
            # Strip outer $ delimiters
            inner = original[1:-1]
            return f'<span class="math-inline">{inner}</span>'
        text = re.sub(r'\x00MATH(\d+)\x00', restore_math, text)
        return text

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Block math $$...$$
        if stripped.startswith('$$') and stripped.endswith('$$') and len(stripped) > 4:
            flush_blockquote()
            flush_list()
            inner = stripped[2:-2]
            html_parts.append(f'<div class="math-block">{inner}</div>')
            continue

        # Code blocks
        if stripped.startswith('```'):
            if in_code:
                html_parts.append('</code></pre>')
                in_code = False
            else:
                flush_blockquote()
                flush_list()
                lang_match = re.match(r'```(\w+)', stripped)
                code_lang = lang_match.group(1) if lang_match else ''
                html_parts.append(f'<pre><code class="language-{code_lang}">')
                in_code = True
            continue

        if in_code:
            html_parts.append(line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))
            continue

        if stripped.startswith('---') and not in_table:
            flush_blockquote()
            flush_list()
            html_parts.append('<hr>')
            continue

        # Blockquotes
        if stripped.startswith('>'):
            flush_list()
            if in_table:
                html_parts.append('</tbody></table>')
                in_table = False
            content = stripped.lstrip('>').strip()
            if not in_blockquote:
                in_blockquote = True
                bq_lines = [content]
            else:
                bq_lines.append(content)
            continue
        elif in_blockquote:
            flush_blockquote()

        # Empty lines
        if not stripped:
            flush_list()
            if in_table:
                html_parts.append('</tbody></table>')
                in_table = False
            continue

        # H1
        if stripped.startswith('# ') and not stripped.startswith('## '):
            continue

        # H2
        if stripped.startswith('## '):
            flush_list()
            if in_table:
                html_parts.append('</tbody></table>')
                in_table = False
            title = stripped[3:].strip()
            sec_match = re.match(r'(\d+\.\d+)', title)
            if sec_match:
                sec_id = f'sec-{sec_match.group(1).replace(".", "-")}'
            else:
                sec_id = f'sec-{title.lower().replace(" ", "-")[:30]}'

            if current_section_id is not None:
                html_parts.append('</section>')

            current_section_id = sec_id
            html_parts.append(f'<section id="{sec_id}" class="content-section">')
            html_parts.append(f'<h2>{process_inline(title)}</h2>')
            continue

        # H3
        if stripped.startswith('### '):
            flush_list()
            if in_table:
                html_parts.append('</tbody></table>')
                in_table = False
            title = stripped[4:].strip()
            html_parts.append(f'<h3>{process_inline(title)}</h3>')
            continue

        # H4
        if stripped.startswith('#### '):
            flush_list()
            if in_table:
                html_parts.append('</tbody></table>')
                in_table = False
            title = stripped[5:].strip()
            html_parts.append(f'<h4>{process_inline(title)}</h4>')
            continue

        # Images
        img_match = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', stripped)
        if img_match:
            flush_list()
            caption = img_match.group(1)
            src = img_match.group(2)
            src = src.replace('../../assets/figures/', '../assets/figures/')
            src_dark = src.replace('_technical.png', '_darkmode.png')
            html_parts.append(f'<figure>')
            html_parts.append(f'  <a href="{src}" target="_blank"><img src="{src_dark}" alt="{caption}" loading="lazy" onerror="this.src=\'{src}\'" style="cursor:zoom-in"></a>')
            html_parts.append(f'  <figcaption>{process_inline(caption)}</figcaption>')
            html_parts.append(f'</figure>')
            continue

        # Tables
        if '|' in stripped and stripped.startswith('|'):
            if not in_table:
                flush_list()
                in_table = True
                html_parts.append('<table class="styled-table">')
                cells = [c.strip() for c in stripped.split('|')[1:-1]]
                html_parts.append('<thead><tr>')
                for c in cells:
                    html_parts.append(f'<th>{process_inline(c)}</th>')
                html_parts.append('</tr></thead><tbody>')
            elif re.match(r'\|[\s\-:|]+\|', stripped):
                continue
            else:
                cells = [c.strip() for c in stripped.split('|')[1:-1]]
                html_parts.append('<tr>')
                for c in cells:
                    html_parts.append(f'<td>{process_inline(c)}</td>')
                html_parts.append('</tr>')
            continue
        elif in_table:
            html_parts.append('</tbody></table>')
            in_table = False

        # Unordered list
        if re.match(r'^[-*]\s', stripped):
            content = re.sub(r'^[-*]\s+', '', stripped)
            if not in_list or list_type != 'ul':
                flush_list()
                html_parts.append('<ul>')
                in_list = True
                list_type = 'ul'
            html_parts.append(f'<li>{process_inline(content)}</li>')
            continue

        # Ordered list
        ol_match = re.match(r'^(\d+)\.\s+(.+)', stripped)
        if ol_match:
            content = ol_match.group(2)
            if not in_list or list_type != 'ol':
                flush_list()
                html_parts.append('<ol>')
                in_list = True
                list_type = 'ol'
            html_parts.append(f'<li>{process_inline(content)}</li>')
            continue

        # Regular paragraph
        flush_list()
        html_parts.append(f'<p>{process_inline(stripped)}</p>')

    # Close open elements
    flush_blockquote()
    flush_list()
    if in_table:
        html_parts.append('</tbody></table>')
    if in_code:
        html_parts.append('</code></pre>')
    if current_section_id is not None:
        html_parts.append('</section>')

    return '\n'.join(html_parts)


def extract_sections(md_text, ch_num):
    """Extract section titles for sidebar navigation."""
    sections = []
    for line in md_text.split('\n'):
        line = line.strip()
        if line.startswith('## ') and not line.startswith('### '):
            title = line[3:].strip()
            sec_match = re.match(r'(\d+\.\d+)', title)
            if sec_match:
                sec_id = f'sec-{sec_match.group(1).replace(".", "-")}'
            else:
                sec_id = f'sec-{title.lower().replace(" ", "-")[:30]}'
            sections.append({"id": sec_id, "title": title})
    return sections


def build_sidebar(sections, part_num):
    """Build sidebar navigation HTML."""
    if not sections:
        return ''
    dots = []
    for i, sec in enumerate(sections):
        active = ' active' if i == 0 else ''
        label = sec['title']
        if len(label) > 35:
            label = label[:35] + '...'
        dots.append(f'    <a class="nav-dot{active}" data-section="{sec["id"]}">\n'
                     f'      <span class="dot"></span>\n'
                     f'      <span class="label">{label}</span>\n'
                     f'    </a>')
    return f'  <nav class="sidebar-nav part-{part_num}">\n' + '\n'.join(dots) + '\n  </nav>'


def build_chapter_html(ch_num, lang, chapters_meta, book_dir, lang_code):
    """Build a complete chapter HTML page."""
    md_path = os.path.join(book_dir, f'ch{ch_num:02d}.md')
    if not os.path.exists(md_path):
        print(f"  WARNING: {md_path} not found, skipping")
        return None

    with open(md_path, 'r', encoding='utf-8') as f:
        md = f.read()

    meta, body = parse_frontmatter(md)
    ch_meta = chapters_meta[ch_num]
    part_num = ch_meta['part_num']
    part_label = ch_meta['part']
    title = ch_meta['title']

    date = meta.get('date', '2026-04-08')
    last_updated = meta.get('last_updated', '2026-04-08')

    if lang_code == 'ko':
        date_label = '집필일'
        updated_label = '최종수정일'
        toc_label = '목록'
    else:
        date_label = 'Written'
        updated_label = 'Last updated'
        toc_label = 'Index'

    if ch_num > 1:
        prev_link = f'<a href="ch{ch_num-1:02d}.html" class="prev">&larr; Ch.{ch_num-1}</a>'
    else:
        prev_link = '<span class="placeholder"></span>'

    toc_link = f'<a href="./" class="toc-link">{toc_label}</a>'

    if ch_num < NUM_CHAPTERS:
        next_link = f'<a href="ch{ch_num+1:02d}.html" class="next">Ch.{ch_num+1} &rarr;</a>'
    else:
        next_link = '<span class="placeholder"></span>'

    chapter_nav_html = f'''      <nav class="chapter-nav">
        {prev_link}
        {toc_link}
        {next_link}
      </nav>'''

    cite_map, ref_list = build_citation_map(body)

    ref_marker = None
    body_content = body
    for marker in ['## 참고문헌', '## References']:
        idx = body.find(marker)
        if idx != -1:
            ref_marker = marker
            body_content = body[:idx]
            break

    content_html = md_to_html_content(body_content, ch_num, lang)
    content_html = replace_citations_with_links(content_html, cite_map, ch_num, ref_list)

    ref_section_title = '참고문헌' if lang == 'ko' else 'References'
    ref_html = ''
    if ref_list:
        ref_html = f'<section id="sec-references" class="content-section">\n'
        ref_html += f'<h2>{ref_section_title}</h2>\n'
        ref_html += build_references_list_html(ref_list, ch_num)
        ref_html += '\n</section>'

    content_html = content_html + '\n' + chapter_nav_html + '\n' + ref_html

    sections = extract_sections(body, ch_num)
    sidebar_html = build_sidebar(sections, part_num)

    html = f'''<!DOCTYPE html>
<html lang="{lang_code}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chapter {ch_num}: {title}</title>
  <link rel="stylesheet" href="../css/style.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
</head>
<body{' class="lang-en"' if lang_code == 'en' else ''}>
  <canvas id="particle-canvas"></canvas>

  <header id="site-header"></header>
  <script src="../js/header.js"></script>

  <main class="chapter-page part-{part_num}">
{sidebar_html}

    <article class="chapter-content">
      <header class="chapter-header">
        <span class="part-label">{part_label}</span>
        <h1>Chapter {ch_num}: {title}</h1>
        <div class="chapter-meta">
          <span>{date_label}: {date}</span>
          <span>{updated_label}: {last_updated}</span>
        </div>
      </header>

{content_html}

{chapter_nav_html}
    </article>
  </main>

  <footer id="site-footer"></footer>
  <script src="../js/footer.js"></script>

  <script src="../js/main.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
  <script src="../js/chapter.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", function() {{
      if (typeof katex !== 'undefined') {{
        // Render .math-inline and .math-block elements
        document.querySelectorAll('.math-inline').forEach(function(el) {{
          katex.render(el.textContent, el, {{ throwOnError: false, displayMode: false }});
        }});
        document.querySelectorAll('.math-block').forEach(function(el) {{
          katex.render(el.textContent, el, {{ throwOnError: false, displayMode: true }});
        }});
      }}
    }});
  </script>
</body>
</html>'''

    return html


def parse_bib(bib_path):
    """Parse BibTeX file into list of references."""
    refs = []
    with open(bib_path, 'r', encoding='utf-8') as f:
        content = f.read()

    entries = re.findall(r'@\w+\{([^,]+),([^@]+)', content)
    for key, body in entries:
        ref = {'key': key.strip()}
        for field in ['title', 'author', 'year', 'journal', 'booktitle', 'url']:
            match = re.search(rf'{field}\s*=\s*\{{(.+?)\}}', body)
            if match:
                ref[field] = match.group(1).strip()
        if 'title' in ref:
            refs.append(ref)

    return refs


def build_references_html(lang_code, bib_path):
    """Build references page."""
    refs = parse_bib(bib_path)

    if lang_code == 'ko':
        page_title = '통합 참고문헌 (References)'
    else:
        page_title = 'Consolidated References'

    ref_items = []
    for i, ref in enumerate(refs, 1):
        authors = ref.get('author', 'Unknown')
        year = ref.get('year', '')
        title = ref.get('title', '')
        venue = ref.get('journal', ref.get('booktitle', ''))
        url = ref.get('url', '')

        url_html = f' <a href="{url}" target="_blank" rel="noopener">[Link]</a>' if url else ''

        ref_items.append(
            f'<div class="ref-item" id="ref-{ref["key"]}">'
            f'<span class="ref-id">[{i}]</span> '
            f'{authors} ({year}). <strong>{title}</strong>. <em>{venue}</em>.{url_html}'
            f'</div>'
        )

    content = '\n'.join(ref_items)

    html = f'''<!DOCTYPE html>
<html lang="{lang_code}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_title}</title>
  <link rel="stylesheet" href="../css/style.css">
</head>
<body{' class="lang-en"' if lang_code == 'en' else ''}>
  <canvas id="particle-canvas"></canvas>

  <header id="site-header"></header>
  <script src="../js/header.js"></script>

  <main>
    <div class="references-section">
      <header class="chapter-header">
        <h1>{page_title}</h1>
        <p class="chapter-summary">{len(refs)} references</p>
      </header>
{content}

      <section class="acknowledgment-section">
        <h2>{'감사의 글' if lang_code == 'ko' else 'Acknowledgment'}</h2>
        <p>{'이 책은 LLM 기반 로봇 계획에서 에이전틱 로보틱스까지의 연구 흐름을 추적하는 서베이입니다. Agentic Coding과 Agentic Robotics의 근본적 차이를 분석하여 Physical AI의 미래 방향을 제시합니다.' if lang_code == 'ko' else 'This book traces the research evolution from LLM-based robot planning to agentic robotics. It analyzes fundamental differences between agentic coding and agentic robotics to chart the future of Physical AI.'}</p>
        <p>{'이 서베이는 고려대학교 최성준 교수님(Prof. Sungjoon Choi)과 김찬우 박사과정(Chanwoo Kim)에게 감사드립니다. 김찬우님의 세미나 발표에서 영감을 받았으며, 그의 세미나 레퍼런스 논문들을 기초로 제작되었습니다.' if lang_code == 'ko' else 'Special thanks to Prof. Sungjoon Choi and Chanwoo Kim (PhD candidate) at Korea University. This survey was inspired by Chanwoo Kim&apos;s seminar presentation, and the reference papers from his seminar formed the foundation of this work.'}</p>
        <p>{'이 프로젝트는 황민호님의 <a href="https://github.com/revfactory/harness">Harness</a> 스킬을 이용하여 제작되었습니다.' if lang_code == 'ko' else 'This project was built using the <a href="https://github.com/revfactory/harness">Harness</a> skill by Minho Hwang.'}</p>
        <p>{'이 저작물의 제작에 AI 도구가 활용되었습니다. 문헌 조사, 콘텐츠 생성, 원고 작성에 Claude(Opus 4.6)를 사용하였습니다.' if lang_code == 'ko' else 'AI tools were used in the production of this work: Claude (Opus 4.6) for literature survey, content generation, and manuscript preparation.'}</p>
      </section>
    </div>
  </main>

  <footer id="site-footer"></footer>
  <script src="../js/footer.js"></script>

  <script src="../js/main.js"></script>
</body>
</html>'''

    return html


def build_index_html():
    """Build root index.html with language auto-detection."""
    return '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Toward Agentic Robotics</title>
  <link rel="stylesheet" href="css/style.css">
  <script>
    (function() {
      var lang = localStorage.getItem('preferred-lang');
      if (lang === 'en') { window.location.replace('en/'); return; }
      if (lang === 'ko') { window.location.replace('ko/'); return; }
      var browserLang = (navigator.language || navigator.userLanguage || '').toLowerCase();
      if (browserLang.startsWith('ko')) {
        localStorage.setItem('preferred-lang', 'ko');
        window.location.replace('ko/');
      } else {
        localStorage.setItem('preferred-lang', 'en');
        window.location.replace('en/');
      }
    })();
  </script>
</head>
<body>
  <canvas id="particle-canvas"></canvas>

  <main class="lang-landing">
    <h1 class="gradient-text">Toward Agentic Robotics</h1>
    <p style="color: var(--text-secondary); font-size: 1.1rem; max-width: 600px; text-align: center; line-height: 1.8;">
      The Future of Physical AI &mdash; Tracing the evolution from LLM-based planning through VLA to agentic robotics
    </p>

    <div class="lang-options">
      <a href="ko/" class="lang-option">
        <span class="lang-flag">&#x1F1F0;&#x1F1F7;</span>
        <span class="lang-name">&#xD55C;&#xAD6D;&#xC5B4;</span>
        <span class="lang-sub">Korean</span>
      </a>
      <a href="en/" class="lang-option">
        <span class="lang-flag">&#x1F1FA;&#x1F1F8;</span>
        <span class="lang-name">English</span>
        <span class="lang-sub">English</span>
      </a>
    </div>
  </main>

  <script src="js/main.js"></script>
</body>
</html>
'''


def build_toc_ko():
    """Build Korean table of contents page."""
    return '''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Toward Agentic Robotics</title>
  <link rel="stylesheet" href="../css/style.css">
</head>
<body>
  <canvas id="particle-canvas"></canvas>

  <header id="site-header"></header>
  <script src="../js/header.js"></script>

  <main>
    <section class="hero">
      <h1 class="gradient-text">Toward Agentic Robotics</h1>
      <p class="subtitle">Physical AI의 미래 &mdash; LLM 기반 계획에서 VLA, Code as Policy를 거쳐 에이전틱 로보틱스로</p>
      <p class="description">
        Agentic Coding의 code&rarr;tool&rarr;execution&rarr;error&rarr;LLM 루프가 물리 세계에서 작동하려면 무엇이 달라져야 하는가? &mdash; 4 Parts, 10 Chapters
      </p>
      <p class="hero-dates" style="color: var(--text-muted); font-size: 0.9rem; margin-top: 0.5rem;">
        <span>First published: 2026-04-08</span>
        <span style="margin: 0 0.5rem;">|</span>
        <span>Last updated: 2026-04-08</span>
      </p>
      <div class="hero-cta">
        <a href="ch01.html" class="btn-primary">읽기 시작</a>
      </div>
    </section>

    <section class="intro-section">
      <div class="intro-list">
        <div class="intro-item">
          <span class="item-icon">&#x1F916;</span>
          <div class="intro-item-content">
            <h4>Agentic Coding vs Agentic Robotics</h4>
            <p>디지털 에이전트의 성공 패턴을 거울 삼아, 물리 세계에서의 에이전틱 시스템이 넘어야 할 근본적 차이를 분석합니다.</p>
          </div>
        </div>
        <div class="intro-item">
          <span class="item-icon">&#x1F4DA;</span>
          <div class="intro-item-content">
            <h4>연구 흐름 추적</h4>
            <p>LLM as Planner(2022)부터 VLA, Code as Policy를 거쳐 최신 Agentic Robotics까지의 패러다임 전환을 시간순으로 짚습니다.</p>
          </div>
        </div>
        <div class="intro-item">
          <span class="item-icon">&#x1F52C;</span>
          <div class="intro-item-content">
            <h4>핵심 논문 50+편 분석</h4>
            <p>SayCan, RT-2, OpenVLA, pi0, KARMA, BUMBLE 등 주요 논문의 기여, 실험 수치, 한계를 비판적으로 분석합니다.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="chapters-section">

      <div class="part-group part-1">
        <h2 class="part-title">Part I: 기초 &mdash; LLM이 로봇을 만나다</h2>
        <div class="chapter-grid">
          <a href="ch01.html" class="chapter-card fade-in">
            <span class="ch-num">01</span>
            <h3>서론 &mdash; Agentic Coding에서 Agentic Robotics로</h3>
            <p>핵심 비유, 7대 차원 비교, 이 책의 질문과 구조</p>
            <span class="arrow">&rarr;</span>
          </a>
          <a href="ch02.html" class="chapter-card fade-in">
            <span class="ch-num">02</span>
            <h3>LLM as Planner &mdash; 제로샷 계획과 그라운딩</h3>
            <p>LLM as Planners, SayCan, SayPlan, affordance grounding</p>
            <span class="arrow">&rarr;</span>
          </a>
          <a href="ch03.html" class="chapter-card fade-in">
            <span class="ch-num">03</span>
            <h3>Code as Policies &mdash; 코드로 로봇을 제어하다</h3>
            <p>CaP, Code-as-Symbolic-Planner, CaP-X, code generation</p>
            <span class="arrow">&rarr;</span>
          </a>
        </div>
      </div>

      <div class="part-group part-2">
        <h2 class="part-title">Part II: VLA 혁명</h2>
        <div class="chapter-grid">
          <a href="ch04.html" class="chapter-card fade-in">
            <span class="ch-num">04</span>
            <h3>Vision-Language-Action 모델의 부상</h3>
            <p>PaLM-E, RT-2, OpenVLA, pi0, GR00T N1, generalist policy</p>
            <span class="arrow">&rarr;</span>
          </a>
          <a href="ch05.html" class="chapter-card fade-in">
            <span class="ch-num">05</span>
            <h3>계층적 계획 &mdash; 고수준에서 저수준으로</h3>
            <p>AutoTAMP, RT-H, Hi Robot, HAMSTER, hierarchical VLA</p>
            <span class="arrow">&rarr;</span>
          </a>
          <a href="ch06.html" class="chapter-card fade-in">
            <span class="ch-num">06</span>
            <h3>저수준 제어 &mdash; Diffusion Policy와 3D 표현</h3>
            <p>Diffusion Policy, 3D Diffuser Actor, DROID, action tokenization</p>
            <span class="arrow">&rarr;</span>
          </a>
        </div>
      </div>

      <div class="part-group part-3">
        <h2 class="part-title">Part III: 에이전틱 로보틱스를 향하여</h2>
        <div class="chapter-grid">
          <a href="ch07.html" class="chapter-card fade-in">
            <span class="ch-num">07</span>
            <h3>메모리와 세계 표현</h3>
            <p>KARMA, Embodied-RAG, scene graph, spatial memory</p>
            <span class="arrow">&rarr;</span>
          </a>
          <a href="ch08.html" class="chapter-card fade-in">
            <span class="ch-num">08</span>
            <h3>폐루프 에이전틱 시스템</h3>
            <p>REFLECT, BUMBLE, AutoRT, PragmaBot, error recovery</p>
            <span class="arrow">&rarr;</span>
          </a>
          <a href="ch09.html" class="chapter-card fade-in">
            <span class="ch-num">09</span>
            <h3>Sim-to-Real 전이와 평가</h3>
            <p>SIMPLER, language-based sim2real, evaluation benchmarks</p>
            <span class="arrow">&rarr;</span>
          </a>
        </div>
      </div>

      <div class="part-group part-4">
        <h2 class="part-title">Part IV: 근본적 차이 &mdash; 디지털 에이전트 vs 물리 에이전트</h2>
        <div class="chapter-grid">
          <a href="ch10.html" class="chapter-card fade-in">
            <span class="ch-num">10</span>
            <h3>Agentic Coding vs Agentic Robotics &mdash; 간극과 미래</h3>
            <p>7대 차원 종합 분석, 근본적 차이, 미래 연구 방향</p>
            <span class="arrow">&rarr;</span>
          </a>
        </div>
      </div>

      <div class="part-group part-2">
        <h2 class="part-title">부록 (Appendices)</h2>
        <div class="chapter-grid">
          <a href="ch11.html" class="chapter-card fade-in">
            <span class="ch-num">11</span>
            <h3>참고 &mdash; Agentic Coding 시스템의 구조</h3>
            <p>Claude Code, Codex의 메모리/피드백/하네스 구조와 성공 비결</p>
            <span class="arrow">&rarr;</span>
          </a>
          <a href="references.html" class="chapter-card fade-in">
            <span class="ch-num">A</span>
            <h3>통합 참고문헌 (References)</h3>
            <p>전체 참고문헌 목록</p>
            <span class="arrow">&rarr;</span>
          </a>
        </div>
      </div>

    </section>
  </main>

  <footer id="site-footer"></footer>
  <script src="../js/footer.js"></script>

  <script src="../js/main.js"></script>
</body>
</html>
'''


def build_toc_en():
    """Build English table of contents page."""
    return '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Toward Agentic Robotics</title>
  <link rel="stylesheet" href="../css/style.css">
</head>
<body class="lang-en">
  <canvas id="particle-canvas"></canvas>

  <header id="site-header"></header>
  <script src="../js/header.js"></script>

  <main>
    <section class="hero">
      <h1 class="gradient-text">Toward Agentic Robotics</h1>
      <p class="subtitle">The Future of Physical AI &mdash; Tracing the evolution from LLM-based planning through VLA to agentic robotics</p>
      <p class="description">
        What must change for the agentic coding loop (code&rarr;tool&rarr;execution&rarr;error&rarr;LLM) to work in the physical world? &mdash; 4 Parts, 10 Chapters
      </p>
      <p class="hero-dates" style="color: var(--text-muted); font-size: 0.9rem; margin-top: 0.5rem;">
        <span>First published: 2026-04-08</span>
        <span style="margin: 0 0.5rem;">|</span>
        <span>Last updated: 2026-04-08</span>
      </p>
      <div class="hero-cta">
        <a href="ch01.html" class="btn-primary">Start Reading</a>
      </div>
    </section>

    <section class="intro-section">
      <div class="intro-list">
        <div class="intro-item">
          <span class="item-icon">&#x1F916;</span>
          <div class="intro-item-content">
            <h4>Agentic Coding vs Agentic Robotics</h4>
            <p>Using the success patterns of digital agents as a mirror, we analyze the fundamental differences that must be overcome in the physical world.</p>
          </div>
        </div>
        <div class="intro-item">
          <span class="item-icon">&#x1F4DA;</span>
          <div class="intro-item-content">
            <h4>Research Flow Tracking</h4>
            <p>Tracing paradigm shifts from LLM as Planner (2022) through VLA, Code as Policy, to the latest Agentic Robotics systems.</p>
          </div>
        </div>
        <div class="intro-item">
          <span class="item-icon">&#x1F52C;</span>
          <div class="intro-item-content">
            <h4>50+ Key Papers Analyzed</h4>
            <p>Critical analysis of contributions, experimental results, and limitations of SayCan, RT-2, OpenVLA, pi0, KARMA, BUMBLE, and more.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="chapters-section">

      <div class="part-group part-1">
        <h2 class="part-title">Part I: Foundations &mdash; LLM Meets Robotics</h2>
        <div class="chapter-grid">
          <a href="ch01.html" class="chapter-card fade-in">
            <span class="ch-num">01</span>
            <h3>Introduction &mdash; From Agentic Coding to Agentic Robotics</h3>
            <p>Core analogy, 7-dimension comparison, key questions and structure</p>
            <span class="arrow">&rarr;</span>
          </a>
          <a href="ch02.html" class="chapter-card fade-in">
            <span class="ch-num">02</span>
            <h3>LLM as Planner &mdash; Zero-Shot Planning and Grounding</h3>
            <p>LLM as Planners, SayCan, SayPlan, affordance grounding</p>
            <span class="arrow">&rarr;</span>
          </a>
          <a href="ch03.html" class="chapter-card fade-in">
            <span class="ch-num">03</span>
            <h3>Code as Policies &mdash; Programming Robot Control</h3>
            <p>CaP, Code-as-Symbolic-Planner, CaP-X, code generation</p>
            <span class="arrow">&rarr;</span>
          </a>
        </div>
      </div>

      <div class="part-group part-2">
        <h2 class="part-title">Part II: The VLA Revolution</h2>
        <div class="chapter-grid">
          <a href="ch04.html" class="chapter-card fade-in">
            <span class="ch-num">04</span>
            <h3>The Rise of Vision-Language-Action Models</h3>
            <p>PaLM-E, RT-2, OpenVLA, pi0, GR00T N1, generalist policy</p>
            <span class="arrow">&rarr;</span>
          </a>
          <a href="ch05.html" class="chapter-card fade-in">
            <span class="ch-num">05</span>
            <h3>Hierarchical Planning &mdash; From High-Level to Low-Level</h3>
            <p>AutoTAMP, RT-H, Hi Robot, HAMSTER, hierarchical VLA</p>
            <span class="arrow">&rarr;</span>
          </a>
          <a href="ch06.html" class="chapter-card fade-in">
            <span class="ch-num">06</span>
            <h3>Low-Level Control &mdash; Diffusion Policy and 3D Representations</h3>
            <p>Diffusion Policy, 3D Diffuser Actor, DROID, action tokenization</p>
            <span class="arrow">&rarr;</span>
          </a>
        </div>
      </div>

      <div class="part-group part-3">
        <h2 class="part-title">Part III: Toward Agentic Robotics</h2>
        <div class="chapter-grid">
          <a href="ch07.html" class="chapter-card fade-in">
            <span class="ch-num">07</span>
            <h3>Memory and World Representation</h3>
            <p>KARMA, Embodied-RAG, scene graph, spatial memory</p>
            <span class="arrow">&rarr;</span>
          </a>
          <a href="ch08.html" class="chapter-card fade-in">
            <span class="ch-num">08</span>
            <h3>Closed-Loop Agentic Systems</h3>
            <p>REFLECT, BUMBLE, AutoRT, PragmaBot, error recovery</p>
            <span class="arrow">&rarr;</span>
          </a>
          <a href="ch09.html" class="chapter-card fade-in">
            <span class="ch-num">09</span>
            <h3>Sim-to-Real Transfer and Evaluation</h3>
            <p>SIMPLER, language-based sim2real, evaluation benchmarks</p>
            <span class="arrow">&rarr;</span>
          </a>
        </div>
      </div>

      <div class="part-group part-4">
        <h2 class="part-title">Part IV: Fundamental Differences &mdash; Digital vs Physical Agents</h2>
        <div class="chapter-grid">
          <a href="ch10.html" class="chapter-card fade-in">
            <span class="ch-num">10</span>
            <h3>Agentic Coding vs Agentic Robotics &mdash; The Gap and the Future</h3>
            <p>7-dimension synthesis, fundamental differences, future research directions</p>
            <span class="arrow">&rarr;</span>
          </a>
        </div>
      </div>

      <div class="part-group part-2">
        <h2 class="part-title">Appendices</h2>
        <div class="chapter-grid">
          <a href="ch11.html" class="chapter-card fade-in">
            <span class="ch-num">11</span>
            <h3>Appendix &mdash; Architecture of Agentic Coding Systems</h3>
            <p>Claude Code, Codex memory/feedback/harness architecture and success factors</p>
            <span class="arrow">&rarr;</span>
          </a>
          <a href="references.html" class="chapter-card fade-in">
            <span class="ch-num">A</span>
            <h3>Consolidated References</h3>
            <p>Full bibliography</p>
            <span class="arrow">&rarr;</span>
          </a>
        </div>
      </div>

    </section>
  </main>

  <footer id="site-footer"></footer>
  <script src="../js/footer.js"></script>

  <script src="../js/main.js"></script>
</body>
</html>
'''


def main():
    bib_path = os.path.join(BASE, 'book', 'references.bib')

    # Ensure output directories exist
    for d in ['ko', 'en', 'css', 'js', os.path.join('assets', 'figures')]:
        os.makedirs(os.path.join(DOCS, d), exist_ok=True)

    # Build KO chapters
    print("Building Korean chapters...")
    for ch in range(1, NUM_CHAPTERS + 1):
        html = build_chapter_html(ch, 'ko', CHAPTERS_KO, BOOK_KO, 'ko')
        if html:
            out_path = os.path.join(DOCS, 'ko', f'ch{ch:02d}.html')
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"  Created: ko/ch{ch:02d}.html")

    # Build EN chapters
    print("Building English chapters...")
    for ch in range(1, NUM_CHAPTERS + 1):
        html = build_chapter_html(ch, 'en', CHAPTERS_EN, BOOK_EN, 'en')
        if html:
            out_path = os.path.join(DOCS, 'en', f'ch{ch:02d}.html')
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"  Created: en/ch{ch:02d}.html")

    # Build References
    print("Building references...")
    if os.path.exists(bib_path):
        for lang_code in ['ko', 'en']:
            html = build_references_html(lang_code, bib_path)
            out_path = os.path.join(DOCS, lang_code, 'references.html')
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"  Created: {lang_code}/references.html")
    else:
        print("  WARNING: references.bib not found, skipping references page")

    # Build index pages
    print("Building index pages...")
    with open(os.path.join(DOCS, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(build_index_html())
    print("  Created: index.html")

    with open(os.path.join(DOCS, 'ko', 'index.html'), 'w', encoding='utf-8') as f:
        f.write(build_toc_ko())
    print("  Created: ko/index.html")

    with open(os.path.join(DOCS, 'en', 'index.html'), 'w', encoding='utf-8') as f:
        f.write(build_toc_en())
    print("  Created: en/index.html")

    # Copy figures
    print("Copying figures...")
    import shutil
    src_figures = os.path.join(BASE, 'assets', 'figures')
    dst_figures = os.path.join(DOCS, 'assets', 'figures')
    if os.path.exists(src_figures):
        if os.path.exists(dst_figures):
            shutil.rmtree(dst_figures)
        shutil.copytree(src_figures, dst_figures)
        print(f"  Copied figures to docs/assets/figures/")

    print("\nBuild complete!")
    # Count files
    total = 0
    for root, dirs, files in os.walk(DOCS):
        total += len([f for f in files if f.endswith('.html')])
    print(f"Total HTML files: {total}")


if __name__ == '__main__':
    main()
