from django.shortcuts import render
from . models import Item
from django.core.paginator import Paginator

from django.views.generic import ListView


def index(request):
  items = Item.objects.all()

  paginator = Paginator(items, 5)

  page_number = request.GET.get('page')   # გვერდის კონკრეტული ნომერი
  page_obj = paginator.get_page(page_number)  # კონკრეტული გვერდის ჩატვირთვა

  context = {
    'items': page_obj
  }

  return render(request, 'items/index.html', context)


class ItemsList(ListView):
  paginate_by = 4
  model = Item
  template_name = 'items/items-list.html'
  context_object_name = 'items'