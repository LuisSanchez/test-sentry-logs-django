from django.urls import path

from logs import views

urlpatterns = [
    path(
        "logger_test/",
        views.TestView.as_view(),
        name="logger_test_view",
    ),
]
