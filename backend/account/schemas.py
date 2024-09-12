from ninja import Schema

class RegisterIn(Schema):
    username: str
    password: str