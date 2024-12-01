from django.urls import path

from . import views

list_parties_urlpatterns = [
    path("", views.PartyListPage.as_view(), name="page_party_list"),
]
party_detail_urlpatterns = [
    path(
        "party/<uuid:party_uuid>/",
        views.PartyDetailPage.as_view(),
        name="page_single_party",
    ),
    path(
        "party/<uuid:party_uuid>/details/",
        views.PartyDetailPartial.as_view(),
        name="partial_party_detail",
    ),
]

urlpatterns = list_parties_urlpatterns + party_detail_urlpatterns
