from django.shortcuts import render
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .serializers import RestaurantSerializer
from .models import Dish


def search(request):
    query = request.GET.get('q', '')
    if query:
        dishes = Dish.objects.filter(Q(name__icontains=query) | Q(name__istartswith=query))[:10]
    else:
        dishes = Dish.objects.none()
    context = {'query': query, 'dishes': dishes}
    return render(request, 'search.html', context)


@api_view(['GET', 'POST'])
def restaurant_list(request):
    if request.method == 'GET':
      restaurant = Dish.objects.all()
      serializer = RestaurantSerializer(restaurant, many=True)
      return Response(serializer.data)

    elif request.method == 'POST':
      serializer = RestaurantSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    


@api_view(['GET', 'PUT', 'DELETE'])
def restaurant_detail(request, pk):
    restaurants = get_object_or_404(Dish, pk=pk)

    if request.method == 'GET':
        serializer = RestaurantSerializer(restaurants);
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = RestaurantSerializer(restaurants, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
    elif request.method == 'DELETE':
        restaurants.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

