from ninja import Schema

class LoginIn(Schema):
    username: str
    password: str