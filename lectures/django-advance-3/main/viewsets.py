from rest_framework import viewsets
from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSerializer


class MenuItemViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = MenuItem.objects.all()
        serializer = MenuItemSerializer(queryset, many=True)
        return Response(serializer.data)