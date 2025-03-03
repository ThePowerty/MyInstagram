from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from posts.views import PostCreateView, PostDetailView, PostDeleteView, like_post_ajax

app_name = "post"

urlpatterns = [
    path('create/', PostCreateView.as_view(), name="create"),
    path('detail/<pk>/', PostDetailView.as_view(), name="detail"),
    path('delete/<pk>/', PostDeleteView.as_view(), name='delete'),
    path('like/<pk>/', like_post_ajax, name="like"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
