"""

"""

from django.urls import path

from catalogue.views.item import items_list, ItemViewList, create_item, ItemCreateView, item_catalogue, item_detail, \
    item_search

app_name = "catalogue"

urlpatterns = [

    path('', item_catalogue, name="item_catalogue"),
    path('<slug:category_slug>/', item_catalogue, name="item_catalogue_slug"),
    path('detail/<int:id>/<str:slug>', item_detail, name="item_catalogue_detail"),
    path('search/', item_search, name="item_catalogue_search"),


    path('items/', items_list, name="item_list"),
    path('items-2/', ItemViewList.as_view(), name="item_class_list"),

    path('items/create/', create_item, name="item_new"),
    path('items/create/2/', ItemCreateView.as_view(), name="item_new_2")
]
