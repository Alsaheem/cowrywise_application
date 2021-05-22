from django.urls import path
from .views import MyUUIDCreatorView


urlpatterns = [
    # Apis
    path("perform-magic/", MyUUIDCreatorView.as_view(), name="perform-magic"),
]
