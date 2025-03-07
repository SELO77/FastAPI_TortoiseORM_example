from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        table = "users"


class Todo(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    description = fields.TextField()
    is_completed = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
    user = fields.ForeignKeyField("models.User", related_name="todos")

    def __str__(self):
        return self.title

    class Meta:
        table = "todos"


class TodoComment(Model):
    id = fields.IntField(pk=True)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    # modified_at = fields.DatetimeField(auto_now=True)
    todo = fields.ForeignKeyField("models.Todo", related_name="comments")
    user = fields.ForeignKeyField("models.User", related_name="comments")

    def __str__(self):
        return self.content[:50]

    class Meta:
        table = "todo_comments"


class UserFollow(Model):
    id = fields.IntField(pk=True)
    follower = fields.ForeignKeyField("models.User", related_name="following")
    following = fields.ForeignKeyField("models.User", related_name="followers")

    class Meta:
        table = "user_follows"
