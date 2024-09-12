from ninja import Router
from account.models import User
from .schemas import LoginIn

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout

login_api = Router()

@login_api.post("/login/")
def auth_login(request: HttpRequest, response: HttpResponse, payload: LoginIn):
    user = authenticate(request, username=payload.username, password=payload.password)
    print(user)
    print(type(user))
    if user is not None:
        login(request, user)
        response.set_cookie("userid", user.id)
        response.set_cookie("username", user.username)
        if user.is_admin == False:
            return {"msg": "Login successful", "username": user.username, "code": 0}
        else:
            return {"msg": "Login successful", "username": user.username, "code": 1}
    else:
        return {"msg": "Invalid credentials"}