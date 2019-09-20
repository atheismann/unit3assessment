from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Wish

# Create your views here.
def home(request):
  wishes = Wish.objects.all()
  return render(request, 'index.html', {'wishes': wishes})

class WishCreate(CreateView):
  model = Wish
  fields = '__all__'
  success_url = '/'

class WishUpdate(UpdateView):
  model = Wish
  fields = '__all__'
  success_url = '/'

class WishDelete(DeleteView):
  model = Wish
  success_url = '/'