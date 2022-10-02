from django.shortcuts import render
from .models import Movies , User , Entry,Category,Watcher,MovieRating,WatchMovies
from .serializer import MoviesSelializer , UserSerializer,EntrySerializer,CategorySerializer,WatcherSerializer,MoviesRatingSeializer,UserEntrySerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

# Create your views here.




class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset         = Category.objects.all().order_by('id')


class Categorydetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset         = Category.objects.all()



    

class ListMovies(generics.ListCreateAPIView):
    serializer_class = MoviesSelializer
    queryset = Movies.objects.all().select_related("auther","category").prefetch_related("watcher").order_by('id')

class Moviedetais(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MoviesSelializer
    queryset = Movies.objects.all().select_related("auther","category").prefetch_related("watcher")



class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset         = User.objects.all().order_by('id')



class Userdetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset         = User.objects.all()



class EntryList(generics.ListCreateAPIView):
    serializer_class = EntrySerializer
    queryset         = Entry.objects.all().select_related("movie","movie__category").prefetch_related("auther").order_by('id')


class Entrydetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EntrySerializer
    queryset         = Entry.objects.all().select_related("movie","movie__category").prefetch_related("auther")


class WatcherList(generics.ListCreateAPIView):
    serializer_class = WatcherSerializer
    queryset         = Watcher.objects.all().order_by('id')


class Watcherdetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WatcherSerializer
    queryset         = Watcher.objects.all()



# class WatchermovieList(generics.ListCreateAPIView):
#     serializer_class = WatchMoviesSerializer
#     queryset = WatchMovies.objects.all().select_related("movie").prefetch_related("watcher")



# class WatchermovieDetails(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = WatchMoviesSerializer
#     queryset = WatchMovies.objects.all().select_related("movie").prefetch_related("watcher")
#     # queryset = WatchMovies.objects.all().prefetch_related("movie","watcher")








class MoviesRatingList(generics.ListCreateAPIView):
    serializer_class = MoviesRatingSeializer
    queryset = MovieRating.objects.all()



class MoviesRatingDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MoviesRatingSeializer
    queryset = MovieRating.objects.all()



class Usermovies(generics.ListCreateAPIView):
    serializer_class = MoviesSelializer
    def get_queryset(self):
        user_id= self.kwargs['user_id']
        user = get_object_or_404(User,pk=user_id)
        return Movies.objects.filter(auther=user).select_related("auther","category")



class UserEntries(generics.ListCreateAPIView):
    serializer_class = UserEntrySerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user    = get_object_or_404(User,pk=user_id)

        return Entry.objects.filter(auther=user).select_related("movie").prefetch_related("auther")



class SearchMovie(generics.ListCreateAPIView):
    serializer_class = MoviesSelializer
    queryset = Movies.objects.all().select_related("auther","category").prefetch_related("watcher")

    def get_queryset(self):
        qs = super().get_queryset()
        if 'searchmovie' in self.kwargs:
            search = self.kwargs['searchmovie']
            qs = Movies.objects.filter(title__icontains=search).select_related("auther","category").prefetch_related("watcher")
        return qs



def fetch_watched_movies(request,watcher_id,movie_id):
    watcher = get_object_or_404(Watcher,pk=watcher_id)
    movie   = get_object_or_404(Movies,pk=movie_id)
    watch_movies = WatchMovies.objects.filter(movie=movie,watcher=watcher).count()
    if watch_movies:
        return JsonResponse({'bool':True})
    else:
        return JsonResponse({'bool':False})




def delet_movie(request,user_id,movie_id):
    user = get_object_or_404(User,pk=user_id)
    movie_state = Movies.objects.filter(auther=user,pk=movie_id).delete()
    if movie_state:
        return JsonResponse({'bool':True})
    else:
        return JsonResponse({'bool':False})



def delete_rating(request,watcher_id,rating_id):
    watcher = get_object_or_404(Watcher,pk=watcher_id)
    del_rating = MovieRating.objects.filter(user=watcher,pk=rating_id).delete()
    if del_rating:
        return JsonResponse({'bool':True})
    else:
        return JsonResponse({'bool':False})




