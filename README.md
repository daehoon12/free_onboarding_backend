# 프리온보딩 백엔드 코스 과제

- 구현한 방법과 이유에 대한 간략한 내용
- 자세한 실행 방법(endpoint 호출방법)
- api 명세(request/response 서술 필요)

# 유저 인증 기능

## 1. 회원 가입

### Endpoint : [POST] http://127.0.0.1:5000/auth/register  
### curl 명령어 예시 : curl -X POST -H "Content-Type: application/json" http://127.0.0.1:5000/auth/register -d '{ "name" : "Daehoon","password" : "pass"}'  

- Client에서 POST 방식으로 데이터 패킷에 id와 password를 보내면 password는 jwt 모듈을 이용해서 암호화하고 id들을 관리하는 딕셔너리에 암호화한 패스워드를 value로 두었다.

