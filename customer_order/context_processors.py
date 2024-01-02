# your_app/context_processors.py
from django.contrib import messages

def custom_messages(request):
    return {'messages': messages.get_messages(request)}
