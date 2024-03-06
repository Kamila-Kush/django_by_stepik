from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.index, name="index"),
    path("about-us/", views.about_us, name="about_us"),
    path("contacts/", views.contact, name="contacts")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
