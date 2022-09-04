from django.contrib import admin

# Register your models here.
from blog.models import post
from blog.models import Categoria
from blog.models import Comentario

admin.site.register(post)
admin.site.register(Categoria)
admin.site.register(Comentario)
