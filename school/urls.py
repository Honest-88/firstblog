from . import views
from django.urls import path ,include


app_name='school'

urlpatterns = [
    
    path('', views.CategoryListView.as_view(), name='category_list'),
    path('<slug:slug>/', views.CategoryListView.as_view(), name='category_list'),
    path('post_list/<str:category>/<slug:slug>/', views.PostListView.as_view(), name='post_list'),
    path('tags/<slug:tag_slug>/', views.TagIndexView.as_view(), name='posts_by_tag'),
    path('post_detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post_detail/<str:category>/<str:name>/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),

    path('search_results', views.search_results, name='search_results'),
   # path('<str:post>/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    #path('post_create/<str:category>/<int:pk>/create/', views.PostCreateView.as_view(), name='post_create'),
    path('<str:category>/<slug:slug>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('<str:category>/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('tinymce/', include('tinymce.urls')),
]

