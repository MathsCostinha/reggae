from django.urls import path
from .views import HomePageView, ListagemView, PostagemDetailView, PostCreateView, PostUpdateView, PostDeleteView
urlpatterns = [
    path('post/', HomePageView.as_view(), name ='homepost'),
    path('post/listagem/', ListagemView.as_view(), name='listagem'),
    path('post/<int:pk>/', PostagemDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post_delete'),
]