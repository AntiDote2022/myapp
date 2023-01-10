from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    #path('<int:pk>', views.add_comment, name='comments'),
    path('<int:pk>', views.add_comment, name='news-detail'),
    #path('<int:pk>/comments2', views.CommentDetailView.as_view(), name='comments2'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete')
]