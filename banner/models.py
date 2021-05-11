from django.conf import settings
from django.db import models



class Banner(models.Model):
    id = models.AutoField(primary_key=True)
    banner_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200,null=True)
    url = models.URLField(max_length=100)
    image = models.ImageField(upload_to='uploads/banners')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING,related_name='BannerCreatedBy',blank=True,null=True)
    created_date=models.DateField(auto_now_add=True)
    modify_by=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING,related_name='BannerModifyBy',blank=True,null=True)
    status = models.BooleanField(default=False)


    class Meta:
        db_table = 'banners'
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __str__(self):
        return self.banner_name
