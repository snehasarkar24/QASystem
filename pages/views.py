from django.shortcuts import render


def home(request):
    from pages.main import namer, visit
    return render(request, "home.html", {"name": namer})


def query(request):
    if request.method == "post":
        query_entry = request.post['myValue']
        print(query_entry)



