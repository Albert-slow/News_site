from django.db import models


class CategoryModel(models.Model):
    category_title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_title

    class Meta:
        verbose_name = 'News category'
        verbose_name_plural = 'News categories'


class TagModel(models.Model):
    tag_title = models.CharField(max_length=30, help_text='Тут добавьте Тэг')

    def __str__(self):
        return self.tag_title

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class ArticleModel(models.Model):
    article_title = models.CharField(max_length=100, help_text='Тут добавьте название статьи')
    article_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    article_tag = models.ForeignKey(TagModel, on_delete=models.CASCADE)
    article_news = models.TextField()
    article_image = models.FileField(upload_to='news_images')
    article_author = models.CharField(max_length=50, help_text='ФИО автора')
    article_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name = 'News article'
        verbose_name_plural = 'News articles'


