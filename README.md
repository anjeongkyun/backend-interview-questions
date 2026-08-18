# 백엔드 면접 질문과 답변

백엔드 면접에서 실제로 나오는 질문을 모으고, 면접관이 듣고 싶어 하는 답변과 함께 **그럴듯하지만 틀리는 답변**까지 적었습니다.

## 목차

<!-- INDEX:START -->
### 운영체제

- [컨텍스트 스위칭이란 무엇이고 언제 발생하나요?](questions/operating-system/context-switching.md#컨텍스트-스위칭이란-무엇이고-언제-발생하나요)
- [프로세스 전환과 스레드 전환의 비용 차이는?](questions/operating-system/context-switching.md#프로세스-전환과-스레드-전환의-비용-차이는)
- [컨텍스트 스위칭의 간접 비용(캐시)을 설명해주세요.](questions/operating-system/context-switching.md#컨텍스트-스위칭의-간접-비용캐시을-설명해주세요)
- [컨텍스트 스위칭 오버헤드를 줄이는 방법은?](questions/operating-system/context-switching.md#컨텍스트-스위칭-오버헤드를-줄이는-방법은)
- [뮤텍스와 세마포어의 차이를 설명해주세요.](questions/operating-system/mutex-vs-semaphore.md#뮤텍스와-세마포어의-차이를-설명해주세요)
- [이진 세마포어와 뮤텍스의 차이는?](questions/operating-system/mutex-vs-semaphore.md#이진-세마포어와-뮤텍스의-차이는)
- [경쟁 조건(Race Condition)이란 무엇인가요?](questions/operating-system/mutex-vs-semaphore.md#경쟁-조건race-condition이란-무엇인가요)
- [실무에서 세마포어가 사용되는 예시를 들어주세요.](questions/operating-system/mutex-vs-semaphore.md#실무에서-세마포어가-사용되는-예시를-들어주세요)
- [프로세스와 스레드의 차이를 설명해주세요](questions/operating-system/process-vs-thread.md#프로세스와-스레드의-차이를-설명해주세요)
- [멀티 프로세스 vs 멀티 스레드, 언제 뭘 쓰나요?](questions/operating-system/process-vs-thread.md#멀티-프로세스-vs-멀티-스레드-언제-뭘-쓰나요)
- [가상 메모리가 무엇이고 왜 필요한가요?](questions/operating-system/virtual-memory.md#가상-메모리가-무엇이고-왜-필요한가요)
- [페이지 폴트가 나면 무슨 일이 일어나나요?](questions/operating-system/virtual-memory.md#페이지-폴트가-나면-무슨-일이-일어나나요)
- [스왑이 일어나면 왜 그렇게 느려지나요?](questions/operating-system/virtual-memory.md#스왑이-일어나면-왜-그렇게-느려지나요)

### 네트워크

- [브라우저에 주소를 입력하고 첫 응답이 오기까지 무슨 일이 일어나나요?](questions/network/dns-and-request-flow.md#브라우저에-주소를-입력하고-첫-응답이-오기까지-무슨-일이-일어나나요)
- [DNS 조회는 어떤 순서로 이루어지나요?](questions/network/dns-and-request-flow.md#dns-조회는-어떤-순서로-이루어지나요)
- [같은 도메인인데 응답이 사람마다 다른 IP 로 오는 이유는?](questions/network/dns-and-request-flow.md#같은-도메인인데-응답이-사람마다-다른-ip-로-오는-이유는)
- [HTTPS 는 어떻게 안전한 통신을 만드나요?](questions/network/https-and-tls.md#https-는-어떻게-안전한-통신을-만드나요)
- [인증서는 무엇을 보증하나요?](questions/network/https-and-tls.md#인증서는-무엇을-보증하나요)
- [TLS 1.3 이 1.2 보다 빠른 이유는?](questions/network/https-and-tls.md#tls-13-이-12-보다-빠른-이유는)
- [TCP 3-way handshake 과정을 설명해주세요](questions/network/tcp-3way-handshake.md#tcp-3-way-handshake-과정을-설명해주세요)
- [왜 2-way가 아니라 3-way인가요?](questions/network/tcp-3way-handshake.md#왜-2-way가-아니라-3-way인가요)
- [TCP 연결 해제 과정(4-way handshake)을 설명해주세요](questions/network/tcp-3way-handshake.md#tcp-연결-해제-과정4-way-handshake을-설명해주세요)
- [SYN Flood 공격이란? 대응 방법은?](questions/network/tcp-3way-handshake.md#syn-flood-공격이란-대응-방법은)
- [TCP 흐름 제어와 혼잡 제어의 차이를 설명해주세요.](questions/network/tcp-flow-control.md#tcp-흐름-제어와-혼잡-제어의-차이를-설명해주세요)
- [슬라이딩 윈도우 방식은 어떻게 동작하나요?](questions/network/tcp-flow-control.md#슬라이딩-윈도우-방식은-어떻게-동작하나요)
- [Slow Start와 혼잡 회피의 차이점은?](questions/network/tcp-flow-control.md#slow-start와-혼잡-회피의-차이점은)
- [실제 전송 윈도우 크기는 어떻게 결정되나요?](questions/network/tcp-flow-control.md#실제-전송-윈도우-크기는-어떻게-결정되나요)
- [TCP와 UDP 차이를 설명해주세요](questions/network/tcp-vs-udp.md#tcp와-udp-차이를-설명해주세요)
- [게임 서버에서 UDP를 쓰는 이유는?](questions/network/tcp-vs-udp.md#게임-서버에서-udp를-쓰는-이유는)
- [HTTP/3가 UDP 기반(QUIC)인 이유는?](questions/network/tcp-vs-udp.md#http3가-udp-기반quic인-이유는)

### 데이터베이스

- [ACID 를 각각 설명하고, 어떤 문제를 막아주는지 말해주세요.](questions/database/acid-and-transaction.md#acid-를-각각-설명하고-어떤-문제를-막아주는지-말해주세요)
- [커밋했는데 서버가 바로 죽어도 데이터가 남는 이유는?](questions/database/acid-and-transaction.md#커밋했는데-서버가-바로-죽어도-데이터가-남는-이유는)
- [트랜잭션을 길게 잡으면 무엇이 문제인가요?](questions/database/acid-and-transaction.md#트랜잭션을-길게-잡으면-무엇이-문제인가요)
- [B-tree 인덱스의 구조와 동작 원리를 설명해주세요.](questions/database/btree-index.md#b-tree-인덱스의-구조와-동작-원리를-설명해주세요)
- [B-tree와 Hash 인덱스의 차이는 무엇인가요?](questions/database/btree-index.md#b-tree와-hash-인덱스의-차이는-무엇인가요)
- [인덱스를 타지 않는 쿼리 패턴은 어떤 것이 있나요?](questions/database/btree-index.md#인덱스를-타지-않는-쿼리-패턴은-어떤-것이-있나요)
- [인덱스를 많이 만들면 어떤 문제가 생기나요?](questions/database/btree-index.md#인덱스를-많이-만들면-어떤-문제가-생기나요)
- [클러스터드 인덱스와 논클러스터드 인덱스의 차이를 설명해주세요](questions/database/clustered-index.md#클러스터드-인덱스와-논클러스터드-인덱스의-차이를-설명해주세요)
- [MySQL InnoDB에서 PK를 UUID로 설정하면 어떤 문제가 생기나요?](questions/database/clustered-index.md#mysql-innodb에서-pk를-uuid로-설정하면-어떤-문제가-생기나요)
- [테이블에 클러스터드 인덱스가 1개만 가능한 이유는?](questions/database/clustered-index.md#테이블에-클러스터드-인덱스가-1개만-가능한-이유는)
- [복합 인덱스의 최좌선 원칙(Leftmost Prefix Rule)을 설명해주세요](questions/database/composite-index.md#복합-인덱스의-최좌선-원칙leftmost-prefix-rule을-설명해주세요)
- [복합 인덱스에서 컬럼 순서를 어떻게 결정하나요?](questions/database/composite-index.md#복합-인덱스에서-컬럼-순서를-어떻게-결정하나요)
- [WHERE A = ? AND C = ? 쿼리가 INDEX(A, B, C)를 활용할 수 있나요?](questions/database/composite-index.md#where-a---and-c---쿼리가-indexa-b-c를-활용할-수-있나요)
- [데드락이 발생하는 4가지 조건은 무엇인가요?](questions/database/database-deadlock.md#데드락이-발생하는-4가지-조건은-무엇인가요)
- [DB에서 데드락을 예방하는 방법을 설명해주세요](questions/database/database-deadlock.md#db에서-데드락을-예방하는-방법을-설명해주세요)
- [MySQL InnoDB는 데드락을 어떻게 감지하고 처리하나요?](questions/database/database-deadlock.md#mysql-innodb는-데드락을-어떻게-감지하고-처리하나요)
- [트랜잭션 격리 수준 4가지를 설명해주세요](questions/database/isolation-levels.md#트랜잭션-격리-수준-4가지를-설명해주세요)
- [실무에서 주로 어떤 격리 수준을 쓰나요?](questions/database/isolation-levels.md#실무에서-주로-어떤-격리-수준을-쓰나요)
- [MySQL과 PostgreSQL의 기본 격리 수준 차이는?](questions/database/isolation-levels.md#mysql과-postgresql의-기본-격리-수준-차이는)
- [N+1 문제가 무엇이고 왜 생기나요?](questions/database/n-plus-one.md#n1-문제가-무엇이고-왜-생기나요)
- [N+1 문제를 어떻게 발견하나요?](questions/database/n-plus-one.md#n1-문제를-어떻게-발견하나요)
- [N+1 문제를 어떻게 해결하나요?](questions/database/n-plus-one.md#n1-문제를-어떻게-해결하나요)
- [낙관적 락과 비관적 락의 차이를 설명해주세요](questions/database/optimistic-vs-pessimistic.md#낙관적-락과-비관적-락의-차이를-설명해주세요)
- [쇼핑몰 재고 차감에 어떤 락 방식이 적합한가요? 이유는?](questions/database/optimistic-vs-pessimistic.md#쇼핑몰-재고-차감에-어떤-락-방식이-적합한가요-이유는)
- [낙관적 락에서 충돌이 발생하면 어떻게 처리하나요?](questions/database/optimistic-vs-pessimistic.md#낙관적-락에서-충돌이-발생하면-어떻게-처리하나요)

### 캐시

- [DB와 캐시의 정합성을 어떻게 맞추나요?](questions/cache/cache-consistency.md#db와-캐시의-정합성을-어떻게-맞추나요)
- [캐시 삭제가 실패하면 어떻게 처리하나요?](questions/cache/cache-consistency.md#캐시-삭제가-실패하면-어떻게-처리하나요)
- [캐시 갱신과 DB 갱신 사이의 경합을 설명해주세요](questions/cache/cache-consistency.md#캐시-갱신과-db-갱신-사이의-경합을-설명해주세요)
- [캐시하면 안 되는 데이터를 판단하는 기준은?](questions/cache/cache-consistency.md#캐시하면-안-되는-데이터를-판단하는-기준은)
- [캐시 스탬피드가 왜 장애로 이어지나요?](questions/cache/cache-stampede.md#캐시-스탬피드가-왜-장애로-이어지나요)
- [TTL 만료가 몰리는 문제를 어떻게 막나요?](questions/cache/cache-stampede.md#ttl-만료가-몰리는-문제를-어떻게-막나요)
- [분산 락으로 갱신을 직렬화할 때 주의할 점은?](questions/cache/cache-stampede.md#분산-락으로-갱신을-직렬화할-때-주의할-점은)
- [배포 직후 트래픽을 안전하게 받으려면 무엇을 준비하나요?](questions/cache/cache-stampede.md#배포-직후-트래픽을-안전하게-받으려면-무엇을-준비하나요)
- [Cache-Aside와 Write-Through 중 무엇을 선택하고 왜 그렇게 판단했나요?](questions/cache/cache-strategies.md#cache-aside와-write-through-중-무엇을-선택하고-왜-그렇게-판단했나요)
- [데이터를 갱신할 때 캐시를 새 값으로 덮지 않고 삭제하는 이유는?](questions/cache/cache-strategies.md#데이터를-갱신할-때-캐시를-새-값으로-덮지-않고-삭제하는-이유는)
- [Write-Back의 위험은 무엇이고 어떻게 완화하나요?](questions/cache/cache-strategies.md#write-back의-위험은-무엇이고-어떻게-완화하나요)
- [캐시 서버가 다운되면 서비스는 어떻게 동작해야 하나요?](questions/cache/cache-strategies.md#캐시-서버가-다운되면-서비스는-어떻게-동작해야-하나요)

### API 설계

- [세션 인증과 JWT 중 무엇을 고르고 왜 그렇게 판단했나요?](questions/api-design/auth-session-vs-jwt.md#세션-인증과-jwt-중-무엇을-고르고-왜-그렇게-판단했나요)
- [JWT 를 쓰면서 로그아웃을 어떻게 구현하나요?](questions/api-design/auth-session-vs-jwt.md#jwt-를-쓰면서-로그아웃을-어떻게-구현하나요)
- [Refresh Token 은 어디에 저장해야 하나요?](questions/api-design/auth-session-vs-jwt.md#refresh-token-은-어디에-저장해야-하나요)
- [모든 응답을 200으로 주고 본문에 에러 코드를 담는 API의 문제는 무엇인가요?](questions/api-design/http-status-and-error-design.md#모든-응답을-200으로-주고-본문에-에러-코드를-담는-api의-문제는-무엇인가요)
- [400과 422, 401과 403을 각각 어떤 기준으로 구분하나요?](questions/api-design/http-status-and-error-design.md#400과-422-401과-403을-각각-어떤-기준으로-구분하나요)
- [클라이언트가 자동 재시도를 판단하려면 서버가 무엇을 제공해야 하나요?](questions/api-design/http-status-and-error-design.md#클라이언트가-자동-재시도를-판단하려면-서버가-무엇을-제공해야-하나요)
- [검증 오류가 여러 필드에서 났을 때 응답을 어떻게 설계하겠습니까?](questions/api-design/http-status-and-error-design.md#검증-오류가-여러-필드에서-났을-때-응답을-어떻게-설계하겠습니까)
- [결제 API에서 타임아웃 후 재시도로 이중 결제가 발생했습니다. 어떻게 막겠습니까?](questions/api-design/idempotency-and-retry.md#결제-api에서-타임아웃-후-재시도로-이중-결제가-발생했습니다-어떻게-막겠습니까)
- [POST를 멱등하게 만드는 방법과 그 한계를 설명해주세요](questions/api-design/idempotency-and-retry.md#post를-멱등하게-만드는-방법과-그-한계를-설명해주세요)
- [PUT이 멱등하다는 말의 정확한 의미는 무엇인가요?](questions/api-design/idempotency-and-retry.md#put이-멱등하다는-말의-정확한-의미는-무엇인가요)
- [재시도 정책을 설계할 때 서버와 클라이언트가 각각 무엇을 책임져야 하나요?](questions/api-design/idempotency-and-retry.md#재시도-정책을-설계할-때-서버와-클라이언트가-각각-무엇을-책임져야-하나요)
- [좋은 REST API 설계 원칙은?](questions/api-design/rest-api-design.md#좋은-rest-api-설계-원칙은)
- [REST vs GraphQL 차이와 선택 기준은?](questions/api-design/rest-api-design.md#rest-vs-graphql-차이와-선택-기준은)
- [API 버저닝 전략을 설명해주세요](questions/api-design/rest-api-design.md#api-버저닝-전략을-설명해주세요)
- [HATEOAS는 왜 실무에서 잘 쓰이지 않나요?](questions/api-design/rest-api-design.md#hateoas는-왜-실무에서-잘-쓰이지-않나요)

### 메시징

- [컨슈머 랙이 계속 늘어납니다. 무엇부터 확인하나요?](questions/messaging/consumer-lag-and-dlq.md#컨슈머-랙이-계속-늘어납니다-무엇부터-확인하나요)
- [처리에 계속 실패하는 메시지는 어떻게 하나요?](questions/messaging/consumer-lag-and-dlq.md#처리에-계속-실패하는-메시지는-어떻게-하나요)
- [처리량을 늘리려고 컨슈머를 늘렸는데 효과가 없습니다. 왜일까요?](questions/messaging/consumer-lag-and-dlq.md#처리량을-늘리려고-컨슈머를-늘렸는데-효과가-없습니다-왜일까요)
- [at-least-once 와 exactly-once 의 차이는 무엇인가요?](questions/messaging/delivery-and-idempotency.md#at-least-once-와-exactly-once-의-차이는-무엇인가요)
- [같은 메시지가 두 번 와도 안전하게 만드는 방법은?](questions/messaging/delivery-and-idempotency.md#같은-메시지가-두-번-와도-안전하게-만드는-방법은)
- [순서가 중요한 메시지는 어떻게 다루나요?](questions/messaging/delivery-and-idempotency.md#순서가-중요한-메시지는-어떻게-다루나요)

### 분산 시스템

- [CAP 정리를 설명해주세요.](questions/distributed-systems/cap-and-consistency.md#cap-정리를-설명해주세요)
- [최종 일관성은 실무에서 어떤 문제를 만드나요?](questions/distributed-systems/cap-and-consistency.md#최종-일관성은-실무에서-어떤-문제를-만드나요)
- [두 서비스에 걸친 작업의 정합성은 어떻게 맞추나요?](questions/distributed-systems/cap-and-consistency.md#두-서비스에-걸친-작업의-정합성은-어떻게-맞추나요)
- [타임아웃을 걸지 않으면 무슨 일이 생기나요?](questions/distributed-systems/timeout-retry-circuit-breaker.md#타임아웃을-걸지-않으면-무슨-일이-생기나요)
- [재시도가 오히려 장애를 키우는 경우는?](questions/distributed-systems/timeout-retry-circuit-breaker.md#재시도가-오히려-장애를-키우는-경우는)
- [서킷 브레이커는 무엇을 해결하나요?](questions/distributed-systems/timeout-retry-circuit-breaker.md#서킷-브레이커는-무엇을-해결하나요)

### 관측과 운영

- [어떤 기준으로 알림을 걸어야 하나요?](questions/observability/alerting-and-slo.md#어떤-기준으로-알림을-걸어야-하나요)
- [SLO 와 에러 버짓은 무엇을 결정해주나요?](questions/observability/alerting-and-slo.md#slo-와-에러-버짓은-무엇을-결정해주나요)
- [장애가 났을 때 알림이 여러 개 쏟아지는 문제는 어떻게 다루나요?](questions/observability/alerting-and-slo.md#장애가-났을-때-알림이-여러-개-쏟아지는-문제는-어떻게-다루나요)
- [로그, 메트릭, 트레이스는 각각 어떤 질문에 답하나요?](questions/observability/logs-metrics-traces.md#로그-메트릭-트레이스는-각각-어떤-질문에-답하나요)
- [평균 응답 시간만 보면 무엇을 놓치나요?](questions/observability/logs-metrics-traces.md#평균-응답-시간만-보면-무엇을-놓치나요)
- [여러 서비스에 걸친 요청이 느릴 때 어떻게 원인을 찾나요?](questions/observability/logs-metrics-traces.md#여러-서비스에-걸친-요청이-느릴-때-어떻게-원인을-찾나요)

### 보안

- [비밀번호를 어떻게 저장해야 하나요?](questions/security/password-storage.md#비밀번호를-어떻게-저장해야-하나요)
- [솔트는 무엇을 막나요?](questions/security/password-storage.md#솔트는-무엇을-막나요)
- [로그인 실패 응답은 어떻게 설계하나요?](questions/security/password-storage.md#로그인-실패-응답은-어떻게-설계하나요)
- [SQL 인젝션은 왜 생기고 어떻게 막나요?](questions/security/sql-injection.md#sql-인젝션은-왜-생기고-어떻게-막나요)
- [바인딩할 수 없는 부분은 어떻게 다루나요?](questions/security/sql-injection.md#바인딩할-수-없는-부분은-어떻게-다루나요)
- [인젝션을 코드 리뷰 없이 잡을 방법이 있나요?](questions/security/sql-injection.md#인젝션을-코드-리뷰-없이-잡을-방법이-있나요)
- [XSS와 CSRF의 차이를 설명해주세요.](questions/security/xss-and-csrf.md#xss와-csrf의-차이를-설명해주세요)
- [XSS를 막는 방법을 순서대로 말해주세요.](questions/security/xss-and-csrf.md#xss를-막는-방법을-순서대로-말해주세요)
- [CSRF는 어떻게 막나요?](questions/security/xss-and-csrf.md#csrf는-어떻게-막나요)
<!-- INDEX:END -->

## 기여하는 방법

**면접에서 받은 질문을 알려주세요.** [이슈 열기](../../issues/new?template=received-question.yml)

질문 한 줄만 있으면 충분합니다. 답변을 쓰지 않아도 되고 마크다운을 몰라도 됩니다. 예상 질문은 인터넷에 흔하지만 실제로 면접에서 나온 질문은 구하기 어려워서, 그 한 줄이 이 저장소에서 가장 값진 기여입니다.

답변에 틀린 내용이 있으면 알려주세요. 오타를 고쳐주셔도 좋고, 면접에서 이렇게 답했다가 틀렸다는 경험을 보태주셔도 좋습니다. 자세한 방법은 [CONTRIBUTING.md](CONTRIBUTING.md)에 있습니다.

## 문제로 풀어보기

[![문제로 풀어보기](assets/foundry-practice.svg)](https://learn-foundry.app?utm_source=github&utm_medium=repo&utm_campaign=oss_questions)

여기서 읽은 개념을 실무 상황을 가정한 문제로 직접 풀면서 검증해보세요. 틀린 문제는 오답노트에 모여 약한 개념부터 다시 볼 수 있습니다.

## 라이선스

[CC BY-SA 4.0](LICENSE). 출처를 남기면 자유롭게 쓰실 수 있습니다.
