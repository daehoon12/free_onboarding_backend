# Code 구조  

- app.py : 서버와 데이터베이스 테이블을 생성.    
- auth.py : 회원가입, 로그인 등 사용자 인증을 위한 API를 구현.  
- crud.py : 게시판의 CRUD API를 구현 
- database.py : In-Memory Database 생성  
- test.py : 프로그램의 UnitTest  


# 유저 인증 기능

## 1. 회원 가입

### 구현 방법  
- Client에서 **POST** 방식으로 데이터 패킷에 id와 password를 보내면 password는 jwt 모듈을 이용해서 암호화하고 **회원을 관리하는 딕셔너리에 암호화한 패스워드를 value**로 두었다.

### 실행 방법  

- 아이디와 패스워드의 정보가 담긴 Request Message를 Endpoint에 보낸다.  
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
- Client에서 **POST** 방식으로 데이터 패킷에 id와 password를 보내면 서버는 **회원들의 정보가 들어있는 딕셔너리의 값과 일치하는지 확인**한다.

### 실행 방법  

- 아이디와 패스워드의 정보가 담긴 Request Message를 Endpoint에 보낸다.  
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


# CRUD  

## 1. CREATE

### 구현 방법  
- Client에서 **POST** 방식으로 데이터 패킷에 **id와 data**를 보내면 서버는 **id, 데이터, 생성한 날짜를 database에 저장**한다.  
- 원래는 id를 flask 모듈에서 지원하는 session에 넣어서 인증할 생각이었다. POSTMAN으로 메시지를 주고 받을 때는 잘 되는데 curl 명령어를 사용했을 때는 session 인증이 안되는 상황이 발생했다. stackoverflow에 쳐보니 curl은 병렬적이며 이전에 상태를 기억하지 않고 보낸다고 써있어 쿠키를 사용하라고 써있었는데 하다가 잘 안되서 메모리 내의 유저 정보와 매칭시켜 인증하는 방식으로 구현했다.  

## 실행 방법  
- id와 data의 정보가 담긴 Request Message를 Endpoint에 보낸다.  
<br/>  

Endpoint : [POST] http://127.0.0.1:5000/posts  
curl -X POST -H "content-type: application/json" http://127.0.0.1:5000/posts -d '{"id" : "Daehoon", "data": "study"}'  

### Request

#### 1. Header  
{    
　　"Content-Type: application/json"  
}    

#### 2. Body  
{  
　　"id" : "Daehoon",  
　　"data": "study"  
}  

### Response

#### 1. 200 OK
{  
　　"id": "Daehoon",  
　　"post_no": 1,  
　　"data": "study",  
　　"created_date": "21-10-27 14:01:55",  
　　"modified_date": "21-10-27 14:01:55"  
}  

#### 2. 401 UNAUTHORIZED
{  
　　"message" : "A login is required"  
}   

- 로그인을 안하고 CREATE 요청을 할 때 발생  

## 2. READ

### 구현 방법  
- Client에서 **GET 방식으로 parameter에 limit와 offset**을 넣어서 보내면 서버는 그 값을 통해 db에 쿼리를 날려 데이터를 가져온다.  
- **1에서 offset을 더한 게시글 번호부터 limit까지 데이터를 가져온다.**  
- Pagination을 구현한 DB Query : **SELECT * FROM post_info LIMIT limit OFFSET offset**  


## 실행 방법  
- limit와 offset을 파라미터로 담은 Request Message를 Endpoint에 보낸다.  
<br/>  

Endpoint : [GET] http://127.0.0.1:5000/posts  
curl -X GET -H "content-type: application/json" http://127.0.0.1:5000/posts?limit=30&offset=0  

### Request

#### 1. Header  
{    
　　"Content-Type: application/json"  
}    

#### 2. parameters  
{  
　　"limit" : 30,    
　　"offset: 0  
}  

### Response

#### 1. 200 OK
{  
　　"count": 30,  
　　"data" : [  
  　　　　　　　　{  
　　　　　　　　　　　　"id": "Daehoon",  
　　　　　　　　　　　　"post_number": 1,  
　　　　　　　　　　　　"post": "study",  
　　　　　　　　　　　　"created_date": "21-10-27 14:01:55",  
　　　　　　　　　　　　"modified_date": "21-10-27 14:01:55"  
　　　　　　　　　},  
<br/>
  　　　　　　　　{  
　　　　　　　　　　　　"id": "Daehoon",  
　　　　　　　　　　　　"post_number": 2,  
　　　　　　　　　　　　"post": "hard!",  
　　　　　　　　　　　　"created_date": "21-10-27 14:36:55",  
　　　　　　　　　　　　"modified_date": "21-10-27 14:38:12"  
　　　　　　　　　},  
         <br/>
　　　　　　　　　...  
         
　　　　　　　]  
}  

