from django.test import TestCase
from django.urls import reverse, resolve

from .views import HomePageView, ArticleList, ArticleCategoryList, ArticleDetail


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
    def test_home_url_resolves_home_view(self):
        view = resolve('/') 
        self.assertEquals(view.func.view_class, HomePageView)

class ArticlesTests(TestCase):
    def test_articles_list_view_status_code(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_articles_list_url_resolves_view(self):
        view = resolve('/articles')
        self.assertEquals(view.func.view_class, ArticleList)


class CategoryTest(TestCase):
    def test_category_view_status_code(self):
        url = reverse('articles-category-list', args=('name',))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
    def test_category_url_resolves_view(self):
        view = resolve('/articles/category/test-slug')
        self.assertEquals(view.func.view_class, ArticleCategoryList)
        
class ArticlesDetailTest(TestCase):
    def test_article_detail_view_status_code(self):
        url = reverse('news-detail', args=('2025', '10', '27', 'test-slug'))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_article_detail_url_resolves_view(self):
        view = resolve('/articles/2025/10/27/test-slug')
        self.assertEquals(view.func.view_class, ArticleDetail)