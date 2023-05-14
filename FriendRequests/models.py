from django.db import models
from base.models import SMUser
import uuid

# Create your models here.
#https://docs.djangoproject.com/en/4.2/howto/writing-migrations/#migrations-that-add-unique-fields
class AllRequests(models.Model):
    request_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    from_user=models.ForeignKey(SMUser, related_name='sender_user', on_delete=models.CASCADE)
    to_user=models.ForeignKey(SMUser, related_name='receiver_user', on_delete=models.CASCADE)
    pending=models.BooleanField(default=True) #'True','False'
    status=models.CharField(max_length=8,default="Pending") #'Accept', 'Reject','Pending'
    class Meta:
        unique_together=['from_user','to_user']