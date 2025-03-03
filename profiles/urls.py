from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from profiles.views import ProfileDetailView, ProfileListView, ProfileUpdateView

app_name = "profile"

urlpatterns = [
    path('list/', ProfileListView.as_view(), name='list'),
    path('detail/<pk>/', ProfileDetailView.as_view(), name='detail'),
    path('update/<pk>/', ProfileUpdateView.as_view(), name='update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
