from django.db import models


class News(models.Model):
    class Meta:
        verbose_name_plural = 'News'

    title = models.CharField(max_length=254, null=False, blank=False)
    description = models.TextField()
    date_added = models.DateTimeField(null=True, auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
