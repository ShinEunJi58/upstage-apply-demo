# GitHub Actions 워크플로우 설명서
## Marp 프레젠테이션 자동 배포 시스템

### 📌 이 파일이 하는 일
`presentation.md` 파일을 수정하고 GitHub에 푸시하면, **자동으로** 웹사이트(HTML)로 변환해서 인터넷에 배포해주는 로봇입니다.

---

## 🔧 코드 한 줄씩 설명

### 1. 워크플로우 이름
```yaml
name: Deploy Marp to GitHub Pages
```
- **의미**: 이 자동화 작업의 이름
- **비유**: 로봇의 이름표

---

### 2. 언제 실행될까?
```yaml
on:
  push:
    branches: [ main ]
  workflow_dispatch:
```
- **`push` → `branches: [ main ]`**: `main` 브랜치에 코드를 푸시할 때마다 자동 실행
- **`workflow_dispatch`**: GitHub 웹사이트에서 수동으로 실행 버튼을 눌러도 실행 가능
- **비유**: 
  - 자동 실행 = 문이 열리면 자동으로 켜지는 현관등
  - 수동 실행 = 스위치를 직접 눌러서 켜는 전등

---

### 3. 권한 설정
```yaml
permissions:
  contents: read      # 코드 읽기 권한
  pages: write        # GitHub Pages에 쓰기 권한
  id-token: write     # 보안 토큰 발급 권한
```
- **의미**: 이 로봇이 할 수 있는 일의 범위를 정함
- **비유**: 회사 출입증의 접근 권한 (1층 출입 가능, 2층 출입 가능 등)

---

### 4. 작업 1: 빌드 (Build)
```yaml
jobs:
  build:
    runs-on: ubuntu-latest
```
- **`jobs`**: 할 일 목록
- **`build`**: 첫 번째 작업 이름 (HTML 파일 만들기)
- **`runs-on: ubuntu-latest`**: 우분투(리눅스) 컴퓨터에서 실행
- **비유**: 요리 레시피의 "재료 준비" 단계

#### 4-1. 코드 가져오기
```yaml
- uses: actions/checkout@v4
```
- **의미**: GitHub 저장소의 코드를 작업 컴퓨터로 복사
- **비유**: 요리하기 전에 냉장고에서 재료를 꺼내는 것

#### 4-2. Marp → HTML 변환
```yaml
- name: Convert Marp to HTML
  run: |
    npx @marp-team/marp-cli@latest docs/presentation.md --html -o index.html
```
- **`npx @marp-team/marp-cli@latest`**: Marp 변환 도구를 다운로드하고 실행
- **`docs/presentation.md`**: 변환할 원본 파일
- **`--html -o index.html`**: HTML 형식으로 `index.html` 파일로 저장
- **비유**: 
  - 한글 문서(.hwp)를 PDF로 변환하는 것
  - Markdown → HTML 변환

#### 4-3. 결과물 업로드
```yaml
- name: Upload artifact
  uses: actions/upload-pages-artifact@v3
  with:
    path: '.'
```
- **의미**: 만들어진 `index.html` 파일을 임시 저장소에 업로드
- **`path: '.'`**: 현재 폴더의 모든 파일
- **비유**: 완성된 요리를 서빙 카운터에 올려두는 것

---

### 5. 작업 2: 배포 (Deploy)
```yaml
deploy:
  environment:
    name: github-pages
    url: ${{ steps.deployment.outputs.page_url }}
  runs-on: ubuntu-latest
  needs: build
```
- **`needs: build`**: `build` 작업이 끝난 후에만 실행 (순서 보장)
- **`environment: github-pages`**: GitHub Pages 환경에 배포
- **비유**: 요리가 완성된 후에 손님 테이블로 서빙하는 것

#### 5-1. 웹사이트에 배포
```yaml
- name: Deploy to GitHub Pages
  id: deployment
  uses: actions/deploy-pages@v4
```
- **의미**: 업로드된 HTML 파일을 실제 웹사이트로 공개
- **결과**: https://shineun ji58.github.io/upstage-apply-demo/ 에서 접속 가능
- **비유**: 완성된 요리를 손님에게 제공

---

## 🎯 전체 흐름 요약

```
1. 코드 푸시 (git push)
   ↓
2. GitHub Actions 자동 실행
   ↓
3. [Build] presentation.md → index.html 변환
   ↓
4. [Build] 변환된 파일 임시 저장
   ↓
5. [Deploy] GitHub Pages에 배포
   ↓
6. 웹사이트 업데이트 완료! 🎉
```

---

## 💡 실생활 비유

**블로그 자동 발행 시스템**과 비슷합니다:

1. **글 작성** = `presentation.md` 수정
2. **저장 버튼** = `git push`
3. **자동 변환** = Markdown → 예쁜 웹페이지
4. **자동 발행** = 인터넷에 공개

---

## 🔍 자주 묻는 질문 (FAQ)

### Q1: 이 파일을 수정해야 하나요?
**A**: 아니요! 한 번 설정하면 건드릴 필요 없습니다. `presentation.md`만 수정하세요.

### Q2: 배포가 얼마나 걸리나요?
**A**: 보통 1-2분 정도 걸립니다. GitHub Actions 탭에서 진행 상황을 확인할 수 있습니다.

### Q3: 실패하면 어떻게 하나요?
**A**: GitHub Actions 탭에서 빨간색 X 표시를 클릭하면 에러 로그를 볼 수 있습니다.

---

## 📚 관련 용어 정리

| 용어 | 설명 |
|------|------|
| **GitHub Actions** | GitHub에서 제공하는 자동화 도구 (CI/CD) |
| **Workflow** | 자동화 작업의 전체 흐름 |
| **Job** | 워크플로우 안의 개별 작업 단위 |
| **Step** | Job 안의 세부 단계 |
| **Artifact** | 작업 중간에 생성된 파일 |
| **Deploy** | 웹사이트에 배포(공개)하는 것 |
