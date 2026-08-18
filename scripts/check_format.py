# -*- coding: utf-8 -*-
"""문서 형식을 검사한다. PR 전에 돌려주세요.

    python3 scripts/check_format.py

검사 항목은 모두 **실제로 화면을 깨뜨렸던 것**들이다. 추측으로 넣은 규칙은 없다.
"""
import os
import re
import sys

QUESTIONS = 'questions'
BANNED = {'—': 'em dash. 쉼표나 문장 나누기로', '·': '중간점. 쉼표나 "와"로',
          '✅': '상태 기호. 그 열의 뜻에 맞는 말로', '❌': '상태 기호',
          '⚠': '상태 기호', '⭐': '상태 기호', '✓': '상태 기호', '✗': '상태 기호'}
FENCE = re.compile(r'```([^\n`]*)\n(.*?)```', re.S)
COMMENT_START = re.compile(r'(--|//|#|/\*|\*)\s')


def ko_aligned(md):
    """코드블록에 한글 열을 공백으로 맞춘 곳.

    한글 고정폭 글꼴이 없어 브라우저에서 프로포셔널 폰트로 대체되고, 글자수를
    맞춰 만든 열은 반드시 어긋난다. 표로 써야 한다.

    판정 규칙 (검출기를 두 번 고쳐서 나온 것이다)

    | 조건 | 이유 |
    |------|------|
    | 블록 안에 열 패턴 줄이 **2개 이상** | 한 줄뿐이면 맞출 상대가 없다. 화살표 표현이 걸렸다 |
    | 그 줄들 중 **아무 곳에나** 한글이 있음 | 왼쪽만 보면 `B-tree     3에서 4번` 같은 줄을 놓친다 |
    | 오른쪽이 코드 주석이면 제외 | `WHERE ... -- 설명` 은 열이 아니라 주석이다 |

    두 번째가 중요하다. 처음에는 왼쪽 라벨에만 한글이 있는지 봤는데, 라벨이
    영문이고 값이 한글인 줄(`B-tree     3에서 4번의 노드 읽기`)을 놓쳤다.
    """
    out = []
    for _tag, body in FENCE.findall(md or ''):
        lines = body.split('\n')
        hits = []
        for line in lines:
            m = re.match(r'^(\s*\S.*?\S)([ ]{2,})(\S.*)$', line)
            if not m:
                continue
            _left, _sp, right = m.groups()
            if COMMENT_START.match(right):   # 코드 주석은 열이 아니다
                continue
            if not re.search(r'[가-힣]', line):
                continue
            hits.append(line)
        if len(hits) >= 2:
            out.append(hits[0].strip()[:50])
    return out


def broken_tables(md):
    """표 구분행 앞에 헤더가 없거나 열 수가 안 맞는 곳. 코드블록은 제외"""
    out = []
    lines = FENCE.sub('', md or '').split('\n')
    for i, line in enumerate(lines):
        if re.match(r'^\s*\|[\s:|-]+\|\s*$', line):
            if i == 0 or line.count('|') != lines[i - 1].count('|'):
                out.append(line.strip()[:40])
    return out


def fence_defects(md):
    """코드블록 서식. mermaid 는 그림이므로 열 정렬 검사에서 빼둔다"""
    out = []
    for tag, block in re.findall(r'```([^\n`]*)\n(.*?)```', md, re.S):
        if tag.strip() == 'mermaid':
            continue
        lines = [l for l in block.rstrip('\n').split('\n') if l.strip()]
        if not lines:
            continue
        indent = min(len(l) - len(l.lstrip(' ')) for l in lines)
        if indent > 0:
            out.append(f'블록 전체가 {indent}칸 들여쓰기됨: {lines[0].strip()[:40]}')
        if re.search(r'\\\\', block):
            out.append(f'역슬래시가 두 개로 보인다: {lines[0].strip()[:40]}')
    return out


def check(path, md):
    errs = []
    for ch, why in BANNED.items():
        if ch in md:
            errs.append(f'금지 문자 {ch} 발견. {why}')
    for l in ko_aligned(md):
        errs.append(f'코드블록에 한글 열 정렬. 표나 mermaid 로 바꿔주세요: {l}')
    for t in broken_tables(md):
        errs.append(f'표 문법 깨짐: {t}')
    for d in fence_defects(md):
        errs.append(d)

    # 개수 표기는 늘어날 때마다 고쳐야 하고 아무도 안 고친다
    for m in re.findall(r'질문\s*\d+\s*개|문서\s*\d+\s*개', md):
        errs.append(f'개수 표기 "{m}". 늘어나면 틀린 값이 된다')

    # 머리말 뼈대
    if not re.search(r'^## 이 개념을 왜 묻나', md, re.M):
        errs.append('"## 이 개념을 왜 묻나" 절이 없다')
    elif re.search(r'^## 이 개념을 왜 묻나\s*\n+\s*<!--', md, re.M):
        errs.append('"## 이 개념을 왜 묻나" 가 아직 껍데기다')

    # 질문(### )마다: 답변이 토글 안에 있고, 흔한 실수가 있어야 한다
    sections = re.split(r'\n### ', md)
    for sec in sections[1:]:
        title = sec.split('\n')[0].strip()
        body = re.split(r'\n## ', sec)[0]
        head = body.split('\n', 1)[1] if '\n' in body else ''
        if '<details>' not in head:
            errs.append(f'답변이 토글(<details>) 안에 없다: "{title[:40]}"')
        elif not re.search(r'<summary>답변</summary>\n\n', body):
            errs.append(f'<summary>답변</summary> 다음에 빈 줄이 있어야 안쪽이 렌더된다. 문구도 "답변" 으로 통일한다: "{title[:40]}"')
        if '흔한 실수' not in body:
            errs.append(f'흔한 실수 없음: "{title[:40]}"')
        if len(body) < 200:
            errs.append(f'답변이 너무 짧음({len(body)}자): "{title[:40]}"')
    return errs


def main():
    if not os.path.isdir(QUESTIONS):
        print(f'{QUESTIONS}/ 디렉터리가 없습니다')
        return 1
    total = bad = 0
    for root, _d, files in os.walk(QUESTIONS):
        for f in sorted(files):
            if not f.endswith('.md'):
                continue
            p = os.path.join(root, f)
            total += 1
            errs = check(p, open(p, encoding='utf-8').read())
            if errs:
                bad += 1
                print(f'\n[{p}]')
                for e in errs[:8]:
                    print(f'  {e}')
                if len(errs) > 8:
                    print(f'  ... 그 외 {len(errs)-8}건')
    print(f'\n문서 {total}개 검사 / 문제 {bad}개')
    if bad:
        print('\nSTYLE.md 를 참고해 고쳐주세요. 형식이 어려우면 그대로 PR 을 올려주셔도 함께 다듬습니다.')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
