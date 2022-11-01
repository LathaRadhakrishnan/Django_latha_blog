from django.urls import path
from . import views
urlpatterns=[
    path("",views.StartingPageView.as_view(),name="starting"),
    path("posts", views.AllPostView.as_view(), name="allpost_page"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="singlepost")
]