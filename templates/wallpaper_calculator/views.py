from django.shortcuts import render
from .forms import WallpaperForm
import pulp

def calculate_wallpaper(request):
    if request.method == 'POST':
        form = WallpaperForm(request.POST)
        if form.is_valid():
            room_length = form.cleaned_data['length']
            room_width = form.cleaned_data['width']
            room_height = form.cleaned_data['height']
            roll_width = form.cleaned_data['roll_width']
            roll_length = form.cleaned_data['roll_length']

            perimeter = 2 * (room_length + room_width)
            strips_per_roll = roll_length // room_height

            total_strips_needed = perimeter // roll_width
            rolls = pulp.LpVariable("Rolls", lowBound=0, cat='Integer')

            problem = pulp.LpProblem("Wallpaper Calculation", pulp.LpMinimize)
            problem += rolls
            problem += strips_per_roll * rolls >= total_strips_needed
            problem.solve()

            result = f"Необходимое количество рулонов: {int(pulp.value(rolls))}"
            return render(request, 'wallpaper_calculator/result.html', {'form': form, 'result': result})
    else:
        form = WallpaperForm()

    return render(request, 'wallpaper_calculator/index.html', {'form': form})
