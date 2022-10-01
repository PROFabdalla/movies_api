from dataclasses import fields
from urllib import request
from . import models
from rest_framework import serializers





class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id','title','describtion','created_at','updated_at','movies_cat']



    def __init__(self,*args,**kwargs):
        super(CategorySerializer,self).__init__(*args,**kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1



class MoviesSelializer(serializers.ModelSerializer):
    class Meta:
        model= models.Movies
        fields = ['id','title','rating','category','created_at','updated_at','related_movies','auther','rating_movie']


    def __init__(self, *args, **kwargs):
        super(MoviesSelializer,self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0 
        if request and request.method == 'GET':
            self.Meta.depth = 1



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id','user_name','email','password','user_movies']


    def __init__(self,*args,**kwargs):
        super(UserSerializer,self).__init__(*args,**kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1




class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Entry
        fields = ['id','header','body','created_at','updated_at','movie','auther','number_of_comments','rating','movies_comments_number']



    def __init__(self,*args,**kwargs):
        super(EntrySerializer,self).__init__(*args,**kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2




class WatcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Watcher
        fields = ['id','name','email','city','phone_num','favorate_cat','user_similar','cat_list']



    def __init__(self,*args,**kwargs):
        super(WatcherSerializer,self).__init__(*args,**kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1





class WatchMoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WatchMovies
        fields = ['id','movie','watcher','watch_time']


    def __init__(self,*args,**kwargs):
        super(WatchMoviesSerializer,self).__init__(*args,**kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1