from django import forms

class WallpaperForm(forms.Form):
    length = forms.FloatField(label="Длина комнаты (м)")
    width = forms.FloatField(label="Ширина комнаты (м)")
    height = forms.FloatField(label="Высота комнаты (м)")
    roll_width = forms.FloatField(label="Ширина рулона (м)")
    roll_length = forms.FloatField(label="Длина рулона (м)")
