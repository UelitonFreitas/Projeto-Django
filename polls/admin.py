from django.contrib import admin

# Register your models here.
from polls.models import Pergunta, Escolha

class EscolhaInline(admin.TabularInline):
    model = Escolha
    extra = 3

class PerguntaDoAdmin(admin.ModelAdmin):

    list_display = ('pergunta', 'pub_date', 'foi_publicado_recentemente')

    list_filter = ['pub_date']

    fieldsets = [
        (None,               {'fields': ['pergunta']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    inlines = [EscolhaInline]

    search_fields = ['pergunta']

admin.site.register(Pergunta, PerguntaDoAdmin)
