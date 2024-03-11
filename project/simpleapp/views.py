from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import New


class NewsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = New
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'title'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class NewDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельной новости
    model = New
    # Используем другой шаблон — new.html
    template_name = 'new.html'
    # Название объекта, в котором будет выбранная пользователем новость
    context_object_name = 'new'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context

