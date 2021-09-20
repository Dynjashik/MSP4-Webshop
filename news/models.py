from django.db import models


class News(models.Model):
    class Meta:
        verbose_name_plural = 'News'

    title = models.CharField(max_length=254)
    description = models.TextField()
    date_added = models.DateTimeField(null=False, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
