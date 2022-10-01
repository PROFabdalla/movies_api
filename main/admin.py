from django.contrib import admin
from .models import Movies ,Category,User,Entry, Watcher,MovieRating

# Register your models here.


admin.site.register(Category)
admin.site.register(Movies)
admin.site.register(User)
admin.site.register(Entry)
admin.site.register(Watcher)
# admin.site.register(WatchMovies)
admin.site.register(MovieRating)
