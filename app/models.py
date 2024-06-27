from django.db import models

# Create your models here.

table_prefix = "app_"


class User(models.Model):
    uuid = models.CharField(max_length=300, db_comment="uuid")
    name = models.CharField(max_length=300, db_comment="用户名")
    create_datetime = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        db_comment="创建时间",
    )

    class Meta:
        indexes = [
            models.Index(fields=["uuid"])
            ]
        db_table = table_prefix + "user"
        db_table_comment = "用户表"
