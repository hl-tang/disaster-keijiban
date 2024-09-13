from ninja import Schema, ModelSchema
from .models import Disaster, Post

class PostIn(Schema):
    title: str
    content: str
    disaster_id: int
    user_name: str

class PostOut(Schema):
    id: int
    title: str
    content: str
    user_name: str

    # class Meta:
    #     model = Disaster
    #     fields = "__all__"

class DisasterIn(Schema):
    disaster_name: str
    allow_areas: list

class DisasterOut(ModelSchema):
    class Meta:
        model = Disaster
        fields = "__all__"