# DNS & ISPL — 개인 홈페이지 (Quarto)

Dongnyok Shim 교수 개인 홈페이지. Quarto 웹사이트로 작성되어 있으며, GitHub에 푸시하면 자동으로 렌더·배포됩니다.

---

## 1. 이번 업데이트 내용

**논문 (Research)**
- 엑셀(`paper_list.xlsx`) 기준 전체 38편으로 갱신, 누락됐던 최신 2편 추가(Gamification in the Metaverse / Consumer Insights e-Payment).
- 등재 구분 배지(SSCI/SCI/Scopus/KCI), 본인 성함 강조, 카드형 레이아웃, 상단 편수 요약.
- 목록은 `gen_pubs.py`로 생성됩니다. 논문 추가 시 이 파일에 한 줄 넣고 `python3 gen_pubs.py` 실행 → `partials/publications.qmd` 재생성.

**강의 (Courses)** — 새로 구성
- 학기·학부/대학원으로 7개 과목 페이지 신설 + 전체 목록 페이지(`courses/index.qmd`).
  - 1학기: 신제품개발과 혁신, 신제품개발 및 관리, 데이터사이언스개론, 기술예측분석시스템(대학원)
  - 2학기: 디지털산업융합론, 통계분석 및 실무, 신상품개발론(대학원)
- 각 페이지는 **과목 소개 + 강의 구성**으로 구성. 강의 슬라이드 4종(신제품개발과혁신·데이터사이언스개론·기술예측분석시스템·디지털산업융합론)을 반영해 모듈·주차·평가를 채웠고, 나머지 3과목은 제목·연구분야 기준의 간단 소개입니다.
- 각 페이지 하단에 **강의자료(Slides/Notes)** 자리(준비 중 안내 + 링크 추가용 주석 템플릿)를 마련해 두었습니다. 추후 자료를 올리고 주석 표를 채우면 됩니다.

**디자인**
- 정제된 학술 에디토리얼 테마(딥 네이비 + 틸, Fraunces 세리프)를 `styles.css`에 덧입혔습니다.
- 네비게이션 색상은 `brand.scss`로 조정합니다(아래 주의 참고).
- 프로필 사진/로고 적용(`images/`).

---

## 2. 폴더 구성

```
.
├─ _quarto.yml              # 사이트 설정(네비·테마·footer). 실제 설정 기반 + Courses 메뉴 7과목 반영
├─ _publish.yml             # quarto.pub 배포 정보(기존)
├─ brand.scss               # 네비 색상 등 SCSS (★ 기존 파일이 있으면 그걸 유지)
├─ styles.css               # 디자인
├─ index.qmd / about.qmd / research.qmd / lab.qmd / projects.qmd / blogs.qmd
├─ partials/
│   └─ publications.qmd      # 논문 목록(about·research에서 include)
├─ courses/                  # ★ 신규
│   ├─ index.qmd             #   전체 강의 목록
│   └─ *.qmd                 #   과목별 페이지 7개
├─ images/                   # 프로필·로고
├─ gen_pubs.py               # 논문 목록 생성 스크립트
└─ .github/workflows/publish.yml   # 자동 배포 워크플로
```

⚠️ **brand.scss 주의**: `_quarto.yml`의 테마가 `[cosmo, brand.scss]`를 참조합니다. 기존에 쓰시던 `brand.scss`가 있다면 **그 파일을 그대로 사용**하세요(이 압축본의 brand.scss는 색상만 맞춘 스타터입니다). 빌드 시 이 파일이 없으면 오류가 납니다.

---

## 3. 로컬 미리보기 (선택)

```bash
quarto preview     # 실시간 미리보기
quarto render      # _site/ 로 렌더
```

---

## 4. GitHub로 배포 (권장: Actions 자동 배포)

푸시할 때마다 GitHub가 렌더해 올려줍니다. 로컬 Quarto가 없어도 됩니다.

1. 저장소 생성 — 주소를 `https://아이디.github.io` 로 쓰려면 저장소 이름을 `아이디.github.io` 로. (아니면 `https://아이디.github.io/저장소이름`)
2. 파일 전체를 main 브랜치로 push
   ```bash
   git init && git add . && git commit -m "Update publications, courses, design"
   git branch -M main
   git remote add origin https://github.com/dongdahi/저장소이름.git
   git push -u origin main
   ```
3. Actions 탭에서 "Publish website" 실행 확인 → `gh-pages` 브랜치 자동 생성
4. **Settings → Pages → Source: Deploy from a branch → `gh-pages` / `/ (root)`**
5. 잠시 후 사이트 공개. `_quarto.yml`의 `site-url` 을 실제 주소로 바꿔 주세요.

이후 `.qmd`나 `gen_pubs.py` 를 고치고 push만 하면 자동 갱신됩니다.

(대안: Actions 없이 쓰려면 `_quarto.yml`의 `output-dir`를 `docs`로 바꾸고 로컬에서 `quarto render` 후 push → Pages 소스를 `main / docs` 로 지정.)

---

## 5. 강의자료 추가하는 법 (추후)

각 과목 페이지 하단 "강의자료" 섹션에 주석으로 표 템플릿을 넣어 두었습니다. 예:

```
| 주차 | 주제 | 슬라이드 | 노트 |
|------|------|---------|------|
| 1주차 | 강의 소개 | [Slides](slides/week01.pdf) | [Notes](notes/week01.html) |
```

슬라이드/노트 파일은 과목 폴더 하위(예: `courses/slides/`, `courses/notes/`)에 두고 위처럼 링크하면 됩니다.

---

## 6. quarto.pub 병행

기존 `_publish.yml` 이 있어 `quarto publish quarto-pub` 으로 quarto.pub에도 계속 배포할 수 있습니다. GitHub Pages와 병행 운영 가능합니다.
