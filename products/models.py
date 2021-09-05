from django.db import models


class SkillCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Skill categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class EnvCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Env categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    skill_category = models.ForeignKey('SkillCategory', null=True, blank=True, on_delete=models.SET_NULL)
    env_category = models.ForeignKey('EnvCategory', null=True, blank=True, on_delete=models.SET_NULL)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
