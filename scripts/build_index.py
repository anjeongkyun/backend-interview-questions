# -*- coding: utf-8 -*-
"""README 의 목차를 questions/ 구조에서 생성한다.

    python3 scripts/build_index.py

목차를 손으로 관리하면 문서를 추가할 때마다 빠뜨린다. 파일에서 뽑는다.
"""
import os
import re
import sys

QUESTIONS = 'questions'
README = 'README.md'
TOPIC_NAMES = {
    'data-structures': '자료구조', 'operating-system': '운영체제', 'network': '네트워크',
    'database': '데이터베이스', 'cache': '캐시', 'messaging': '메시징',
    'distributed-systems': '분산 시스템', 'api-design': 'API 설계',
    'performance': '성능', 'security': '보안',
}


def main():
    lines = []
    total_q = 0
    for topic in sorted(os.listdir(QUESTIONS)):
        tdir = os.path.join(QUESTIONS, topic)
        if not os.path.isdir(tdir):
            continue
        files = sorted(f for f in os.listdir(tdir) if f.endswith('.md'))
        if not files:
            continue
        lines.append(f'### {TOPIC_NAMES.get(topic, topic)}\n')
        for f in files:
            p = os.path.join(tdir, f)
            text = open(p, encoding='utf-8').read()
            title = next((l[2:].strip() for l in text.split('\n') if l.startswith('# ')), f[:-3])
            n = len(re.findall(r'^### ', text, re.M))
            total_q += n
            lines.append(f'- [{title}]({p}) — 질문 {n}개')
        lines.append('')

    block = f'\n질문 {total_q}개 / 문서 {sum(1 for _ in re.finditer("- .", chr(10).join(lines)))}개\n\n' + '\n'.join(lines)
    md = open(README, encoding='utf-8').read()
    new = re.sub(r'(<!-- INDEX:START -->).*?(<!-- INDEX:END -->)',
                 lambda m: m.group(1) + block + m.group(2), md, flags=re.S)
    open(README, 'w', encoding='utf-8').write(new)
    print(f'목차 갱신: 질문 {total_q}개')
    return 0


if __name__ == '__main__':
    sys.exit(main())
