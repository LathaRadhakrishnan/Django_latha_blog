from datetime import date
from django.shortcuts import render,get_object_or_404
from .models import Post
from django.views import View
from django.views.generic import ListView,DetailView
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# posts=[
# {
#         "slug": "mountains",
#         "image": "2.jpg",
#         "author": "Latha",
#         "date": date(2021, 7, 21),
#         "title": "Mountain Hiking",
#         "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
#         "content": """
#         Whether it's watching blue, rolling waves crash against the sandy shore or hearing birds chirping in a green, luscious forest, there is something so remarkable and beautiful about being immersed in nature. It’s easy to be swept away with today’s technology and fast-paced living, but no matter where you are, nature always has a way of bringing peace to the mind and grounding a person.

# A   lthough most of us spend our days online, it’s always important to unplug and step outside for a little sunshine and fresh air. Maybe it’s going for a walk in the park or planning a hike on a sunny weekend. Whatever you decide, we're sure it will be full of awe! And to celebrate Earth’s gifts, we are sharing some amazing nature quotes to emphasize some of the beauty and wonders of Mother Nature.

# So, as you venture out to see the fall foliage or spring flowers blooming, it’s also important to be mindful of how we take care of our home so it stays beautiful and healthy. Some small ways that we can all help keep nature thriving is by shopping eco-friendly products, recycling correctly and reducing food waste just to name a few. So go ahead and read through these marvelous nature quotes, as we hope they inspire you to venture out to mountains, lakes, rivers, forests and more!
# """
# },
# {
#         "slug": "path",
#         "image": "5.jpeg",
#         "author": "Padmanapan",
#         "date": date(2021, 3, 21),
#         "title": "Path Way",
#         "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
#         "content": """
#         Whether it's watching blue, rolling waves crash against the sandy shore or hearing birds chirping in a green, luscious forest, there is something so remarkable and beautiful about being immersed in nature. It’s easy to be swept away with today’s technology and fast-paced living, but no matter where you are, nature always has a way of bringing peace to the mind and grounding a person.

# A   lthough most of us spend our days online, it’s always important to unplug and step outside for a little sunshine and fresh air. Maybe it’s going for a walk in the park or planning a hike on a sunny weekend. Whatever you decide, we're sure it will be full of awe! And to celebrate Earth’s gifts, we are sharing some amazing nature quotes to emphasize some of the beauty and wonders of Mother Nature.

# So, as you venture out to see the fall foliage or spring flowers blooming, it’s also important to be mindful of how we take care of our home so it stays beautiful and healthy. Some small ways that we can all help keep nature thriving is by shopping eco-friendly products, recycling correctly and reducing food waste just to name a few. So go ahead and read through these marvelous nature quotes, as we hope they inspire you to venture out to mountains, lakes, rivers, forests and more!
# """
# },
# {
#         "slug": "nature",
#         "image": "3.jpeg",
#         "author": "Lakshmi",
#         "date": date(2021, 4, 21),
#         "title": "Nature Hiking",
#         "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
#         "content": """
#         Whether it's watching blue, rolling waves crash against the sandy shore or hearing birds chirping in a green, luscious forest, there is something so remarkable and beautiful about being immersed in nature. It’s easy to be swept away with today’s technology and fast-paced living, but no matter where you are, nature always has a way of bringing peace to the mind and grounding a person.

# A   lthough most of us spend our days online, it’s always important to unplug and step outside for a little sunshine and fresh air. Maybe it’s going for a walk in the park or planning a hike on a sunny weekend. Whatever you decide, we're sure it will be full of awe! And to celebrate Earth’s gifts, we are sharing some amazing nature quotes to emphasize some of the beauty and wonders of Mother Nature.

# So, as you venture out to see the fall foliage or spring flowers blooming, it’s also important to be mindful of how we take care of our home so it stays beautiful and healthy. Some small ways that we can all help keep nature thriving is by shopping eco-friendly products, recycling correctly and reducing food waste just to name a few. So go ahead and read through these marvelous nature quotes, as we hope they inspire you to venture out to mountains, lakes, rivers, forests and more!
# """
# },
# {
#         "slug": "beauty",
#         "image": "4.jpg",
#         "author": "Beauty",
#         "date": date(2021, 5, 21),
#         "title": "Nature Beauty",
#         "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
#         "content": """
#         Whether it's watching blue, rolling waves crash against the sandy shore or hearing birds chirping in a green, luscious forest, there is something so remarkable and beautiful about being immersed in nature. It’s easy to be swept away with today’s technology and fast-paced living, but no matter where you are, nature always has a way of bringing peace to the mind and grounding a person.

# A   lthough most of us spend our days online, it’s always important to unplug and step outside for a little sunshine and fresh air. Maybe it’s going for a walk in the park or planning a hike on a sunny weekend. Whatever you decide, we're sure it will be full of awe! And to celebrate Earth’s gifts, we are sharing some amazing nature quotes to emphasize some of the beauty and wonders of Mother Nature.

# So, as you venture out to see the fall foliage or spring flowers blooming, it’s also important to be mindful of how we take care of our home so it stays beautiful and healthy. Some small ways that we can all help keep nature thriving is by shopping eco-friendly products, recycling correctly and reducing food waste just to name a few. So go ahead and read through these marvelous nature quotes, as we hope they inspire you to venture out to mountains, lakes, rivers, forests and more!
# """
# },
# ]
# Create your views here.



# def get_date(post):
#    return post['date']

# def starting(request):
# #    sorted_posts=sorted(posts,key=get_date)
# #    latest_posts=sorted_posts[-3:]
#    latest_posts=Post.objects.all().order_by("-date")[:3]
#    return render(request,"index.html",{
#         "posts":latest_posts
#    })

class StartingPageView(ListView):
    template_name="index.html"
    model=Post
    ordering=["-date"]
    context_object_name="posts"
    
    def get_queryset(self):
        queryset= super().get_queryset()
        data=queryset[:3]
        return data

class AllPostView(ListView):
    template_name="all_post.html"
    model=Post
    ordering=["-date"]
    context_object_name="all_posts"


# def allposts(request):
#     all_posts=Post.objects.all().order_by("-date")
#     return render(request,"all_post.html",{
#         "all_posts":all_posts
#     })

# def singlepost(request,slug):
#     identified_post=get_object_or_404(Post,slug=slug)        

# #     identified_post=next(post for post in posts if post['slug']==slug)
#     return render(request,"post-detail.html",{
#         "post":identified_post
#     })

class SinglePostView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
          "post": post,
          "post_tags": post.tags.all(),
          "comment_form": CommentForm(),
          "comments":post.comments.all().order_by("-id")
        }
        return render(request, "post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
          comment = comment_form.save(commit=False)
          comment.post = post
          comment.save()
          
          return HttpResponseRedirect(reverse("singlepost", args=[slug]))

        context = {
          "post": post,
          "post_tags": post.tags.all(),
          "comment_form": comment_form,
          "comments":post.comments.all()
        }
        return render(request, "post-detail.html", context)
