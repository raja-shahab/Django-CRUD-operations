from django.shortcuts import render, redirect
from recipe.models import Receipe
from django.http import HttpResponse


def receipe(request):
    if request.method == 'POST':
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = request.POST.get('receipe_name')
        receipe_description = request.POST.get('receipe_description')

        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image
        )
        return redirect('/')

    queryset = Receipe.objects.all()

    if request.GET.get('search'):
        queryset = Receipe.objects.filter(receipe_name__icontains=request.GET.get('search'))

    context = {
        'receipes': queryset
    }

    return render(request, 'index.html', context)


def delete_recipe(request, id):
    queryset = Receipe.objects.get(id=id)

    queryset.delete()
    return redirect('/')


def update_recipe(request, id):
    queryset = Receipe.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST

        receipe_image2 = request.FILES.get('receipe_image')
        receipe_name2 = data.get('receipe_name')
        receipe_description2 = data.get('receipe_description')

        queryset.receipe_name = receipe_name2
        queryset.receipe_description = receipe_description2

        if receipe_image2:
            queryset.receipe_image = receipe_image2

        queryset.save()
        return redirect('/')

    context = {
        'receipe': queryset
    }

    return render(request, 'update_receipe.html', context)


