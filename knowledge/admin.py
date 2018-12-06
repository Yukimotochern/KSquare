from django.contrib import admin
from knowledge.models import Relation, ForthLink, ToLink, Concept
# Register your models here.


admin.site.register(Relation)
admin.site.register(ForthLink)
admin.site.register(ToLink)
admin.site.register(Concept)

