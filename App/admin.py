from django.contrib import admin
from .models import PostModel, UserModel

admin.site.register(PostModel)
admin.site.register(UserModel)
