# Endpoints

## 1. /auth (POST)
This endpoint is used for creating a user

### Request
**Method:** POST

**Path:** /auth

## 2. /user_by_id/{userid} (GET)
This endpoint is used to get the used with used id

### Request
**Method**: GET

**Path**: /user_by_id/{userid}

### Response example

```bash
{
  "id": 1,
  "username": "vichu",
  "phone": "8546629577",
  "hashed_password": "$2b$12$6qW1MuPM/CNm3n9S3wwqFOiTgR87QGkiGAFqJt8DeK60fNUKAestC",
  "email": "user@example.com",
  "name": "string"
}
```

## 3. /token
This endpoint authenticates a user and returns an access token

### Request
Method: POST

Path: /token

### Response example

```bash
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ2aWNodSIsImlkIjoxLCJleHAiOjE3MjIyNTQwNjZ9.sJUeRFAo2izk6_UGRbae_OrqVhwqEOfk2JnK3ExzrZo",
  "token": "bearer"
}
```





