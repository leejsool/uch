# CLAUDE.md

UniverCityHunter — 대학가 로그라이크. 취미·지인 공유용, 상업 목적 아님.
**자세한 사양·설계·수치는 [`인수인계.md`](인수인계.md) 를 보세요. 이 문서는 규칙만 적습니다.**

## 작업 규칙

- **파일을 고칠 때 읽기보다 쓰기를 먼저 실행하지 말 것.** 읽기 → 변환 → 쓰기 순서.
  이 순서를 어겨서 소스가 통째로 날아간 적이 있음.
- **밸런스 시뮬레이션(승률 측정)은 사용자가 요청할 때만.** 시간·비용이 큼.
- **문법 검사와 동작 검증은 매번 한다.** (`<script>` 만 뽑아 `node --check`, 그리고
  jsdom 으로 실제 화면을 그려 눌러 보기. 방법은 `인수인계.md` §1 참고)
- **코드는 `index.html` 한 파일로 유지한다. 외부 라이브러리 금지.** 캔버스 2D만 사용.
- **배포 전 `index.html` 최상단 `DEV_SHOW_UNLOCK` 를 `false` 로 바꾼다.**
- **설명은 간결하게.** 무엇을 왜 그렇게 했는지 위주로 적는다.

## 저장소

- `main` 브랜치가 곧 배포본. push 하면 GitHub Pages(https://leejsool.github.io/uch/)에 올라간다.
- `python3 build-single.py` → `univercityhunter-single.html` (그림까지 박힌 단일 파일).
