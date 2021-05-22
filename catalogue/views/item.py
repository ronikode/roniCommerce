"""
View: For management info about items.
"""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView

from carts.forms import CartAddItemForm
from catalogue.forms import ItemBasicForm, ItemModelForm
from catalogue.models import ItemModel, CategoryModel


# GET - query param
@login_required(login_url="users:login")
def items_list(request):
    """

    """
    items = ItemModel.objects.filter(pvp__gt=5)  # Select * from item_model; -> [Queryset]
    # render(object request, <name_html>, context-> dict
    user = request.user  # None si no inicia sesion

    return render(request, "catalogue/index.html", {"products": items, "message": "Promociones"})


# POST - CREATE
def create_item(request):
    if request.method == "POST":
        form = ItemBasicForm(request.POST)
        if form.is_valid():  # Valida si los datos ingresados son correctos
            data = form.cleaned_data  # dict
            ItemModel.objects.create(**data)  # Crear el registro en bd
            messages.success(request, "Item creado exitosamente!")
            return HttpResponseRedirect(reverse("catalogue:item_list"))
        else:
            messages.error(request, "Data enviada no es válida!")
    form = ItemBasicForm()
    return render(request, "create.html", {"form": form})


# CRUD - Create , Read , Update , Delete
class ItemViewList(LoginRequiredMixin, ListView):
    """

    """
    model = ItemModel
    template_name = "catalogue/index.html"
    context_object_name = "products"
    redirect_field_name = reverse_lazy("users:login")
    queryset = ItemModel.objects.filter(pvp__gt=5)  # >


class ItemCreateView(CreateView):
    model = ItemModel
    form_class = ItemModelForm
    template_name = "create.html"
    success_url = reverse_lazy("catalogue:item_list")  # devuelve la url recibiendo el name.


# Catalogue
def item_catalogue(request, category_slug: str = None):
    category = None
    qs_categories = CategoryModel.objects.order_by("name")
    items = ItemModel.objects.order_by("name")
    if category_slug:
        category = get_object_or_404(CategoryModel, slug=category_slug)
        items = items.filter(category=category)  # []
    return render(request, "catalogue/list.html",
                  {"category": category, "categories": qs_categories, "items": items})


def item_detail(request, id: int, slug: str):
    item = get_object_or_404(ItemModel, id=id, slug=slug)
    cart_item_from = CartAddItemForm()
    return render(request, "catalogue/detail.html", {"item": item, "cart_item_form": cart_item_from})


# Search
def item_search(request):
    """

    """
    search_param = request.get("search")
    qs_items = ItemModel.objects.filter(
        Q(name__icontains=search_param) or Q(category__name__icontains=search_param)
    )
    return render(request, "catalogue/list.html", {"items": qs_items})
