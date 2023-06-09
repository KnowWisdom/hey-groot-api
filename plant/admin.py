from django.contrib import admin
from .models import *

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'name', 'character_id', 'plant_id', 'is_alarm', 'pot_color')
    
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'plant_id')
    
@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'content', 'is_confirm')    
    
@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'question', 'answer')