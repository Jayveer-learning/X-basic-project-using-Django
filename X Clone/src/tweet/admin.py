from django.contrib import admin
from .models import Tweet

# Register your models here.
@admin.register(Tweet) # this is a decorator to register the model with the admin site. 
class TweetAdmin(admin.ModelAdmin):
    list_display = ['user', 'text', 'created_at'] # this is to display the fields in the admin site. 
    search_fields = ['text'] # this is to search the fields in the admin site by text field or any other fields.
    list_filter = ['created_at'] # this is to filter the fields in the admin site by created_at field or any other fields. 
    date_hierarchy = 'created_at' # this is to display the data hierarchy in the admin site by created_at field or any other fields.

# admin.site.register(Tweet, TweetAdmin) # this is the same as the about code but without the decorator but this is not recommended because it is not clear that this is a model admin class above code is more clear and recommended way to do this. 
