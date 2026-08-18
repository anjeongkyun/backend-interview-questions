# 기여하는 방법

아래로 갈수록 품이 듭니다. 편한 것부터 하세요.

## 1. 받은 면접 질문 제출

[이슈 열기](../../issues/new?template=received-question.yml)

질문 한 줄만 있으면 충분합니다. 답변을 쓰지 않아도 되고 마크다운을 몰라도 됩니다. 회사명 대신 규모나 직군만 알려주셔도 도움이 됩니다.

## 2. 틀린 내용이나 오타 알려주기

답변 내용이 사실과 다르거나 오타가 보이면 [이슈로 알려주세요](../../issues/new?template=error-report.yml). 직접 고칠 수 있으면 PR 이 더 좋습니다.

## 3. 틀렸던 경험 보태기

각 답변 끝에는 "흔한 실수" 항목이 있습니다. 그럴듯하지만 틀린 답을 적어두는 자리입니다.

면접에서 이렇게 답했다가 막혔다는 경험이 있으면 그 자리에 보태주세요. 본인이 직접 틀려본 것이 가장 유용합니다.

## 4. 답변 작성

`answer-needed` 라벨이 붙은 질문에 답변을 써주세요. 형식은 [STYLE.md](STYLE.md)를 따릅니다.

쓰면서 공부하는 게 목적이라면 이게 효과가 가장 큽니다.

---

## PR 보내기

```bash
git checkout -b add-tcp-flow-control-answer
# questions/<토픽>/<개념>.md 를 고치거나 추가
python3 scripts/check_format.py     # 형식 검사
python3 scripts/build_index.py      # 목차 갱신
```

## 커밋 메시지는 영어로

문서는 한국어지만 **커밋 메시지는 영어**로 씁니다. 오픈소스 저장소의 일반 관례이고,
`git log` 는 저장소를 처음 보는 사람이 읽는 곳입니다.

| 규칙 | 예 |
|------|-----|
| 명령형 현재 시제 | `Add`, `Fix`, `Update`. `Added`, `Fixing` 이 아니다 |
| 첫 줄은 50자 안쪽, 마침표 없이 | `Add canonical terms to concept definitions` |
| 무엇을 왜 바꿨는지 본문에 | 한 줄 비우고 72자로 줄바꿈 |

**바꾼 내용만 씁니다.** 어디서 제안이 왔는지, 누가 지적했는지 같은 경위는 넣지 않습니다.
읽는 사람에게 필요한 것은 무엇이 달라졌는지입니다.

```
좋음:  Add canonical terms to concept definitions

       Answers explained mechanics without naming the standard term, so
       readers had no short handle to compress the explanation.

나쁨:  대표 용어를 답변 첫 문장에 넣는다 (독자 제보 반영)
```

## 리뷰에서 보는 것

| 항목 | 기준 |
|------|------|
| 사실 | 틀린 내용이 없는지 |
| 형식 | [STYLE.md](STYLE.md) 골격을 지키는지. 답변은 `<details>` 안에 |
| 흔한 실수 | 있는지. 없으면 답변이 절반이다 |
| 문장 | em dash, 중간점, 상태 이모지, 코드블록 한글 열맞춤 금지 |

## 기여한 내용은 어디에 쓰이나

PR 이 병합되면 이 저장소에 바로 공개됩니다.

[learn-foundry.app](https://learn-foundry.app?utm_source=github&utm_medium=repo&utm_campaign=oss_contributing)의 학습 콘텐츠로 반영될 수 있습니다. 자동은 아니고 선별해서 문제와 해설로 다듬어 넣으며, 반영되면 커밋과 크레딧에 남깁니다.

두 곳은 각자 관리됩니다. 저장소는 읽는 사람을 위해 자세히 쓰고, 서비스는 문제로 풀기 좋게 다듬습니다.

라이선스는 [CC BY-SA 4.0](LICENSE)입니다. 기여하면 같은 라이선스로 배포되는 것에 동의하는 것으로 봅니다.

## 행동 규범

면접 준비는 불안한 시기에 하는 일입니다. 서로에게 너그럽게 대해주세요. 특정 회사나 사람을 비방하는 내용은 병합하지 않습니다.
