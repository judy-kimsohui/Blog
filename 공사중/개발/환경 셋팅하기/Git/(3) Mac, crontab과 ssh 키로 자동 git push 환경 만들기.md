---
title: (3) Mac, crontab과 ssh 키로 자동 git push 환경 만들기
draft: false
tags: 
date:
---

#### 요구 사항

1. Mac 환경
2. 작업 중인 내용을 git에 매일 6시간마다 자동으로 커밋하고, 푸시하고 싶다.
3. 두 개의 Repository와 연결해야 한다. (origin이 2개)
4. 커밋 내용은 현재 날짜를 기준으로 한다.

---
#### 1. ssh 키 생성


터미널로 이동하여 다음과 같이 입력한다.
```
ssh-keygen -t ed25519 -C "깃허브 등록 메일"
```

다음과 같은 문장이 나오면 Enter를 누르자.
```
Enter passphrase (empty for no passphrase): 
Enter same passphrase again:
```

성공적이면, 다음과 같은 문장이 나온다.
```
Your identification has been saved in 블라블라
Your public key has been saved in 블라블라

The key fingerprint is: 블라블라
The key's randomart image is: 블라블라
```

"Your public key has been saved in" 다음의 경로를 복사해서, 다음과 같이 입력하자.
```
cat [복사한 경로]

// 예시
cat [어떤 경로].ssh/id_ed25519.pub
```

그럼, ssh-ed25519로 시작하고 이메일로 끝나는 형태의 ssh키가 나오게 되는데, 이를 모두 복사한다.

---

GitHub 웹사이트로 이동하자.
계정 설정(오른쪽 상단 프로필 이미지 > Settings)으로 이동하여 “SSH and GPG keys” 섹션을 찾는다.
“New SSH key” 버튼을 클릭하고, 복사한 공개 키를 붙여넣는다.

키 이름은 원하는대로 설정해도 된다.

---

다시 터미널로 돌아와서, 다음과 같이 입력한다.
```
eval "$(ssh-agent -s)"
open ~/.ssh/config
```

만약, ".ssh/config does not exist." 와 같은 문구가 나타난다면 다음과 같이 추가로 입력한다.
```
touch ~/.ssh/config
vi ~/.ssh/config
```

vi파일에 들어왔으면, a 또는 i를 눌러 편집 모드로 이동 후, 다음과 같이 입력한다.
```
Host github.com
  AddKeysToAgent yes
  IdentityFile ~/.ssh/id_ed25519
```

esc를 눌러 편집 모드 종료 후 읽기 모드로 돌아오고, :wq를 입력해 저장 후 터미널로 돌아간다.

ssh 키를 등록한다.
```
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
ssh -T git@github.com
```

다음 문장이 나올 것이다.
```
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

yes라고 입력해준다.
만약 Enter를 입력하게 된다면 "Host key verification failed." 가 되니 주의하자.

입력 후 다음 문장이 나올 것이다.
```
Permanently added 'github.com' (ED25519) to the list of known hosts.
You've successfully authenticated, but GitHub does not provide shell access.
```

성공적으로 ssh 키 등록을 완료했다.

---
#### 2. git origin 경로 ssh 형식으로 재설정


git에 올리고자 하는 폴더 경로
```
/Users/folder
```

Repository 경로
```
// 개인 경로
origin git@github.com:깃허브유저이름/레파지토리이름.git (fetch)
origin git@github.com:깃허브유저이름/레파지토리이름.git (push)

// 팀 워크스페이스 경로
origin2 git@github.com:팀스페이스이름/레파지토리이름.git (fetch)
origin2 git@github.com:팀스페이스이름/레파지토리이름.git (push)
```

Repository 경로 추가 방법 (origin, origin2), origin 이름은 당연히 변경 가능하다.
```
git remote set-url origin git@github.com:깃허브유저이름/레파지토리이름.git
git remote set-url origin2 git@github.com:팀스페이스이름/레파지토리이름.git
```

Repository 기존 경로 삭제 방법
```
git remote set-url --delete origin git@github.com:깃허브유저이름/레파지토리이름.git

// 또는 push일 경우
git remote set-url --delete origin --push git@github.com:깃허브유저이름/레파지토리이름.git
```

---
#### 3. 현재 폴더에 업데이트 스크립트 파일 생성, crontab 등록


git에 올리고자 하는 폴더 안에 "git-backup" 폴더를 만들어주고, "git-backup.sh" 파일을 생성한다.

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

vi파일에 들어왔으면, a 또는 i를 눌러 편집 모드로 이동 후, 다음과 같이 입력한다.

우선, 제대로 작동하는지 확인하기 위해 매 분마다 실행하도록 실험할 예정이다.
```
* * * * * /Users/folder/git-backup/git-backup.sh
```

로그 파일을 추가하는 방법은 다음과 같다. "git-backup" 폴더 안에 로그 파일이 추가되고, 매 분마다 자동으로 실행 성공 여부가 기록된다.
```
 * * * * * /Users/folder/git-backup/git-backup.sh >> /Users/folder/git-backup/git-backup.log 2>&1
```

esc를 눌러 편집 모드 종료 후 읽기 모드로 돌아오고, :wq를 입력해 저장 후 터미널로 돌아간다.

---

"git-backup.log" 파일을 열어 매 분마다 자동으로 github에 실행되는지 확인해보자.

만약 오류가 난다면, "/Users/folder/git-backup" 경로에서 터미널을 열어 다음과 같이 파일을 직접 실행해보자.
```
chmod +x git-backup.sh
./git-backup.sh
```

ssh키 등록을 잘 했는지, Repository 설정을 잘 했는지 꼭 확인하고, 실행 결과를 보며 천천히 오류를 해결하자.

모든 오류를 수정하고 성공적으로 커밋과 푸시가 된다면, 다음 문법을 적용해서 커스텀해보자.
```
* * * * *: 매 분마다 실행
0 * * * *: 한 시간마다 실행
0 0 * * *: 하루에 한 번 자정에 실행
0 0,6,12,18 * * *: 하루에 4번 0시, 6시, 12시, 18시에 실행
0 12 * * 1-5: 평일(월요일-금요일) 매일 정오에 실행
0 0 * * 1: 매주 월요일 자정에 실행
30 2 * * *: 매일 오전 2시 30분에 실행
```