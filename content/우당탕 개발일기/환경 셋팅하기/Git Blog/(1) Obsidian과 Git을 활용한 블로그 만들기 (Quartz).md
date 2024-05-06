---
title: (1) Obsidian과 Git을 활용한 블로그 만들기
draft: false
tags: 
date:
---
개발 공부를 하다보니 프로젝트와 기록물이 감당 못할 정도로 많아지게 되었다.
그래서 기록 용으로 Notion을 이용하다가, 자잘한 오류에 싫증이 나 Obsidian으로 옮기게 되었고, 추가로 데일리 루틴 자동화 설정을 위해 노력하고 있다.

이번 편의 주제는 "Obsidian에 쓴 글을 자동으로 블로그에 포스팅 하는 환경 구축"이다.

다음 블로그를 참고해서 만들었다.
[블로그 생성기](https://jongdeug.github.io/blog/IT%EC%9D%BC%EA%B8%B0/%EB%B8%94%EB%A1%9C%EA%B7%B8-%EC%83%9D%EC%84%B1%EA%B8%B0/Part-0.-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EC%9A%B4%EC%98%81-%EC%9D%B4%EC%9C%A0)

#### 요구사항

1. Mac 환경
2. 블로그와 옵시디언 연결하기
3. 매일 0시 자동으로 커밋하고 푸시해서 블로그와 연동하기

---
#### 1. 블로그 폴더 환경 설정하기

Obsidian 내 "blog"라는 이름의 폴더를 새로 만들었다.
![[(1) Obsidian과 Git을 활용한 블로그 만들기 (Quartz)-20240506131127705.png]]

Github 웹사이트에 들어가 Repository를 하나 생성한다.

방금 생성한 블로그 폴더에서 터미널을 열고, git을 시작한다.
```
git init
```

quartz 초기 설정을 한다.
```
npm i
npx quartz create
```

폴더와 깃 Repository를 연결한다.
```
git remote remove origin
git remote add origin 레포지토리주소
```

---

crontab을 활용해서 자동으로 커밋 후 푸시해주는 환경을 만들어준다.

"blog"폴더 안에 "git-backup" 폴더를 만들고, "git-backup.sh" 파일을 생성한다.

"git-backup.sh" 파일에 다음과 같이 입력한다. 현재 날짜 $(date) 를 기준으로 커밋된다.
```
# git-backup.sh

WorkDir="/Users/folder"

cd $WorkDir
git add .
git commit -m "backup $(date)"

git push origin main
git push origin2 main
```

터미널로 이동해서, 다음과 같이 입력한다.
```
crontab -e
```

vi파일에 들어왔으면, a 또는 i를 눌러 편집 모드로 이동 후, 다음과 같이 입력한다. 매일 자정에 자동으로 커밋 후 푸시된다.
```
0 0 * * * /blog/git-backup/git-backup.sh >> /blog/git-backup/git-backup.log 2>&1
```

경로는 각자 환경에 맞게 설정해야 한다. 예시로, "/Users/path/to/blog/"와 같이 설정해야 한다.

처음 설정하는 사람은 아래 포스트를 참고하자.

[[(3) Mac, crontab과 ssh 키로 자동 git push 환경 만들기]] 

---
#### 2. Obsidian 설정하기

커뮤니티 플러그인 중 Templater를 설치한다.
/ 키를 누르고, "Add Property"를 통해 다음과 같이 만든 후 템플릿을 추가해준다.

```
title: <% tp.file.title %>
draft: true
tags:
date:
```

`draft`가 true이면 블로그가 올라가지 않고, 내용을 모두 작성 후 체크를 해제하게 되면 블로그에 올라갈 수 있게 된다.

Templater 옵션 중 Template Hotkey에 템플릿을 추가하게 되면 /키로 템플릿을 검색해 바로 추가할 수 있다.

---

#### 3. Quartz 설정하기

"blog" 폴더의 아래 경로 ".github/workflows"에 "deploy.yml" 파일을 생성한다. 나는 쉬운 편집 위해 vscode로 해당 폴더를 열었다.

![[(1) Obsidian과 Git을 활용한 블로그 만들기 (Quartz)-20240506133218919.png|397]]

다음과 같이 "deploy.yml" 를 작성한다.
```
name: Deploy Quartz site to GitHub Pages
 
on:
  push:
    branches:
      - v4
 
permissions:
  contents: read
  pages: write
  id-token: write
 
concurrency:
  group: "pages"
  cancel-in-progress: false
 
jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0 # Fetch all history for git info
      - uses: actions/setup-node@v3
        with:
          node-version: 18.14
      - name: Install Dependencies
        run: npm ci
      - name: Build Quartz
        run: npx quartz build
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v2
        with:
          path: public
 
  deploy:
    needs: build
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v2
```

---
#### 4. github Actions 설정하기

아까 생성해둔 Repository의 Settings 탭에 들어간다.
왼쪽 메뉴 중 Pages를 찾아 들어가고, Source의 토글을 "Gihub Actions"으로 변경한다.

터미널로 돌아가서, 다음과 같이 입력한다.
```
npx quartz sync
```

이제 커밋 후 푸시하면 저장소에 파일이 올라가고, Repository의 Actions 탭에서 상태를 확인 할 수 있다. deploy가 다 됐다면 황토색에서 녹색으로 상태가 변경된다.

다시 Repository의 Settings 탭에 들어가면, 내 깃허브 블로그 주소가 나온다.

---

이제 옵시디언으로 글을 쓰면, 매일 0시에 자동으로 포스팅이 올라가게 될 것이다.

나는 자동 푸시 외에도 원할 때 쉽게 포스팅 하기 위해, 커뮤니티 플러그인 중 "Git"을 활용해 다음과 같은 설정을 만들었다. 가장 왼쪽 동그라미 화살표를 누르면, 오늘 날짜로 커밋 후 푸시할 수 있다.

![[(1) Obsidian과 Git을 활용한 블로그 만들기 (Quartz)-20240506134243778.png|287]]

---
#### 5. 블로그 스타일 설정하기

기존 블로그 스타일도 깔끔하지만, 나만의 스타일을 적용하고 싶어서 조금 수정했다.
현재도 시간이 날 때마다 조금씩 스타일을 변경하고 있다. 

레이아웃 변경 등의 스타일 변경은 공식 문서를 참고하면 좋다.
[Quartz 레이아웃](https://quartz.jzhao.xyz/layout)

나는 크롬 개발자 도구와 vscode 탐색 기능을 활용해 눈치껏 스타일을 변경했다.
클래스 명을 복사해서 vscode 에서 "command+shift+f"를 누르면 해당 문구가 포함된 모든 파일들이 검색된다. 

##### Tip

Quartz는 리액트로 만들어졌고, 주로 "quartz" 폴더 안을 보면 스크립트와 정적 파일 등을 확인할 수 있다. 살살 수정하면 된다.

1. favicon 수정하기
	 "quartz" 폴더가 아닌, "public" 폴더에 들어가면 icon.png가 있다. 원하는 그림으로 바꾸면 favicon을 수정할 수 있다. 참고로, og-image도 수정이 가능하다.

2. 블로그 내 요소 색상 변경하기
	 "blog/quartz.config.ts" 경로에서, QuartzConfig에서 폰트 색상을 변경할 수 있다. Light 모드와 Dark 모드를 변경할 수 있다.

3. fotter 내용 수정하기
	"blog/quartz/components/Footer.tsx"에서 Footer의 p 부분을 주석 처리하면 create with.. 문구를 삭제할 수 있다. 주석 처리는 `{/* */}` 로 한다.
	내용은 "blog/quartz.layout.ts" 경로에서, SharedLayout "links" 부분을 수정하면 된다.

4. Home 내용 수정하기
	상단의 블로그명을 클릭하면 기본 소개 페이지가 나오는데, "blog/content/index.md"에서 내용 수정이 가능하다.

5. font 수정하기
	"blog/quartz/util/theme.ts"에서 변경 가능하다.

6. 오른쪽, 왼쪽 레이아웃 위치 조정하기
	"blog/quartz/styles/variables.scss"의 topSpacing를 조절하면 된다.

7. 그래프뷰 삭제
	"blog/quartz/components/Graph.tsx"에서 아래 부분을 모두 주석처리했다.
```
<h3>{i18n(cfg.locale).components.graph.title}</h3> 
<div class="graph-outer"></div> 
```

9. 헤더 추가
	"blog/quartz/components/renderPage.tsx"에 추가했다.
```
<div id="quartz-root" class="page">
<div class="header-image" style={{ width: '100%', height: '12px', backgroundColor: '#2d4277' }}></div>
```
	
