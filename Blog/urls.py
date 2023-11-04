
from django.urls import path
from .views import blog_page, details

urlpatterns = [
    path('blog/', blog_page, name='blog'),
    path('detail/', details, name='detail'),
    # path('blog/<int:pk>/', drugDetailView.as_view(), name='detail'),
]
