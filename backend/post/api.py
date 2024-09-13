from ninja import Router
from .models import Post, Disaster
from .schemas import PostIn, PostOut, DisasterIn, DisasterOut
from django.http import HttpRequest, HttpResponse, JsonResponse
from .try_uuid import get_random_str
import os
from django.conf import settings
from django.db.models import Q

post_api = Router()

@post_api.post("/disaster_create/", response=DisasterOut)
def disaster_create(request, payload: DisasterIn):
    disaster = Disaster.objects.create(
        disaster_name = payload.disaster_name,
        allow_areas = payload.allow_areas
    )
    return disaster

@post_api.get("/disasters/", response=list[DisasterOut])
def list_posts(request):
    return Disaster.objects.all().order_by('-id')

@post_api.post("/post_create/")
def post_create(request, payload: PostIn):
    # 未登录不可
    # 前端判定 alert

    # 限制IP
    # 前端判定 alert

    post = Post.objects.create(
        title = payload.title,
        content = payload.content,
        disaster_id = payload.disaster_id,
        user_name = payload.user_name
    )
    return {"msg": "post success"}

@post_api.get("/posts/", response=list[PostOut])
def list_posts(request, disaster_id):
    # return Post.objects.all().order_by('-id')
    return Post.objects.filter(disaster_id=disaster_id).order_by('-id')

@post_api.get("/post_search/", response=list[PostOut])
def post_search_string(request, disaster_id, keyword):
    # return Post.objects.get(content__contains=keyword) # 只返回一个对象
    # return Post.objects.filter(content__icontains=keyword).order_by('-last_date')
    return Post.objects.filter( Q(disaster_id=disaster_id) & (Q(content__icontains=keyword) | Q(title__icontains=keyword))).order_by('-last_date')

@post_api.get("/post_search_tag/", response=list[PostOut])
def post_search_tag(request, tag):
    pass


@post_api.post("receive_img")
def receive_img(request):
    rev_file = request.FILES.get('image')
    if not rev_file:
        return JsonResponse({"code": 0, "msg": "no img exists"})
    new_name = get_random_str()
    extension = os.path.splitext(rev_file)[1]
    file_path = os.path.join(settings.MEDIA_ROOT, new_name + extension)
    try:
        f = open(file_path, 'wb')
        for i in rev_file.chunks():
            f.write(i)
        f.close()
        return JsonResponse({'code': 1, 'name': new_name + extension})
    except Exception as e:
        return JsonResponse({'code':0, 'msg':str(e)})

