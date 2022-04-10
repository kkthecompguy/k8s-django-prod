from django.http import JsonResponse
from django.shortcuts import render
from .models import Post

# Create your views here.

def create_post_view(request):
  for i in range(100):
    Post.objects.create(title=f"Post {i}")
  return JsonResponse({"message", "post created successfully"}, safe=False)  


def list_post_view(request):
  posts = Post.objects.count()
  return JsonResponse({ 'no of posts': f"{posts} found" })