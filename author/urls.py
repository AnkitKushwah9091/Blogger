from django.urls import path
from.views import get_author_profile,get_delete_author
urlpatterns = [
    path("<slug:id>",get_author_profile,name="author-profile"),
    path("author/<int:id>/delete",get_delete_author,name="author-delete")
]
