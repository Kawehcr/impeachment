from django.contrib import admin
from django.urls import path
from impeachment.views import ImpeachmentCreateViewSet
from impeachment.views import ImpeachmentRetrieveUpdateDeleteViewSet
from impeachment.views import ImpeachmentListViewSet
from impeachment.views import RequestTestAPI

urlpatterns = [
    path("api/v1/Impeachments/create", ImpeachmentCreateViewSet.as_view(), name="Impeachment_create"),

    path("api/v1/Impeachments/<int:pk>/retrieve", ImpeachmentRetrieveUpdateDeleteViewSet.as_view(), name = "Impeachment_retrieve"),

    path("api/v1/Impeachments/<int:pk>/update", ImpeachmentRetrieveUpdateDeleteViewSet.as_view(), name = "Impeachment_update"),

    path("api/v1/Impeachments/<int:pk>/destroy", ImpeachmentRetrieveUpdateDeleteViewSet.as_view, name = "Impeachment_destroy"),

    path("api/v1/Impeachments/list", ImpeachmentListViewSet.as_view, name = "Impeachment_list"),

    path("api/v1/request", RequestTestAPI.as_view(), name = "Impeachment_test"),    
]