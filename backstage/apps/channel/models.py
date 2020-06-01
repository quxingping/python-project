from django.db import models

# Create your models here.

"""
Channel 所有频道
Yangshi 央视频道
Weishi 卫视频道
"""


class Channel(models.Model):
    name = models.CharField(max_length=50,verbose_name="频道")
    bianmaqi = models.CharField(max_length=50,blank=True,null=True,verbose_name="编码器")
    jieru = models.CharField(max_length=50,blank=True,null=True,verbose_name="sdi/ip")
    type = models.CharField(max_length=50,verbose_name="类型")
    pindao_id =  models.CharField(max_length=50,blank=True,null=True,verbose_name="频道ID")
    beizhu = models.CharField(max_length=50, blank=True, null=True, verbose_name="beizhu")

    class Meta:
        verbose_name = '所有频道'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name


class Yangshi(models.Model):
    name = models.CharField(max_length=50,verbose_name="频道")
    bianmaqi = models.CharField(max_length=50,blank=True,null=True,verbose_name="编码器")
    jieru = models.CharField(max_length=50,blank=True,null=True,verbose_name="sdi/ip")
    pindao_id = models.CharField(max_length=50, blank=True, null=True, verbose_name="频道ID")
    beizhu = models.CharField(max_length=50, blank=True, null=True, verbose_name="beizhu")

    class Meta:
        verbose_name = '央视频道'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name


class Weishi(models.Model):
    name = models.CharField(max_length=50,verbose_name="频道")
    bianmaqi = models.CharField(max_length=50,blank=True,null=True,verbose_name="编码器")
    jieru = models.CharField(max_length=50,blank=True,null=True,verbose_name="sdi/ip")
    pindao_id = models.CharField(max_length=50, blank=True, null=True, verbose_name="频道ID")
    beizhu = models.CharField(max_length=50, blank=True, null=True, verbose_name="beizhu")

    class Meta:
        verbose_name = '地方卫视频道'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name

class Jiaoyu(models.Model):
    name = models.CharField(max_length=50,verbose_name="频道")
    bianmaqi = models.CharField(max_length=50,blank=True,null=True,verbose_name="编码器")
    jieru = models.CharField(max_length=50,blank=True,null=True,verbose_name="sdi/ip")
    pindao_id = models.CharField(max_length=50, blank=True, null=True, verbose_name="频道ID")
    beizhu = models.CharField(max_length=50, blank=True, null=True, verbose_name="beizhu")

    class Meta:
        verbose_name = '教育频道'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name


class Qita(models.Model):
    name = models.CharField(max_length=50,verbose_name="频道")
    bianmaqi = models.CharField(max_length=50,blank=True,null=True,verbose_name="编码器")
    jieru = models.CharField(max_length=50,blank=True,null=True,verbose_name="sdi/ip")
    pindao_id = models.CharField(max_length=50, blank=True, null=True, verbose_name="频道ID")
    beizhu = models.CharField(max_length=50, blank=True, null=True, verbose_name="beizhu")

    class Meta:
        verbose_name = '其它频道'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name


class Server(models.Model):
    ip =  models.CharField(max_length=50,verbose_name="源站地址")
    jifang = models.CharField(max_length=50,verbose_name="所在机房")
    type = models.CharField(max_length=50,verbose_name="源站服务类型")
    jiankong = models.CharField(max_length=50,verbose_name="后台监控地址")


    class Meta:
        verbose_name = '源站信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ip
