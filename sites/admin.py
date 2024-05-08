from django.contrib import admin
from .models import Article,Category,Livre,Auteur

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Livre)
admin.site.register(Auteur)

