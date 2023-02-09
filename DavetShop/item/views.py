from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ItemCreateForm
# Create your views here.
def detail(request, pk):
    return render(request, 'item/detail.html')

@login_required
def create(request):
    if request.method == 'POST':
        form = ItemCreateForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = ItemCreateForm()

    return render(request, 'item/create.html', {
        'form': form,
        'title': 'New Item'
        }, )