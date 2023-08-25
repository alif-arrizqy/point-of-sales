import uuid
from django.db import models

class Item(models.Model):
    HAT = 'hats'
    TOP = 'tops'
    SHORTS = 'shorts'
    
    ITEM_TYPES = [
        (HAT, 'Hat'),
        (TOP, 'Top'),
        (SHORTS, 'Shorts'),
    ]
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=20, choices=ITEM_TYPES)
    regular_price = models.IntegerField()
    vip_price = models.IntegerField()
    wholesale_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
