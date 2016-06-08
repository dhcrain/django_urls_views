from django.http import HttpResponse
from django.shortcuts import render
from templates import test_temp

# Create your views here.


def index_view(request):
    return HttpResponse("This is an index view page!")


def hello_view(request):
    return HttpResponse("Hello, Hello, Hello, Hello, Hello, Hello, Hello, Hello World!")
    # return render(request, 'test_temp/yippee.html', {})


def red_baloons_view(request):
    return HttpResponse("Hast Du etwas Zeit für mich\nDann singe ich ein Lied für Dich\n"
                        "Von 99 Luftballons\nAuf ihrem Weg zum Horizont")
