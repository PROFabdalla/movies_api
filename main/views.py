from django.shortcuts import render
from .models import Movies , User , Entry,Category,Watcher,MovieRating
from .serializer import MoviesSelializer , UserSerializer,EntrySerializer,CategorySerializer,WatcherSerializer,MoviesRatingSeializer,UserEntrySerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404

# Create your views here.




class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset         = Category.objects.all().order_by('id')


class Categorydetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset         = Category.objects.all()



    

class ListMovies(generics.ListCreateAPIView):
    serializer_class = MoviesSelializer
    queryset = Movies.objects.all().select_related("auther","category").order_by('id')

class Moviedetais(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MoviesSelializer
    queryset = Movies.objects.all().select_related("auther","category")



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