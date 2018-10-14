from django.db import models


class HeroInfoManager(models.Manager):
    def get_queryset(self):
        return super(HeroInfoManager, self).get_queryset().filter()

    def create_hero(self, hname=None, hgender=1, isdelete=False):
        hero_info = HeroInfo()
        hero_info.hname = hname
        hero_info.hgender = hgender
        hero_info.isDelete = isdelete
        return hero_info


class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = "hero_info"
    hero_manager = HeroInfoManager()

