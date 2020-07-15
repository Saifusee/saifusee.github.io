from django.urls import path
from independence_day import views


urlpatterns=[

    path("", views.independence, name="independence-day"),
    path("today", views.today, name="today")
]

