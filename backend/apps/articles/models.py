from django.db import models
# from apps.core.models import TimeStampedModel



class Article(models.Model):
  # author = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  content = models.TextField()
  # image = models.ImageField(upload_to='images/')
  # bookmark = models.ForeignKey(Bookmark, on_delete=models.CASCADE)
  # comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
  #TODO: Use TimeStampedModel
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  deleted_at = models.DateTimeField(null=True, blank=True)
  
  class Meta:
    verbose_name = 'article'
    verbose_name_plural = 'articles'

  def __str__(self):
    return self.title