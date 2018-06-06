
# RESTFul Authentication Documentation

## 1. Registration
Description: Registering the user to the system:

| URL        | URI/api/v1/myauth/logout/|
| ------------- |---------------| 
| Method      | POST |
| Parameters      | username, password, email,first_name, last_name      |

### Sample Request:
curl -X POST \
  http://localhost:8000/api/v1/myauth/register/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
        "username": "abir",
        "password": "adfa", \
        "email": "abir@a.com", 
        "first_name": "Abir",\
        "last_name": "Ahmed"
    }'

## 2. Login
Description: User Login to the system

| URL        | URI/api/v1/myauth/login/|
| ------------- |---------------| 
| Method      | POST |
| Parameters      | username, password|

### Sample Request

curl -X POST \
  http://localhost:8000/api/v1/myauth/login/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
	"username":"ruhshan",
	"password":"test1234"
}'

## 3. Logout:
Description: Loggin Out a user from system
| URL        | URI/api/v1/myauth/logout/|
| ------------- |---------------| 
| Method      | POST |
|Authorization| JWT "token" |
| Parameters      | username|

### Sample Request:

curl -X POST \
  http://localhost:8000/api/v1/myauth/logout/ \
  -H 'authorization: JWT "token" \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
    "user":"ruhshan"
}'
