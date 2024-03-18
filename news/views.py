from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound

from .forms import NewsForm
from news.models import ArticleModel, CategoryModel, TagModel
# from haystack.query import SearchQuerySet
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


# получение данных из бд
def home_page(request):
    categories = CategoryModel.objects.all()
    articles = ArticleModel.objects.all()
    context = {"categories": categories, "articles": articles}
    return render(request, template_name="index.html", context=context)


class SearchResultsView(ListView):
    model = ArticleModel
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        article_list = ArticleModel.objects.filter(
            Q(article_title__icontains=query)
        )
        return article_list
    # def search(request):
    #     query = request.GET['q']
    #     article_list = ArticleModel.objects.filter(article_title__iregex=query)
    #     return render(request, 'search.html', {'article_list': article_list})


class NewsListView(ListView):
    model = ArticleModel
    template_name = 'articles_list.html'
    context_object_name = 'articles'


class NewsDetailView(DetailView):
    model = ArticleModel
    template_name = 'article.html'
    context_object_name = 'article'


class NewsCreateView(CreateView):
    model = ArticleModel
    form_class = NewsForm
    template_name = 'create.html'
    success_url = reverse_lazy('articles_list')


class NewsUpdateView(UpdateView):
    model = ArticleModel
    form_class = NewsForm
    template_name = 'edit.html'
    success_url = reverse_lazy('articles_list')


class NewsDeleteView(DeleteView):
    model = ArticleModel
    template_name = 'delete.html'
    success_url = reverse_lazy('articles_list')


# сохранение данных в бд
# def create(request):
#     article = ArticleModel.objects.all()
#     if request.method == "POST":
#         article.article_title = request.POST.get("article_title")
#         CategoryModel.article_category = request.POST.get("article_category")
#         TagModel.article_tag = request.POST.get("article_tag")
#         article.article_news = request.POST.get("article_news")
#         article.article_image = request.POST.get("article_image")
#         article.article_author = request.POST.get("article_author")
#         article.save()
#         return HttpResponseRedirect("/")
#     else:
#         return render(request, "create.html", {"article": article})


# def create_news(request):
#     if request.method == 'POST':
#         formset = NewsForm(request.POST)
#     else:
#         formset = NewsForm()
#     context = {
#         'formset': formset
#     }
#     return render(request, 'create.html', context)
#
#
# изменение данных в бд
# def edit(request, pk):
#     try:
#         article = ArticleModel.objects.get(pk=pk)
#
#         if request.method == "POST":
#             article.article_title = request.POST.get("article_title")
#             CategoryModel.article_category = request.POST.get("article_category")
#             TagModel.article_tag = request.POST.get("article_tag")
#             article.article_news = request.POST.get("article_news")
#             article.article_image = request.POST.get("article_image")
#             article.article_author = request.POST.get("article_author")
#             article.save()
#             return HttpResponseRedirect("/")
#         else:
#             return render(request, "edit.html", {"article": article})
#     except ArticleModel.DoesNotExist:
#         return HttpResponseNotFound("<h2>Article not found</h2>")
#
#
# # удаление данных из бд
# def delete(request, id):
#     try:
#         article = ArticleModel.objects.get(id=id)
#         article.delete()
#         return HttpResponseRedirect("/")
#     except ArticleModel.DoesNotExist:
#         return HttpResponseNotFound("<h2>Article not found</h2>")
