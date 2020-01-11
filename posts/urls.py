from django.conf.urls.static import static
from django.urls import path

from ustim import settings
from .views import *

urlpatterns = [
    path('', ViewFunctions.home),
    path('about', ViewFunctions.about),
    path('partners', ViewFunctions.partner),
    path('staff', ViewFunctions.staff),
    path('news', ViewFunctions.news),
    path('service', ViewFunctions.services),
    path('contact', ViewFunctions.contact),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
