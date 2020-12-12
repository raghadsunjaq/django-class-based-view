from django.db import models
from django.utils import timezone
# Create your models here.
class poost(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField(max_length=1000)
    created_at=models.DateTimeField(default=timezone.now)

    image=models.ImageField(upload_to='post/' ,default=None)
    active=models.BooleanField(default=False)
 
    class Meta:
        verbose_name = ("poost")
        verbose_name_plural = ("poosts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("poost_detail", kwargs={"pk": self.pk})

