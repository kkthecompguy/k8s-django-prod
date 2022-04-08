from django.urls import path
from .views import *

urlpatterns = [
  path("", list_post_view, name="list posts"),
  path("create", create_post_view, name="create posts"),
]