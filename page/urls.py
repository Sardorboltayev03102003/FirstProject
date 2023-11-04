from django.urls import path

from .views import stuff_page, gallery_page, reservation_page

urlpatterns = [
    path('reservation/', reservation_page, name="reservation"),
    path('stuff/', stuff_page, name="stuff"),
    path('gallery/', gallery_page, name="gallery")

]
