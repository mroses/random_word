from django.shortcuts import render
from django.utils.crypto import get_random_string 
# Create your views here.
def index(request):
    context= {
        "word": get_random_string(length=14),
        "number": (number + 1)
    }
    return render(request, "random_word/index.html", context)
