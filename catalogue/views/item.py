"""
View: For management info about items.
"""
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView

from catalogue.forms import ItemBasicForm, ItemModelForm
from catalogue.models import ItemModel


# GET - query param
def items_list(request):
    """

    """
    items = ItemModel.objects.filter(pvp__gt=5)  # Select * from item_model; -> [Queryset]
    # render(object request, <name_html>, context-> dict
    return render(request, "base.html", {"products": items, "message": "Promociones"})


# POST - CREATE
def create_item(request):
    if request.method == "POST":
        form = ItemBasicForm(request.POST)
        print(form.errors)
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
class ItemViewList(ListView):
    """

    """
    model = ItemModel
    template_name = "base.html"
    context_object_name = "products"
    queryset = ItemModel.objects.filter(pvp__gt=5)  # >


class ItemCreateView(CreateView):
    model = ItemModel
    form_class = ItemModelForm
    template_name = "create.html"
    success_url = reverse_lazy("catalogue:item_list")  # devuelve la url recibiendo el name.
