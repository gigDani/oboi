from django import forms

class WallpaperForm(forms.Form):
    room_length = forms.FloatField(label='Длина комнаты (м)')
    room_width = forms.FloatField(label='Ширина комнаты (м)')
    room_height = forms.FloatField(label='Высота комнаты (м)')
    roll_width = forms.FloatField(label='Ширина рулона (м)')
    roll_length = forms.FloatField(label='Длина рулона (м)')
    calculate_with_pattern = forms.BooleanField(label='Расчет с рисунком', required=False)
    pattern_repeat = forms.FloatField(label='Раппорт рисунка (м)', required=False)
    pattern_match_extra = forms.FloatField(label='Запас на подгонку (м)', required=False)
