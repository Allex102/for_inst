from django.contrib import admin
from .models import Collection,Collection_stellaj,Stellaj

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_display = ('id','book_name','autor_name', 'code','year',)

@admin.register(Stellaj)
class StellajAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_display = ('id','name',)

@admin.register(Collection_stellaj)
class Collection_stellajAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_display = ('id','book_id','stellaj_id')