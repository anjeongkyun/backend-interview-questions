# 백엔드 면접 질문과 답변

> 백엔드 기술 면접에서 실제로 나오는 질문과, **면접관이 듣고 싶어 하는 답변**을 모읍니다.

정리 노트가 아니라 **답변집**입니다. 개념 설명만으로는 면접에서 막힙니다. "그래서 뭐라고 답해야 하나"와 "이렇게 답하면 틀린다"를 함께 적습니다.

## 답변이 이렇게 생겼습니다

모든 답변이 같은 골격을 지킵니다.

| 순서 | 내용 |
|------|------|
| 정의 | 한두 문장으로 |
| 비교 | 표로. 무엇과 무엇이 어떻게 다른가 |
| 판단 기준 | 실무에서 무엇을 보고 고르나 |
| **흔한 실수** | 이렇게 답하면 틀린다 |

마지막이 이 저장소의 이유입니다. 정답을 적은 자료는 많지만, **틀리는 방식**을 적은 자료는 드뭅니다.

예를 들어 "Cache-Aside 에서 왜 캐시를 갱신하지 않고 삭제하나요?" 의 흔한 실수는 이렇습니다.

> 삭제가 완벽하다고 보는 것. 조회가 DB 에서 옛 값을 읽은 뒤 삭제가 끼어들고, 그 다음 조회가 옛 값을 캐시에 채우는 좁은 창이 남습니다. 만료 시간을 함께 두어 수렴시킵니다.

## 목차

<!-- INDEX:START -->
질문 64개 / 문서 18개

### API 설계

- [HTTP 상태 코드와 에러 응답 설계](questions/api-design/http-status-and-error-design.md) — 질문 4개
- [멱등성과 재시도](questions/api-design/idempotency-and-retry.md) — 질문 4개
- [REST API 설계 원칙](questions/api-design/rest-api-design.md) — 질문 4개

### 캐시

- [캐시 일관성 문제](questions/cache/cache-consistency.md) — 질문 4개
- [캐시 스탬피드 (Thundering Herd)](questions/cache/cache-stampede.md) — 질문 4개
- [캐시 읽기와 쓰기 전략](questions/cache/cache-strategies.md) — 질문 4개

### 데이터베이스

- [B-tree 인덱스](questions/database/btree-index.md) — 질문 4개
- [클러스터드 vs 논클러스터드 인덱스](questions/database/clustered-index.md) — 질문 3개
- [복합 인덱스](questions/database/composite-index.md) — 질문 3개
- [데드락](questions/database/database-deadlock.md) — 질문 3개
- [트랜잭션 격리 수준](questions/database/isolation-levels.md) — 질문 3개
- [낙관적 락 vs 비관적 락](questions/database/optimistic-vs-pessimistic.md) — 질문 3개

### 네트워크

- [TCP 3-way Handshake](questions/network/tcp-3way-handshake.md) — 질문 4개
- [TCP 흐름 제어](questions/network/tcp-flow-control.md) — 질문 4개
- [TCP vs UDP](questions/network/tcp-vs-udp.md) — 질문 3개

### 운영체제

- [컨텍스트 스위칭](questions/operating-system/context-switching.md) — 질문 4개
- [뮤텍스 vs 세마포어](questions/operating-system/mutex-vs-semaphore.md) — 질문 4개
- [프로세스 vs 스레드](questions/operating-system/process-vs-thread.md) — 질문 2개
<!-- INDEX:END -->

## 문제로 풀어보고 싶다면

읽는 것과 답할 수 있는 것은 다릅니다. 각 문서 아래에 그 개념의 **연습 문제 링크**가 있습니다.

[learn-foundry.app](https://learn-foundry.app) 에서 객관식으로 풀고, 틀린 것만 모아 다시 볼 수 있습니다. 로그인 없이 5문제를 먼저 풀어볼 수 있습니다.

| | 이 저장소 | learn-foundry.app |
|---|---|---|
| 하는 일 | 읽고 기여한다 | 풀고 관리한다 |
| 형태 | 질문과 답변 | 객관식 문제, 오답노트, 약점 진단 |
| 로그인 | 필요 없음 | 기록을 남기려면 필요 |

## 기여를 기다립니다

**가장 반가운 기여는 "내가 실제로 받은 질문" 입니다.**

면접에서 받은 질문을 [이슈로 제출](../../issues/new?template=received-question.yml)해주세요. 마크다운을 몰라도 되고 답변을 쓰지 않아도 됩니다. 질문만 있으면 충분합니다.

기여하면 서로에게 남는 것이 있습니다.

- **기여자:** 답변을 쓰면서 가장 확실하게 공부됩니다. 남에게 설명할 수 있어야 아는 것입니다. GitHub 활동 이력에도 남습니다
- **읽는 사람:** 실제로 나온 질문을 봅니다. 예상 질문 목록보다 정확합니다

오타 수정, 사실 오류 신고, 흔한 실수 추가도 모두 환영합니다. 자세한 방법은 [CONTRIBUTING.md](CONTRIBUTING.md) 를 봐주세요.

첫 기여를 찾으신다면 [`good first issue`](../../issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) 라벨을 보세요.

## 왜 만들었나

백엔드 면접을 준비하며 자료를 찾다 보면 두 가지가 아쉬웠습니다.

1. **개념 설명은 많은데 답변 예시가 없다.** TCP 흐름 제어가 무엇인지는 알겠는데, 면접에서 어떻게 답해야 할지는 모릅니다
2. **틀리는 방식을 알려주지 않는다.** 그럴듯하지만 틀린 답을 외우고 가면 꼬리 질문에서 무너집니다

그래서 답변과 흔한 실수를 함께 적기로 했습니다.

한국어 백엔드 면접 자료 중 관리되는 저장소가 마땅치 않다는 점도 이유였습니다. 오래 관리할 생각으로 만듭니다.

## 라이선스

문서는 [CC BY-SA 4.0](LICENSE) 입니다. 출처를 남기면 자유롭게 쓰실 수 있습니다.
