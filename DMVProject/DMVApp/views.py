from django.shortcuts import render, redirect
from .forms import testForm
from .models import testModel


# Create your views here.
def index(request):
    if request.method == "POST":
        form = testForm(request.POST, request.FILES)
        form.save()
        return redirect("index")

    context = {
        "form": testForm(),
        "alldata": testModel.objects.all()
    }
    return render(request, "DMVApp/index.html", context)
