from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('block_name', 'room_number_or_name_of_audi', 'author', 'date_created', 'date_updated')
    search_fields = ['block_name', 'room_number_or_name_of_audi']
    list_filter = ('block_name', 'author')

    def save_model(self, request, obj, form, change):
        # Save the model instance
        super().save_model(request, obj, form, change)

        # Check if an image is uploaded
        if 'image' in request.FILES:
            image = request.FILES['image']

            # Perform any additional processing here, such as resizing, renaming, etc.
            # For now, we will simply associate the image with the room number
            obj.image = image
            obj.save()

admin.site.register(Item, ItemAdmin)
