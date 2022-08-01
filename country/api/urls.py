from django.urls import path
from . import views as api_views


urlpatterns=[

    path('countries',api_views.country_list_create_api_view),
    path('countries/<str:iso>',api_views.country_detail_api_view)
]