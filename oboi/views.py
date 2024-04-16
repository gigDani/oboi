from django.shortcuts import render
from .forms import WallpaperForm
import pulp

def calculate_wallpaper_rolls(request):
    if request.method == 'POST':
        form = WallpaperForm(request.POST)
        if form.is_valid():
            # Здесь логика расчёта, аналогичная вашему Tkinter приложению
            # Используйте данные формы так: form.cleaned_data['room_length'], etc.
            # В конце, добавьте результат расчёта в контекст для отображения в шаблоне
            context = {'form': form, 'result': "Результат расчёта"}
            return render(request, 'wallpaper_calculator/calculate.html', context)
    else:
        form = WallpaperForm()
    return render(request, 'wallpaper_calculator/calculate.html', {'form': form})

