from django.http import HttpResponse


def show(request):
    return HttpResponse('---PIZZA---')
