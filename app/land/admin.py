from django.contrib import admin

from .models import SoilNutrient,RecommendedPlant


@admin.register(SoilNutrient)
class SoilNutrientAdmin(admin.ModelAdmin):
    list_display = ('name','description', 'nitrogen','phosphorous','potasium')
    search_fields = ('name','description','client__email') 
 
    actions = ['fertile','not_fertile' ]
    
    def fertile(self, queryset):
        queryset.update(is_fertile=True)
        
    def not_fertile(self, queryset):
        queryset.update(is_fertile=False)
        
 
@admin.register(RecommendedPlant)
class RecommendedPlantAdmin(admin.ModelAdmin):
    list_display = ('name','soil')
    search_fields = ('name','soil__name','soil__description') 
 
 