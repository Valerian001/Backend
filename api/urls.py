from django.urls import path, include # type: ignore
from .views import ContactFormView, ImageViewSet, AchivitaContactFormView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'images', ImageViewSet, basename='images')



urlpatterns = [
    path('contact/', ContactFormView.as_view(), name='contact-form'),
    path('achivitacontact/', AchivitaContactFormView.as_view(), name='achivita-contact-form'),
    path('', include(router.urls)),  # Include the router's URLs
]

# Include the router's URLs in the urlpatterns
# urlpatterns += router.urls

# Ensure media files are served in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)