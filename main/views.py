from django.shortcuts import render

def show_main(request):
    context = {
        'my_name': 'Mikhail Haritz',
        'my_class': 'PBP F'
    }

    return render(request, "main.html", context)

# Create your views here.