- count : data 안에 있는 element의 수  
- data : 가져온 데이터 정보  
 


## 3. UPDATE

### 구현 방법  
- Client에서 **PUT** 방식으로 **데이터 패킷에 아이디, 수정할 데이터, 게시글 번호**를 보내면 서버는 **게시글 번호를 통해 db에서 게시자를 찾는다.** **게시자와 요청한 client의 아이디가 일치하면 게시글을 수정하고 일치하지 않으면 아이디가 일치하지 않는다는 Response를 클라이언트에 보낸다.**      
- 원래는 id를 flask 모듈에서 지원하는 session의 값과 비교하려했지만, curl 명령어를 사용했을 때는 session의 값이 사라지는 상황이 생겨 위와 같은 방법으로 진행하였다. 여담으로 POSTMAN으로 했을 때는 session 값이 사라지지 않아 원래 생각한 방식으로 잘 돌아갔다.

## 실행 방법  
- id, 수정한 data, 게시글 번호가 담긴 Request Message를 Endpoint에 보낸다.  

Endpoint : [PUT] http://127.0.0.1:5000/posts/post_number (단 post_number는 unsigned int형 정수)  
curl -X PUT -H "content-type: application/json" http://127.0.0.1:5000/posts/1 -d '{"id": "Daehoon","post_no": 1, "data": "studydsdadsadasdas"}'
### Request

#### 1. Header  
{    
　　"Content-Type: application/json"  
}    

#### 2. Body  
{  
　　"id": "Daehoon",  
　　"post_no": 1,  
　　"data": "studydsdadsadasdas"  
}  

### Response

#### 1. 200 OK
{  
　　"id": "Daehoon",  
　　"post_no": 1,  
　　"data": "studydsdadsadasdas",  
　　"created_date": "21-10-27 14:01:55",  
　　"modified_date": "21-10-27 14:27:09"  
}  

#### 2. 400 BAD REQUEST
{  
　　"message" : "Your ID does not match the author's ID."  
}   

- 게시자 아이디와 로그인한 아이디가 일치하지 않을 때 발생.    


## 4. DELETE  

### 구현 방법  
- Client에서 **DELETE** 방식으로 데이터 패킷에 **아이디, 게시글 번호**를 보내면 서버는 **게시글 번호를 통해 db에서 게시자를 찾는다.** **게시자와 요청한 client의 아이디가 일치하면 게시글을 삭제하고 일치하지 않으면 아이디가 일치하지 않는다는 Response를 클라이언트에 보낸다.**        
- 원래는 id를 비교하는 방법을 flask 모듈에서 지원하는 session의 값과 비교하려했지만, curl 명령어를 사용했을 때는 session의 값이 사라지는 상황이 생겨 위와 같은 방법으로 진행하였다. 여담으로 POSTMAN으로 했을 때는 session 값이 사라지지 않아 원래 생각한 방식으로 잘 돌아갔다.  

## 실행 방법  
- id, 게시글 번호가 담긴 Request Message를 Endpoint에 보낸다.  

Endpoint : [DELETE] http://127.0.0.1:5000/posts/post_number (단 post_number는 unsigned int형 정수)  
curl -X DELETE -H "content-type: application/json" http://127.0.0.1:5000/posts/1 -d '{"id": "Daehoon","post_no": 1}'  

### Request

#### 1. Header  
{    
　　"Content-Type: application/json"  
}    

#### 2. Body  
{  
　　"id": "Daehoon",  
　　"post_no": 1,  
}  

### Response

#### 1. 200 OK
{  
　　"delete": "success"  
}  

#### 2. 400 BAD REQUEST
{  
　　"message" : "Your ID does not match the author's ID."  
}   

- 게시자 아이디와 로그인한 아이디가 일치하지 않을 때 발생.    


# Test  
- 테스트는 Postman, curl 명령어, 파이썬 모듈인 unittest를 이용해 진행.  
- 
