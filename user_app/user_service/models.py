import uuid
from django.db import models

class User(models.Model):
    REGULAR = 'regular'
    VIP = 'vip'
    WHOLESALE = 'wholesale'
    
    USER_TYPES = [
        (REGULAR, 'Regular'),
        (VIP, 'VIP'),
        (WHOLESALE, 'Wholesale'),
    ]
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(choices=USER_TYPES, default='reguler', max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)