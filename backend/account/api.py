from ninja import Router
from .models import User
from .schemas import RegisterIn
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout

account_api = Router()

@account_api.post("/register/")
def auth_register(request, payload: RegisterIn):
    if User.objects.filter(username=payload.username).exists():
        return {"msg": "Username already exists"}
    user = User.objects.create_user(
        username=payload.username, password=payload.password)
    return {"msg": "User created successfully", "username": user.username, "pwd": user.password}

@account_api.get("/logout/")
def auth_logout(request, response: HttpResponse):
    logout(request)
    response.delete_cookie('userid')
    response.delete_cookie('username')
    return {"msg": "Logged out successfully"}