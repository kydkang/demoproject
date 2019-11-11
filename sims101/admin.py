from django.contrib import admin
from .models import Index101, Index101Data



class Index101Admin(admin.ModelAdmin):
#     # exclude=("calculated_value",)
    readonly_fields=('calculated_value', )

admin.site.register(Index101, Index101Admin)


# admin.site.register(Index101)
admin.site.register(Index101Data)


