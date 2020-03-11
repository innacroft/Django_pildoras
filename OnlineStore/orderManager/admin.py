from django.contrib import admin

# Register your models here.
from orderManager.models import Clients,Articles,Orders


class ClientsAdmin(admin.ModelAdmin):
  list_display=("name","address","tel","email")
  search_fields=("name", "email")

class ArticlesAdmin(admin.ModelAdmin):
  list_filter=("section",)

class OrdersAdmin(admin.ModelAdmin):
  list_display=("number","date")
  list_filter=("date",)
  date_hierarchy="date" #visualizacion de filtros (date) de forma horizontal




admin.site.register(Clients,ClientsAdmin)
admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Orders,OrdersAdmin)