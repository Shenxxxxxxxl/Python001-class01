
from django.db import models
class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    rating = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    comment_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'