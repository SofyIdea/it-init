from django.contrib import admin
from .models import Feedbacks, FeedbackResponse, FeedbackResponseReply

@admin.register(Feedbacks)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'rating', 'created_at') 
    list_filter = ('rating', 'created_at') 
    search_fields = ('author__username', 'content')  
    
@admin.register(FeedbackResponse)
class FeedbackResponse(admin.ModelAdmin):
    list_display = ('id', 'author', 'review', 'text', 'created_at') 
    
@admin.register(FeedbackResponseReply)
class FeedbackResponseReply(admin.ModelAdmin):
    list_display = ('id', 'author', 'parent_response', 'text', 'created_at') 