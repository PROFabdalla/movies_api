from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ListMovies,Moviedetais,UserList,Userdetails,EntryList,Entrydetails,CategoryList,Categorydetails,WatcherList,Watcherdetails,WatchermovieList,WatchermovieDetails,Usermovies

urlpatterns = [
    path('category',CategoryList.as_view(),name='categories'),
    path('category/<int:pk>',Categorydetails.as_view(),name='category'),

    path('movies',ListMovies.as_view(),name='movies'),
    path('movie/<int:pk>',Moviedetais.as_view(),name='movie'),

    path('users',UserList.as_view()),
    path('user/<int:pk>',Userdetails.as_view()),

    path('entry',EntryList.as_view(),name='entry'),
    path('entry/<int:pk>',Entrydetails.as_view(),name='entry'),

    path('watcher',WatcherList.as_view()),
    path('watcher/<int:pk>',Watcherdetails.as_view()),


    path('watch_movies',WatchermovieList.as_view()),
    path('watch_movies/<int:pk>',WatchermovieDetails.as_view()),

    path('user_movies/<int:user_id>',Usermovies.as_view()),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)