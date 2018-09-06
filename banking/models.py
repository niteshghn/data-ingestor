from django.db import models


# Create your models here.

class Transaction(models.Model):
    source_service = models.CharField(max_length=30, db_index=True)
    type = models.CharField(max_length=40, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user_email = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=40)
    amount = models.IntegerField(default=0)
    action = models.CharField(max_length=20, db_index=True)
    modified_at = models.DateTimeField(auto_now=True)
    increment_id = models.IntegerField(db_index=True)
    