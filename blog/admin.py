from django.contrib import admin

# Register your models here.
from blog.models import Post
from blog.models import Categoria
from blog.models import Comentario

admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Comentario)
