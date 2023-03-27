# Impeachment - Back-end - API Rest

# 📖 Documentation

- [About](#-about)
- [Project status](#-project-status)
- [Technologies](#-technologies)
- [How to use](#-how-to-use)
- [Testing application](#-testing-application)
- [Host of API](#-host-of-api)
- [REST API](#-rest-api)
- [Features](#-features)

---

## 🔖 About

Software designed to manage financial.

---

## 📖 Project status

Django project development

---

## 🚀 Technologies

the project was developer with the technologies:

- [Ubuntu](https://ubuntu.com/)
- [Windows](https://www.microsoft.com/pt-br/windows/)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Docker](https://www.docker.com/)
- [AWS](https://aws.amazon.com/pt/)

---

## 🗂 How to use

## 🐳 Development enviroment

```
docker build -t impeachment-workservice -f Dockerfile.dev .
```

```
docker run -d --env-file .env -p 6006:6006 impeachment-workservice 
```

Run in browser of your choice, for verify active service

```
http://localhost:6006/
```

# 📑 Note

-- Enviroment developer is created username "admin" and passsword "admin"

Inform your credentials

Run in browser of your choice, for verify active service

---

## 🔨 Testing application

When being at the root of the project, if necessary, we can perform tests with the following command.

```
pytest -v --ds=<INFO_WSGI>
```

---

# ➿ REST API

The REST API to the example app is described below.

## Get token of authentication

Exclusive router for login. Return token for validation in routers

### Request

`GET http://auth-dev.camposdevelopers.com.br/api/v1/authenticate/login`

    curl --header "Content-Type: application/json" --request POST --data "{\"username\": \"admin\", \"password\": \"admin\" }" http://auth-dev.camposdevelopers.com.br/api/v1/authenticate/login

### Response

    {"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYwMTMyNDk1OCwianRpIjoiYzI5NzJhMDJiMjgyNDExNWI2OWE3MTU1N2JlMDQyNzEiLCJ1c2VyX2lkIjoxfQ.xvYJ-RbITZiBUTaKKPjrAzvUlG0QpdsgRWbS7R7v51U","access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAxMjM4ODU4LCJqdGkiOiI1NDhiM2Y4M2IxYjk0M2FmYWI5NzczZWI0OTk1MmQ5NiIsInVzZXJfaWQiOjF9.l_aEk0QiOY9fOzyn_8Ji_zP1SwIB4QMfi3CT3IgIzqg"}

The routers of CRUD, is necessary send token of autentication in headers. Token type "Bearer"

## Get list of Impeachment

### Request

`GET api/v1/impeachments/list`

curl --header "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAxMjM5Nzc5LCJqdGkiOiJjYmU4NTAwMDZmMTg0NjkzODdiMWIyYmVkZTNkODg3MSIsInVzZXJfaWQiOjF9.McY2lLiorIK3SVNtEGKN9rQFtOm_xP7EVVXVcXAR110" --request GET http://localhost:6006/api/v1/impeachments/list

### Response

"id": 1,
"company_id": 12,
"name_impeachment": "teste1",
"description_impeachment": "testando"
...

## Create a new Impeachment

### Request

`POST api/v1/impeachments/create`

curl --header "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAxMjQwOTAxLCJqdGkiOiI4MjJkNDc5NDRmZmU0Yzc3OTE1MTA4ODAwNzQzOGJjMSIsInVzZXJfaWQiOjF9.KXZcekm0kLOQEN4nqsJQ-LMfF5PWbs6g_9BV4CiEiO8" --header "Content-Type: application/json" --request POST --data " http://localhost:6006/api/v1/impeachments/create

### Response

"id": 1,
"company_id": 12,
"name_impeachment": "teste1",
"description_impeachment": "testando"
...

## Get a specific Impeachment

### Request

`GET 'api/v1/impeachments/<int:pk>/retrieve`

curl --header "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAxMjQxODU0LCJqdGkiOiJkYjA0ZDcyZWFiMWU0NzBhYTA2NWRmYzVkODhhMWM0ZiIsInVzZXJfaWQiOjF9.DsXceg-MxMWAO0X7IcjHt_6VkDiif2qwFCMIJPZt758" --header "Content-Type: application/json" --request GET http://localhost:6006/api/v1/impeachments/<int:pk>/retrieve

### Response

"id": 1,
"company_id": 12,
"name_impeachment": "teste1",
"description_impeachment": "testando"
...

## Get a non-existent Impeachment

### Request

`GET 'api/v1/impeachments/<int:pk>/request`

curl --header "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAxMjQxODU0LCJqdGkiOiJkYjA0ZDcyZWFiMWU0NzBhYTA2NWRmYzVkODhhMWM0ZiIsInVzZXJfaWQiOjF9.DsXceg-MxMWAO0X7IcjHt_6VkDiif2qwFCMIJPZt758" --header "Content-Type: application/json" --request GET http://localhost:6006/api/v1/request

### Response

{
    API:OK
}

## Get changed impeachment

### Request

`PUT api/v1/impeachments/<int:pk>/update`

curl --header "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAxMjQzMzA3LCJqdGkiOiJmOTMxYzUxZWI1NjQ0NTZjYjJjZjU4MzNhYzQ1MzE2MyIsInVzZXJfaWQiOjF9.IJBCt0lpgvK2bI7XdKlG51D8jVONhT0ASzHZt6jQL-0" --header  http://localhost:6006/api/v1/impeachments/<int:pk>/update

### Response

"id": 1,
"company_id": 12,
"name_impeachment": "teste2",
"description_impeachment": "testando"
...

## Delete a impeachment

### Request

`DELETE api/v1/impeachments/<int:pk>/destroy`

curl --header "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAxMjQyNjQ1LCJqdGkiOiJiOWEzMTJiN2I3YmE0YWVhOTM3MzFkM2NiZDY2NzY2OCIsInVzZXJfaWQiOjF9.vUEDhJuU7xNPgPJayS_nAb-mpkxAQSCAhzK49yNzANI" --header "Content-Type: application/json" --request DELETE http://localhost:6006/api/v1/impeachments/<int:pk>/destroy

### Response

[]

---

# 📰 Features

- [x] impeachment Register
- [x] Documentation all