from django.shortcuts import render, redirect
from .forms import FileForm

# Create your views here.


def upload_file(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("upload_file")
    else:
        form = FileForm()
    return render(request, "index.html", {"form": form})
