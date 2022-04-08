from django.urls import path
from . import views
urlpatterns =[
    path("blog/", views.BlogListview.as_view(), name="blog"),
    path('blog/<int:pk>/', views.BlogDetailview.as_view(), name="post-detail"),
    path('blog/new/',views.BlogCreateView.as_view(), name="newPost")

]