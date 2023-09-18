from django.contrib import admin
from Store.models import BookStore

# Register your models here.



class BookStoreModelAdmin(admin.ModelAdmin):
    list_display = ('id','name','author','category','first_pub','last_pub')


admin.site.register(BookStore, BookStoreModelAdmin)