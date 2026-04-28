# Kakao Cache-Bust Test

카카오톡 공유 시 OG(Open Graph) 캐시가 URL + query parameter 조합으로 분리되는지 검증하기 위한 매우 간단한 정적 페이지.

배포 URL: https://coen90.github.io/kakao-cache-bust-test/

## 가설

- **H1**: Kakao OG scraper가 URL + query parameter를 별개 cache key로 다루는가?
- **H2**: H1이 참이라면, OG 변경 후 새 query param으로 공유하면 새 OG가 반영되는가?

## 구조

```
.
├── index.html              # OG 메타태그 + 안내 페이지
├── images/
│   ├── og-v1.png           # 1200x630, 파란 배경 + "V1"
│   └── og-v2.png           # 1200x630, 빨간 배경 + "V2"
├── screenshots/            # 실험 스크린샷
├── EXPERIMENT_LOG.md       # 실험 기록
├── scripts/
│   └── generate-og.py      # OG 이미지 생성 스크립트
└── .omc/plans/             # 합의된 실험 계획서
```

## 실험 절차 (요약)

1. **Round 1**: V1 배포, `?v=1`/`?v=2` 카카오톡 직접 공유 → Sharing Debugger 순.
2. **Round 2**: 재배포 없이 `?v=3` 추가 공유 (기준선).
3. **Round 3**: V2로 재배포. **카카오톡 직접 공유부터** `?v=3`, `?v=1` 순 → Debugger 호출은 그 다음.
4. **Round 4** (H1 입증 시): 30분/1시간/2시간 후 `?v=1` 재공유 → TTL 측정.

> **핵심 원칙**: Sharing Debugger는 force re-scrape를 트리거할 수 있으므로, 모든 Round에서 카카오톡 직접 공유를 Debugger 호출보다 먼저 수행한다.

## OG 이미지 재생성

```bash
python3 scripts/generate-og.py
```

## OG 변경 (Round 3 재배포)

`index.html`에서 다음을 V1 → V2로 교체:

- `<title>Cache Test V1</title>` → `Cache Test V2`
- `<meta property="og:title" content="Cache Test V1" />` → `Cache Test V2`
- `<meta property="og:image" content=".../og-v1.png" />` → `og-v2.png`
- 본문의 `og:title`/`og:image` 표 셀, `<img src="images/og-v1.png">`, badge 표시도 `V2`로

`og:url`은 절대 변경하지 않는다 (통제 변수).

## 배포 완료 검증

```bash
until curl -s https://coen90.github.io/kakao-cache-bust-test/ | grep -q "og-v2.png"; do
  echo "배포 대기..."; sleep 10
done
echo "배포 완료"
```
