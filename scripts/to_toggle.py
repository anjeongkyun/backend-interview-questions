# -*- coding: utf-8 -*-
"""답변을 <details> 토글로 감싸고, 문제 풀기 링크를 배지 버튼으로 바꾼다.

    python3 scripts/to_toggle.py          # 미리보기
    python3 scripts/to_toggle.py --apply

## 왜

답이 바로 보이면 스스로 답해보는 연습이 안 된다. 질문은 크게 두고 답변만 접는다.

## 하는 일

1. `## 질문` 아래 각 `### ...` 의 본문을 `<details><summary>답변</summary>` 로 감싼다
2. `## 연습 문제` 를 `## 문제로 풀어보기` + 배지 버튼으로 바꾸고 UTM 을 붙인다
3. 이미 토글이면 건드리지 않는다 (여러 번 돌려도 안전)
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QDIR = os.path.join(ROOT, 'questions')

UTM = '?utm_source=github&utm_medium=repo&utm_campaign=oss_questions'
BADGE_ALT = '문제로 풀어보기'


def badge_section(guide_url):
    """개념 문서용 버튼. 상대 경로라 GitHub camo 를 거치지 않고 그대로 렌더된다"""
    url = guide_url.split('?')[0] + UTM
    return (f'## 문제로 풀어보기\n\n'
            f'[![{BADGE_ALT}](../../assets/foundry-practice.svg)]({url})\n')


def split_sections(text):
    """`## ` 기준으로 (제목, 본문) 목록. 첫 조각은 머리말"""
    parts = re.split(r'\n(?=## )', text)
    return parts


def wrap_answers(body):
    """`### 질문` 다음 본문을 details 로 감싼다. 돌려주는 값: (새 본문, 감싼 수)"""
    chunks = re.split(r'\n(?=### )', body)
    out, wrapped = [], 0
    for i, chunk in enumerate(chunks):
        if i == 0 or not chunk.startswith('### '):
            out.append(chunk)
            continue
        head, _, rest = chunk.partition('\n')
        rest = rest.strip('\n')
        if not rest:
            out.append(chunk)
            continue
        if rest.lstrip().startswith('<details>'):
            out.append(chunk)          # 이미 토글이다
            continue
        out.append(f'{head}\n\n<details>\n<summary>답변</summary>\n\n{rest}\n\n</details>')
        wrapped += 1
    return '\n\n'.join(out), wrapped


def convert(path):
    text = open(path, encoding='utf-8').read().rstrip('\n')
    sections = split_sections(text)
    changed, wrapped_total = False, 0

    for i, sec in enumerate(sections):
        if sec.startswith('## 질문'):
            new, n = wrap_answers(sec)
            if n:
                sections[i], wrapped_total, changed = new, n, True
        elif sec.startswith('## 연습 문제') or sec.startswith('## 문제로 풀어보기'):
            m = re.search(r'\((https://learn-foundry\.app[^)\s]*)', sec)
            if m:
                sections[i] = badge_section(m.group(1))
                changed = True

    return '\n\n'.join(s.strip('\n') for s in sections) + '\n', changed, wrapped_total


def main():
    apply_now = '--apply' in sys.argv
    total_docs, total_wrapped = 0, 0
    for root, _dirs, files in os.walk(QDIR):
        for f in sorted(files):
            if not f.endswith('.md'):
                continue
            path = os.path.join(root, f)
            new, changed, n = convert(path)
            if not changed:
                continue
            total_docs += 1
            total_wrapped += n
            rel = os.path.relpath(path, ROOT)
            print(f'  {rel}: 답변 {n}개 토글')
            if apply_now:
                open(path, 'w', encoding='utf-8').write(new)
    print(f'\n문서 {total_docs}개 / 토글 {total_wrapped}개'
          + ('' if apply_now else '\n미리보기만 했다. 적용하려면 --apply'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
