# 수상내역

![reward](https://user-images.githubusercontent.com/108659935/217239819-7c7dc07d-4c75-40a2-acd4-137eb85f38cf.png)

# 웹사이트 주소

[NES](http://nes-env.eba-9ycvw3yi.ap-northeast-2.elasticbeanstalk.com/)

**NES : Never Ending Story의 준말로, 예술전공 학생들의 졸업작품 판매를 시작으로 예술가로서의 삶이 시작되기를 장려하는 뜻. **

---

![image](https://user-images.githubusercontent.com/108659935/217242265-d2461b72-781e-4335-8b79-76969734eecf.png)

<br>

# 목차

1. **웹 서비스 소개**
2. **기술 스택**
3. **주요 기능**
4. **특이사항**
5. **개발 팀 소개**
6. **개발 기간 및 일정**
7. **프로젝트 후기**

<br>

# 1. 서비스 소개

<br>

## 입장시 로딩 페이지

![loading](https://user-images.githubusercontent.com/108659935/217294253-dabcc667-3ac5-408a-a3c8-afc22837c495.gif)

  - 젤 처음 홈페이지에 접속했을 때 팀명 NES 를 JS로 3초안에 글자가 써지도록 띄워준 후 페이지를 이동시킨다.

## 회원 가입 후 로그인

![signup](https://user-images.githubusercontent.com/108659935/217301478-9dabb15b-117c-47fc-a501-214c5142b256.gif)

  - 정해진 양식의 회원가입을 진행하는데 아이디 중복확인을 통해서 아이디가 존재하는지 여부를 확인한다.
  - 가입 양식을 작성하고 이메일 인증을 통해서 실제 이메일로 인증번호를 보내 인증번호를 입력하지 않을 경우 가입할 수 없다.
  - 양식대로 가입을 완료했으면 로그인을 진행하고 로그인이 끝나면 미술관의 컨셉에 맞도록 티켓을 뽑는 홈페이지로 이동시킨다.
  - 티켓 출력버튼을 누르고 "Take a ticket"을 누른 후 티켓을 클릭하면 카테고리 목록 사이트를 보여준다.

<br>

## 테마별 카테고리 페이지

![mainPage (1) (1)](https://user-images.githubusercontent.com/108659935/217307475-84c38465-528d-4098-ae4f-217beaead211.gif)

  - 각 테마별로 색상을 지정하여 스크롤이 이동하면서 그 테마의 위치에 올 경우 배경의 색상을 변화를 주는 것을 구현함
  - 좌우 스크롤로 이동 가능함

<br>

## 메인 페이지 및 네브바

![mainpage (3)](https://user-images.githubusercontent.com/108659935/217312999-213e1333-aa98-4c01-83bf-d0618e4c913a.gif)
  
  - 테마별 페이지에서 왼쪽 NES를 클릭하여 네브바를 펼칠 수 있고 각 테마별로 이동시 무슨 테마로 이동되는지 화면에 띄워준 후 이동한다.

<br>

## 쪽지 보내기

![send](https://user-images.githubusercontent.com/108659935/217314484-8190ebb4-d4e0-4874-b732-35c6478affa0.gif)

  - 유저 프로필 페이지의 비행기 모양을 클릭하여 유저에게 쪽지를 보낼 수 있다.
  - 받은 유저는 쪽지함에 받은 편지라는 항목이 생기고 보낸 유저의 경우 보낸 편지함에 목록이 생성된다.

<br>

## 프로필에 작품 담기 및 댓글 비동기

![save](https://user-images.githubusercontent.com/108659935/217321819-c0ccb871-3d38-44db-a199-688865ce81d2.gif)

  - 작품을 저장하여 내 프로필 페이지에서 자유롭게 볼 수 있고 또한 작품에 댓글작성을 통하여 댓글을 작성할 수 있다.

<br>

## 최근 본 작품 및 작품 구매 페이지

![buy](https://user-images.githubusercontent.com/108659935/217328401-5f8f22bc-2ee0-49db-9867-dcd58d771517.gif)

  - 최근에 본 작품들도 열람할 수 있으며 내가 원하는 작품들을 구매할 수 있는 페이지를 구현했다.
  - 작품 가격에있어서 가격흥정도 작가와 가능하도록 문의하기를 통해서 가격을 작가와 상의할 수 있도록 구현했다.
  - 구매를 누르면 사용자의 기본정보를 가져와서 연락처를 입력한 후 이노시스 API를 통해서 결제가 진행되도록 구현했다.
  
<br>

# 2. 기술 스택

| Frontend | Backend | Cooperation | Release |
| --- | --- | --- | --- |
| HTML5 | Python | Git | S3 |
| CSS3 | Django | GitHub | Elastic beanstalk |
| Bootstrap | SQLite | Notion |  |
| JavaScript | PostgreSQL | Discord |  |
|  | Redis |  |  |

<br>

# 3. 주요 기능

- `회원 가입`
- `로그인`
- `CRUD`
- 

<br>

# 4. 팀원 및 참고 자료

**김예린 - 팀장(BE)**

[ererink - Overview](https://github.com/ererink)

**최근영 - 팀원(FE)**

[choikeunyoung - Overview](https://github.com/choikeunyoung)

**백솔비 - 팀원(FE)**

[hae-on - Overview](https://github.com/hae-on)

**문현동 - 팀원(BE)**

[mhd329 - Overview](https://github.com/mhd329)

**이명학 - 팀원(BE)**

[Emhaki - Overview](https://github.com/Emhaki)


**페이지 구성 Figma**

![image](https://user-images.githubusercontent.com/108659935/217279895-547f6d2d-3cff-4dcb-8168-ca9332e96d74.png)

**모델 ERD 구성**

![image](https://user-images.githubusercontent.com/108659935/217280073-580f3de8-d278-445e-88b7-5dcfc8a6b112.png)

**기획서**

<a href="https://www.notion.so/hg-edu/67e2497e86134ad183d49c9c977e0eb7">기획 Notion</a>

# 5. 개발 중 이슈

<a href="https://github.com/orgs/KDT-NES/projects/1">깃허브 칸반보드 이용하여 진행</a>

# 6. 개발 기간 및 일정

- **개발 기간 : 11.24 (목) ~ 12.14 (수)

![image](https://user-images.githubusercontent.com/108659935/217280653-bc77bad0-04be-45a9-a274-d075ea6f3611.png)


# 7. 내가 한 작업들


# 8. 프로젝트 후기
  
  - 부족하지만 짧은 기간동안 반응형 웹페이지를 고려해 작업하는데 몰두헀던 것 같다.
  - Vanilla JS로 좌우스크롤을 구현하고싶었지만 JS 숙련도 부족으로 인하여 JQuery사용법도 모른채 인터넷 코드를 그대로 사용한 것이 아쉬웠다.
  - 기회가 된다면 Vanila JS에 대해서 좀 더 공부를 해본 후 좌우 스크롤에대해서 다시 도전해보고 싶다.
  - 세번 진행한 프로젝트 중에서 제일 CSS적인 요소를 많이 건들여본 프로젝트 같고 또한 BEM 표기법으로 구현할려고 노력했다.
  - 반응형 웹페이지를 "PX"마다 조정하여 진행하였지만 다른 웹사이트를 보면 테블릿, 휴대폰 등으로 나눠서 진행하는 것을보고 많이 부족하고 공부할 것이 많다는 것을 느꼈다.
  - 모든 팀원들이 대부분의 시간을 쏟아부어가며 만들어낸 페이지로 완성도는 처음 기획했던 것 그대로 기획이 된 것 같아서 최종 프로젝트에서 좋은 경험을 하고 교육을 끝마친 것 같다.
