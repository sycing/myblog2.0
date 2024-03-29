from django.db import models

# Create your models here.


class Resource(models.Model):
    fileName=models.CharField('名称',max_length=128)
    fileSize=models.IntegerField('大小')
    fileCreateDate=models.DateTimeField('创建时间',db_column='buildTime',auto_now_add=True)
    headImg = models.FileField(upload_to='./upload/')
    def __unicode__(self):
        return self.fileName

    class Meta:
        verbose_name = '资源'
        verbose_name_plural = verbose_name
