# Kakao OG Cache-Bust Experiment Log

> 계획서: `.omc/plans/kakao-cache-bust-test.md`
> 가설:
> - **H1**: Kakao OG scraper가 URL + query parameter를 별개 cache key로 다루는가?
> - **H2**: H1이 참이라면 새 query param으로 공유 시 새 OG 반영되는가?

## 통제 변수 (모든 Round 공통)

| 변수 | 값 |
|------|-----|
| 카카오 계정 | (실험 전 기록) |
| 공유 채널 | "나와의 채팅" |
| 디바이스 | (실험 전 기록) |
| base URL | `https://coen90.github.io/kakao-cache-bust-test/` |
| og:url | `https://coen90.github.io/kakao-cache-bust-test/` (query param 미포함) |
| 공유 방식 | 카카오톡 채팅창에 URL을 직접 텍스트로 붙여넣기 |

## 핵심 원칙

> **카카오톡 직접 공유 → Sharing Debugger 호출 순서를 모든 Round에서 엄수.**
> Debugger의 force re-scrape가 캐시를 오염시킬 수 있기 때문에 직접 공유를 먼저 한다.

---

## 기록 템플릿

각 Step마다 아래 항목을 채워서 기록한다.

```
### [Round X / Step Y] <행위 요약>
- 타임스탬프(KST):
- 배포 git commit hash:
- 테스트 URL:
- 카카오톡 미리보기 스크린샷: screenshots/rX-stepY-kakao.png
- Sharing Debugger 결과 스크린샷: screenshots/rX-stepY-debugger.png
- 관찰 요약:
- 비고:
```

---

## Round 1 — 기준선 확립 (배포 OG: V1)

### [R1 / Step 1-2] 배포 (og:image=og-v1.png, og:title="Cache Test V1")
- 타임스탬프(KST):
- 배포 git commit hash:
- 배포 검증(curl 폴링 결과): og-v1.png 노출 확인
- 비고:

### [R1 / Step 3] 카카오톡에 `?v=1` 직접 공유
- 타임스탬프(KST):
- 테스트 URL: `https://coen90.github.io/kakao-cache-bust-test/?v=1`
- 카카오톡 미리보기 스크린샷:
- 관찰 요약:
- 비고:

### [R1 / Step 4] 카카오톡에 `?v=2` 직접 공유
- 타임스탬프(KST):
- 테스트 URL: `https://coen90.github.io/kakao-cache-bust-test/?v=2`
- 카카오톡 미리보기 스크린샷:
- 관찰 요약:
- 비고:

### [R1 / Step 5] Sharing Debugger에서 `?v=1` 스크래핑
- 타임스탬프(KST):
- Debugger 결과 스크린샷:
- 관찰 요약:
- 비고:

### [R1 / Step 6] Sharing Debugger에서 `?v=2` 스크래핑
- 타임스탬프(KST):
- Debugger 결과 스크린샷:
- 관찰 요약:
- 비고:

### [R1 / Step 7] Debugger 호출 후 카카오톡에 `?v=1` 다시 공유 (observer effect 측정)
- 타임스탬프(KST):
- 카카오톡 미리보기 스크린샷:
- 관찰 요약 (Step 3과 동일/상이):
- 비고:

---

## Round 2 — query param 분리 검증 준비 (재배포 없이, OG: V1 유지)

### [R2 / Step 8] [재배포 없이] 카카오톡에 `?v=3` 직접 공유
- 타임스탬프(KST):
- 테스트 URL: `https://coen90.github.io/kakao-cache-bust-test/?v=3`
- 카카오톡 미리보기 스크린샷:
- 관찰 요약 (V1 보여야 정상):
- 비고:

### [R2 / Step 9] Sharing Debugger에서 `?v=3` 스크래핑
- 타임스탬프(KST):
- Debugger 결과 스크린샷:
- 관찰 요약:
- 비고:

