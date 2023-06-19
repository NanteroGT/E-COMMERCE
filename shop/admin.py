from django.contrib import admin
from .models import Product,Category,Commande,Newsletter,Contact
# Register your models here.
admin.site.site_header="Don-Shop"
admin.site.site_title="Don-Shop"
admin.site.index_title="chez meleine"

class AdminCategorie(admin.ModelAdmin):
    list_display = ('name','date_added')
    list_per_page=5

class AdminProduct(admin.ModelAdmin):
    list_display = ('title','price','category','pop','date_added')
    search_fields=('title',)
    list_editable=('price','pop')
    list_per_page=5

class AdminCommande(admin.ModelAdmin):
    list_display = ('items','nom','num','address','ville','total','date_commande')
    list_per_page=5

class ContactAdmin(admin.ModelAdmin):
    list_display=('nom','email','besoin','message','date')
    list_per_page=5
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategorie)
admin.site.register(Commande,AdminCommande) 
admin.site.register(Newsletter) 
admin.site.register(Contact,ContactAdmin)
