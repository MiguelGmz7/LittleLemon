from rest_framework import generics 
from .models import MenuItem
from .serializers import MenuItemSerializers
# Create your views here.

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all() # grap all the objects of that model
    serializer_class = MenuItemSerializers # serialize it using this rule

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.RetrieveDestroyAPIView):
    queryset = MenuItem.objects.all() # grap all the objects of that model
    serializer_class = MenuItemSerializers # serialize it using this rule