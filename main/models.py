from django.db import models
from datetime import date,time
from django.core import serializers
import bcrypt
from django.shortcuts import get_object_or_404

# Create your models here.


class Category(models.Model) :
    title       = models.CharField(max_length=100)
    describtion = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title






class User(models.Model):
    user_name  = models.CharField(max_length=120)
    email      = models.EmailField()
    password   = models.CharField(max_length=120,blank=True,null=True)

    

    def user_movies(self):
        movies = Movies.objects.filter(auther=self).count()
        return movies


    def movies_views(self):
        views_number = Watcher.objects.filter(movies__auther=self).count()
        return views_number


    # def count_movies_in_entries(self):
    #     total_movies_in_entry = Movies.objects.filter(entry__auther=self).select_related("entry","entry_auther").count()
    #     return total_movies_in_entry
        


    def __str__(self):
        return self.user_name






class Watcher(models.Model):
    name = models.CharField(max_length=120)
    email= models.EmailField()
    city  = models.CharField(max_length=120)
    phone_num = models.IntegerField()
    # profile_img=models.ImageField(upload_to='watcher_profile_imgs/',null=True)
    favorate_cat = models.TextField(null=True)

    def user_similar(self):
        similar_user = Watcher.objects.filter(favorate_cat__icontains=self.favorate_cat)
        return serializers.serialize('json',similar_user)

    def cat_list(self):
        categries = self.favorate_cat.split(',')
        return categries


    def __str__(self):
        return self.name







class Movies(models.Model):
    title      = models.CharField(max_length=120)
    rating     = models.IntegerField(default=0)
    category   = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,related_name='movies_cat')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auther     = models.ForeignKey(User,on_delete=models.CASCADE,related_name='movies',null=False)
    watcher    = models.ManyToManyField(Watcher,related_name='movies')



    def related_movies(self):
        rel_movie = Movies.objects.filter(category__title__startswith=self.category).select_related("category")
        return serializers.serialize('json',rel_movie)


    def rating_movie(self):
        rating_movie = MovieRating.objects.filter(movie=self).aggregate(rating_avg=models.Avg('rating'))
        return rating_movie['rating_avg']


    def __str__(self):
        return self.title









class MovieRating(models.Model):
    rating             = models.IntegerField(default=5)
    review             = models.TextField()
    created_at         = models.DateField(auto_now_add=True)
    updated_at         = models.DateField(default=date.today)
    movie              = models.ForeignKey(Movies,on_delete=models.CASCADE,related_name="movierating")
    user               = models.ForeignKey(Watcher,on_delete=models.CASCADE,related_name="ratingauther")



    def __str__(self):
        return f"rating {self.movie} user{self.user}"




class WatchMovies(models.Model):
    movie = models.ForeignKey(Movies,on_delete=models.CASCADE,related_name='watched_movie')
    watcher = models.ManyToManyField(Watcher,related_name='watched_watcher')
    watch_time = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"movie:{self.movie}--wtcher:{self.watcher}"




class Entry(models.Model):
    header             = models.CharField(max_length=255)
    body               = models.TextField()
    created_at         = models.DateField(auto_now_add=True)
    updated_at         = models.DateField(default=date.today)
    movie              = models.ForeignKey(Movies,on_delete=models.CASCADE)
    auther             = models.ManyToManyField(User)
    number_of_comments = models.IntegerField(default=0)
    rating             = models.IntegerField(default=5)



    def movies_comments_number(self):
        movies_comments = MovieRating.objects.filter(movie=self.movie).count()
        return movies_comments



    def __str__(self):
        return self.header
