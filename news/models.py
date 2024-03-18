from django.db import models


class CategoryModel(models.Model):
    category_title = models.CharField("Категория", max_length=30, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_title

    class Meta:
        verbose_name = 'Article category'
        verbose_name_plural = 'Article categories'


class TagModel(models.Model):
    tag_title = models.CharField("Тэг", max_length=30, help_text='Тут добавьте Тэг')

    def __str__(self):
        return self.tag_title

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class ArticleModel(models.Model):
    article_title = models.CharField("Название статьи", max_length=100, help_text='Тут добавьте название статьи')
    article_categories = models.ForeignKey(CategoryModel, verbose_name="Article categories",
                                           on_delete=models.CASCADE, null=True)
    article_tags = models.ManyToManyField(TagModel, verbose_name="Tag", default='')
    article_news = models.TextField("Статья")
    article_image = models.FileField("Изображение", upload_to='article_images')
    article_author = models.CharField("Автор", max_length=50, help_text='ФИО автора')
    article_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name = 'News article'
        verbose_name_plural = 'News articles'