### [R2 / Step 10] Debugger 호출 후 카카오톡에 `?v=2` 다시 공유 (observer effect 측정)
- 타임스탬프(KST):
- 카카오톡 미리보기 스크린샷:
- 관찰 요약 (Step 4와 동일/상이):
- 비고:

---

## Round 3 — OG 변경 + 캐시 키 독립성 검증 (배포 OG: V1 → V2)

### [R3 / Step 11-12] 재배포 (og:image=og-v2.png, og:title="Cache Test V2")
- 타임스탬프(KST):
- 배포 git commit hash:
- 배포 검증(curl 폴링 결과): og-v2.png 노출 확인
- GitHub Pages CDN 응답 헤더 (`curl -I` Cache-Control):
- 비고:

### [R3 / Step 13] 카카오톡에 `?v=3` 직접 공유 (Debugger 호출 전!)
- 타임스탬프(KST):
- 테스트 URL: `https://coen90.github.io/kakao-cache-bust-test/?v=3`
- 카카오톡 미리보기 스크린샷:
- 핵심 관찰 (V2이면 H2 지지):
- 비고:

### [R3 / Step 14] 카카오톡에 `?v=1` 직접 공유 (Debugger 호출 전!)
- 타임스탬프(KST):
- 테스트 URL: `https://coen90.github.io/kakao-cache-bust-test/?v=1`
- 카카오톡 미리보기 스크린샷:
- 핵심 관찰 (V1이면 H1 지지, V2이면 H1 반증):
- 비고:

### [R3 / Step 15] Sharing Debugger에서 `?v=3` 스크래핑
- 타임스탬프(KST):
- Debugger 결과 스크린샷:
- 관찰 요약:
- 비고:

### [R3 / Step 16] Sharing Debugger에서 `?v=1` 스크래핑
- 타임스탬프(KST):
- Debugger 결과 스크린샷:
- 관찰 요약:
- 비고:

### [R3 / Step 17] Debugger 호출 후 카카오톡에 `?v=1` 다시 공유 (observer effect 측정)
- 타임스탬프(KST):
- 카카오톡 미리보기 스크린샷:
- 관찰 요약 (Step 14와 동일/상이):
- 비고:

---

## 1차 판정 (Round 3 결과 기반, preliminary)

- **H1**: 입증 / 반증 / 미결
- **H2**: 입증 / 반증 / 미결
- **근거**: 결과 해석 매트릭스의 어느 행에 해당하는지 기록
- **Debugger observer effect**: 있음 / 없음 (Step 7, 10, 17 비교 결과)

### H1 반증 시 Fallback Protocol 결과 (해당 시 작성)

- 새 query param(`?v=10`, `?v=11`) 사용:
- Debugger 미사용 반복 결과:
- 결론 (Debugger의 observer effect 영향):

---

## Round 4 — 캐시 TTL 관찰 (H1 입증 시 필수)

### [R4 / Step 18] Round 3 완료 후 30분 시점, 카카오톡에 `?v=1` 재공유
- 타임스탬프(KST):
- 카카오톡 미리보기 스크린샷:
- 관찰 요약 (V1 → V2 전환 여부):
- 비고:

### [R4 / Step 19] Round 3 완료 후 1시간 시점, 카카오톡에 `?v=1` 재공유
- 타임스탬프(KST):
- 카카오톡 미리보기 스크린샷:
- 관찰 요약:
- 비고:

### [R4 / Step 20] Round 3 완료 후 2시간 시점, 카카오톡에 `?v=1` 재공유
- 타임스탬프(KST):
- 카카오톡 미리보기 스크린샷:
- 관찰 요약:
- 비고:

---

## 최종 판정 (definitive)

- **H1**: 입증 / 반증 / 미결
- **H2**: 입증 / 반증 / 미결
- **TTL 근사값** (V1 → V2 전환 시점):
- **실무 적용 가능 여부**:
- **추가 실험이 필요한 부분**:
