# -*- coding: utf-8 -*-
"""README 목차를 생성한다.

    python3 scripts/build_index.py            # README 갱신
    python3 scripts/build_index.py --print    # 출력만

## 무엇을 만드나

토픽별로 묶고 **질문 문장 자체를 링크**로 나열한다. 개념 이름만 나열하면 무슨
내용인지 알 수 없어 아무도 안 누른다. 질문은 그 자체로 읽고 싶게 만든다.

개수("질문 4개")는 넣지 않는다. 늘어날 때마다 고쳐야 하고 아무도 안 고친다.
"""
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QDIR = os.path.join(ROOT, 'questions')
README = os.path.join(ROOT, 'README.md')

START, END = '<!-- INDEX:START -->', '<!-- INDEX:END -->'

TOPICS = [
    ('operating-system', '운영체제'),
    ('network', '네트워크'),
    ('database', '데이터베이스'),
    ('cache', '캐시'),
    ('api-design', 'API 설계'),
    ('messaging', '메시징'),
    ('distributed-systems', '분산 시스템'),
    ('observability', '관측과 운영'),
]


def anchor(heading):
    """GitHub 이 제목에 붙이는 앵커를 만든다.

    규칙: 소문자로, 공백은 하이픈, 영숫자와 하이픈과 밑줄 외에는 버린다.
    한글은 그대로 남는다. `?` `,` `(` `)` 같은 문장부호가 사라지는 게 핵심이다.
    """
    s = unicodedata.normalize('NFC', heading).strip().lower()
    s = s.replace(' ', '-')
    return ''.join(ch for ch in s if ch.isalnum() or ch in '-_')


def read_doc(path):
    """(문서 제목, [질문 문장])"""
    text = open(path, encoding='utf-8').read()
    m = re.search(r'^#\s+(.+)$', text, re.M)
    title = m.group(1).strip() if m else os.path.basename(path)
    qs = re.findall(r'^###\s+(.+?)\s*$', text, re.M)
    return title, qs


def build():
    lines = []
    for slug, label in TOPICS:
        tdir = os.path.join(QDIR, slug)
        if not os.path.isdir(tdir):
            continue
        entries = []
        for f in sorted(os.listdir(tdir)):
            if not f.endswith('.md'):
                continue
            _title, qs = read_doc(os.path.join(tdir, f))
            rel = f'questions/{slug}/{f}'
            for q in qs:
                entries.append(f'- [{q}]({rel}#{anchor(q)})')
        if not entries:
            continue
        lines.append(f'### {label}')
        lines.append('')
        lines.extend(entries)
        lines.append('')
    return '\n'.join(lines).rstrip('\n')


def main():
    index = build()
    if '--print' in sys.argv:
        print(index)
        return 0

    text = open(README, encoding='utf-8').read()
    if START not in text or END not in text:
        sys.exit(f'README 에 {START} / {END} 표시가 없다')
    head, rest = text.split(START, 1)
    _old, tail = rest.split(END, 1)
    open(README, 'w', encoding='utf-8').write(f'{head}{START}\n{index}\n{END}{tail}')

    print(f'목차 갱신: 토픽 {index.count("### ")}개 / 질문 링크 {index.count(chr(10) + "- ") + 1}개')
    return 0


if __name__ == '__main__':
    sys.exit(main())
