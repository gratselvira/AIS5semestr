from django.db import models
from django.contrib.auth.models import User

# определения моделей данных проекта. Модели представляют собой структуру данных, которые будут храниться в базе данных.

class Advantage(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Владелец статьи', blank = True, null = True )
    create_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Достижение'
        verbose_name_plural='Статьи'

class Comments(models.Model):
    article = models.ForeignKey(Advantage, on_delete = models.CASCADE, verbose_name='Достижение', blank = True, null = True,related_name='comments_articles' )
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Автор комментария', blank = True, null = True )
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name='Текст комментария')
    status = models.BooleanField(verbose_name='Видимость статьи', default=False)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    article = models.ForeignKey(Advantage, on_delete=models.CASCADE, verbose_name='Статья')

    class Meta:
        unique_together = ('user', 'article')  # Один пользователь может лайкнуть статью только один раз

    def __str__(self):
        return f"{self.user.username} likes {self.article.name}"
