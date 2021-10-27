# 프리온보딩 백엔드 코스 과제

- 구현한 방법과 이유에 대한 간략한 내용
- 자세한 실행 방법(endpoint 호출방법)
- api 명세(request/response 서술 필요)

# 유저 인증 기능

## 1. 회원 가입

### 구현 방법  
- Client에서 POST 방식으로 데이터 패킷에 id와 password를 보내면 password는 jwt 모듈을 이용해서 암호화하고 회원을 관리하는 딕셔너리에 암호화한 패스워드를 value로 두었다.

### 실행 방법  

- 아이디와 패스워드의 정보가 담긴 json data를 담아서 Endpoint에 보낸다.  
<br/>  

Endpoint : [POST] http://127.0.0.1:5000/auth/register  
curl 명령어 예시 : curl -X POST -H "Content-Type: application/json" http://127.0.0.1:5000/auth/register -d '{ "id" : "Daehoon","password" : "pass"}'  


### Request

#### 1. Header  
{    
　　"Content-Type: application/json"  
}    

#### 2. Body  
{  
　　"id" : "Daehoon",  
　　"password : "pass"  
}  

### Response

#### 1. 200 OK
{  
　　"Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoiRGFlaG9vbiJ9.kVfdmcIH0xlLRUvL2DF5Q93DTfMjNqwbg4x7ppd-Mvc"  
}  

#### 2. 500 INTERNAL SERVER ERROR
{  
　　"message": "Register Failed"  
}   


## 2. 로그인

### 구현 방법  
- Client에서 POST 방식으로 데이터 패킷에 id와 password를 보내면 서버는 회원들의 정보가 들어있는 딕셔너리의 값과 일치하는지 확인한다.

### 실행 방법  

- 아이디와 패스워드의 정보가 담긴 json data를 담아서 Endpoint에 보낸다.  
<br/>  

Endpoint : [POST] http://127.0.0.1:5000/auth/login  
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:5000/auth/login -d '{ "name" : "Daehoon","password" : "pass"}'

### Request

#### 1. Header  
{    
　　"Content-Type: application/json"  
}    

#### 2. Body  
{  
　　"id" : "Daehoon",  
　　"password : "pass"  
}  

### Response

#### 1. 200 OK
{  
　　"Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoiRGFlaG9vbiJ9.kVfdmcIH0xlLRUvL2DF5Q93DTfMjNqwbg4x7ppd-Mvc"  
}  

#### 2. 404 NOT FOUND
{  
　　"message": "User Not Found"  
}   

- 회원가입이 안되어 있을 때 발생  

#### 3. 500 INTERNAL SERVER ERROR

{  
　　"message": "Auth Failed"  
}  

- 패스워드가 틀렸을 때 발생  


## 3. CREATE

### 구현 방법  
- Client에서 POST 방식으로 데이터 패킷에 id와 data를 보내면 서버는 id, 데이터, 생성한 날짜를 database에 저장한다.  
- 원래는 id를 flask 모듈에서 지원하는 session에 넣어서 인증할 생각이었다. POSTMAN으로 메시지를 주고 받을 때는 잘 되는데 curl 명령어를 사용했을 때는 session 인증이 안되는 상황이 발생했다. stackoverflow에 쳐보니 curl은 병렬적이며 이전에 상태를 기억하지 않고 보낸다고 써있어 쿠키를 사용하라고 써있었는데 하다가 잘 안되서 메모리 내의 유저 정보와 매칭시켜 인증하는 방식으로 구현했다.  

## 실행 방법  
- id와 data의 정보가 담긴 json data를 담아서 Endpoint에 보낸다.  
<br/>  

Endpoint : [POST] http://127.0.0.1:5000/posts/  
curl -X POST -H "content-type: application/json" http://127.0.0.1:5000/posts -d '{"id" : "Daehoon", "data": "study"}'  

### Request

#### 1. Header  
{    
　　"Content-Type: application/json"  
}    

#### 2. Body  
{  
　　"id" : "Daehoon",  
　　"password : "pass"  
}  

### Response

#### 1. 200 OK
{  
　　"Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoiRGFlaG9vbiJ9.kVfdmcIH0xlLRUvL2DF5Q93DTfMjNqwbg4x7ppd-Mvc"  
}  

#### 2. 404 NOT FOUND
{  
　　"message": "User Not Found"  
}   

- 회원가입이 안되어 있을 때 발생  

#### 3. 500 INTERNAL SERVER ERROR

{  
　　"message": "Auth Failed"  
}  

- 패스워드가 틀렸을 때 발생  

