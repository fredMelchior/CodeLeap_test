from django.db import models


class UserModel(models.Model):
    """
    Custom user model -> 'username':'string'
    """

    username = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.username


class PostModel(models.Model):
    """
    Application post model: - 'id':'number', - 'username':'string',
    - 'created_datetime:'datetime', - 'title':'string', - 'content':'string'
    """

    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=700)

    def __str__(self):
        return self.title
