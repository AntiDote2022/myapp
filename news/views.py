from django.shortcuts import render, redirect, get_object_or_404
from .models import Texts, Comments
from .forms import TextsForm, CommentsForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    new = Texts.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': new})


class NewsUpdateView(UpdateView):
    model = Texts
    template_name = 'news/create.html'

    form_class = TextsForm


class NewsDeleteView(DeleteView):
    model = Texts
    success_url = '/news/'
    template_name = 'news/news-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = TextsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма заполнена не верно'

    form = TextsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)


def add_comment(request, pk):

    post = get_object_or_404(Texts, id=pk)
    comment = Comments.objects.filter(numbers=pk)

    if request.method == 'POST':
        cform = CommentsForm(data=request.POST)
        if cform.is_valid():
            comment = cform.save(commit=False)
            comment.numbers_id = pk
            comment.save()
            return redirect('news-detail', pk)
    else:
        cform = CommentsForm
    return render(request, 'news/detail_view.html', {
        'new': post,
        'comment': comment,
        'form': cform})
