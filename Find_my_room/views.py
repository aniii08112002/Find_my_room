from django.shortcuts import render, get_object_or_404
from .models import Item  # Import the Item model from your models.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def get_image(request):
    block_name = request.GET.get('block_name')
    room_number = request.GET.get('room_number')

    # Retrieve the Item object based on block_name and room_number
    item = get_object_or_404(Item, block_name=block_name, room_number_or_name_of_audi=room_number)

    # Get the image URL if an image is uploaded
    image_url = item.image.url if item.image else None

    # Render the index.html template with the image URL as context data
    return render(request, 'index.html', {'image_url': image_url})
