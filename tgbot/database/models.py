from tortoise import fields, models


class User(models.Model):
    id = fields.BigIntField(pk=True)
    name = fields.CharField(max_length=32)
    is_banned = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "users"

class MessageRelations(models.Model):
    message_id = fields.BigIntField(pk=True)
    user_id = fields.BigIntField()

    class Meta:
        table = "message_relations"
