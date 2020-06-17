
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "ShopHome"), 
    path("about/", views.about, name = "AboutUs"),
    path("contact/", views.contact, name = "ContactUs"),
    path("tracker/", views.tracker, name = "TreakingStatus"),
    path("search/", views.search, name = "Search"),
    path("prductview/", views.productView, name = "ProductView"),
    path("chechout/", views.checkout, name = "Checkout"),



    
]
