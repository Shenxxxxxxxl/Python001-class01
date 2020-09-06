from django.db import models


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    pagetitle = models.CharField(max_length=500, blank=True, null=True)
    tab = models.CharField(max_length=255, blank=True, null=True)
    mall = models.CharField(max_length=255, blank=True, null=True)
    channel = models.CharField(max_length=255, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=500, blank=True, null=True)
    release_time = models.DateTimeField(blank=True, null=True)
    pos_count = models.BigIntegerField(blank=True, null=True)
    neg_count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class ProductComment(models.Model):
    id = models.IntegerField(primary_key=True)
    product_id = models.IntegerField(blank=True, null=True)
    usmzdmid = models.IntegerField(blank=True, null=True)
    comment_time = models.DateTimeField(blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    support = models.BigIntegerField(blank=True, null=True)
    oppose = models.BigIntegerField(blank=True, null=True)
    is_pos = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_comment'
