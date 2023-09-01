from django import forms
from .models import *

class fill_TODO_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.required = False

    class Meta:
        model = fill_TODO
        fields = '__all__'


class System_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.required = False

    class Meta:
        model = System
        fields = '__all__'


class Modules_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.required = False

    class Meta:
        model = Modules
        fields = '__all__'


class Products_form(forms.ModelForm):
    uType = forms.ChoiceField(choices=[('', '-------'), ('Миграция', 'Миграция'), ('Разработка','Разработка'), ('Интеграция','Интеграция')],
                              label='Type', widget=forms.Select)
    uStatus = forms.ChoiceField(choices=[('', '-------'), ('Не определен', 'Не определен'), ('Не эксплуатируется', 'Не эксплуатируется'), \
                                         ('На паузе', 'На паузе'), ('Эксплуатируется/Завершен', 'Эксплуатируется/Завершен'), ('<резерв>','<резерв>')],
                                label='Статус', widget=forms.Select)
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.required = False
        
    class Meta:
        model = Products
        fields = '__all__'
        widgets = {
                   'uStartTime' : forms.SelectDateWidget(attrs={'style': 'width: 100px;'}),
                   'uStopTime' : forms.SelectDateWidget(attrs={'style': 'width: 100px;'})}  
        

class ArchLayout_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.required = False

    class Meta:
        model = ArchLayout
        fields = '__all__'


class ProductsVeh_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.required = False

    class Meta:
        model = ProductsVeh
        fields = '__all__'
        widgets = {
                   'uVehDate' : forms.SelectDateWidget(attrs={'style': 'width: 100px;'}),
                   'uVehClosed': forms.CheckboxInput(attrs={'style': 'width: 20px; height: 20px;'}),}  

class ProductsVnedr_form(forms.ModelForm):
    uVnedrStatus = forms.ChoiceField(choices=[('', '-------'), ('Не определен', 'Не определен'), ('Не эксплуатируется', 'Не эксплуатируется'), \
                                         ('На паузе', 'На паузе'), ('Эксплуатируется/Завершен', 'Эксплуатируется/Завершен'), ('<резерв>','<резерв>')],
                                label='Статус', widget=forms.Select)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.required = False

    class Meta:
        model = ProductsVnedr
        fields = '__all__'
        widgets = {
                   'uVnedrStartTime' : forms.SelectDateWidget(attrs={'style': 'width: 100px;'}),
                   'uVnedrStopTime' : forms.SelectDateWidget(attrs={'style': 'width: 100px;'})}  
        

class Resources_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.required = False
    
    class Meta:
        model = Resources
        fields = '__all__'
        widgets = {'uResLeader' : forms.CheckboxInput(attrs={'style' : 'width: 20px; height: 20px;'})}

        
class SaveCommentForm(forms.ModelForm):

    uProductIDReport = forms.CharField(required=False)
    uVehIDReport = forms.CharField(required=False)
    
    class Meta:
        model = ReportCommentsNew
        fields = ['uProductIDReport', 'uVehIDReport', 'text']