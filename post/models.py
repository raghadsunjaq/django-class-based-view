from django.db import models
from django.utils import timezone
# Create your models here.
class poost(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField(max_length=1000)
    created_at=models.DateTimeField(default=timezone.now)
    
    #image=models.ImageField(upload_to='poost-img/')
 
    class Meta:
        verbose_name = ("poost")
        verbose_name_plural = ("poosts")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("poost_detail", kwargs={"pk": self.pk})

