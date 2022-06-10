from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse


def movie_list(request):
    movies = Movie.objects.all() # trae todas las movies
    data = {'movies':list(movies.values())}
    return JsonResponse(data)

def movie_details(request,pk):
    movie = Movie.objects.get(pk=pk) #trae una película en especifico
    data = {'name':movie.name, 
            'description':movie.description,
            'active':movie.active}
    return JsonResponse(data)