from django.db import models
from django_summernote.fields import SummernoteTextField
# import bleach
from django.utils import timezone
from django.core.validators import FileExtensionValidator

# Create your models here.

class document(models.Model):
  title = models.CharField(max_length=140)
  content = models.CharField(max_length=500, blank=True, default="Image link here")
  # content = SummernoteTextField(blank=True, default="Image link here")
  image = models.ImageField(default="image.png", blank=True,
            validators= [FileExtensionValidator(allowed_extensions= ['gif', 'jpg', 'jpeg', 'png', 'svg'])])

  date = models.DateField(auto_now_add=True)
  datetime = models.DateTimeField(default=timezone.now)

  # def save(self, *args, **kwargs):
  #     allowed_tags = ['svg', 'path', 'div', 'span']  # Add more tags as needed
  #     allowed_attrs = {'*': ['class', 'fill', 'd', 'width', 'height', 'viewBox', 'xmlns']}
  #     self.content = bleach.clean(self.content, tags=allowed_tags, attributes=allowed_attrs)
  #     super().save(*args, **kwargs)

  def __str__(self):
    return self.title
  
class doc(models.Model):
  document = models.ForeignKey(document, on_delete=models.CASCADE, related_name='docs')

  title = models.CharField(max_length=140)
  content = models.TextField(blank=True)
  # content = SummernoteTextField()
  code = models.TextField(blank=True)
  image = models.ImageField(default='image.png', blank=True,
            validators= [FileExtensionValidator(allowed_extensions= ['gif', 'jpg', 'jpeg', 'png', 'svg'])])

  date = models.DateField(auto_now_add=True)
  datetime= models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.title
  
class key(models.Model):
  Key = models.CharField(max_length=100)

  def __str__(self):
    return f'Key:- {self.pk}'