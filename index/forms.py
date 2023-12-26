from django import forms
from . import models
import re


class ContactForm(forms.ModelForm):
    
    name = forms.CharField(error_messages={
        "required":'Yozilinishi shart'
    },
    label= "Ism",
    widget=forms.TextInput(attrs={
        'class': 'form-control',
        "placeholder":"Ism"
    })
    )
    
    surname = forms.CharField(error_messages={
        "required":'Yozilinishi shart'
    },
    label="Familiya",
    widget=forms.TextInput(attrs={
        'class': 'form-control',
        "placeholder":"Familiya"
    }))
    
    phone = forms.CharField(error_messages={
        "required":'Yozilinishi shart'
    }, label="Telefon raqam",
    widget=forms.TextInput(attrs={
        'class': 'form-control',
        "placeholder":"Telefon raqam"
    }))
    
    
    courses = forms.ModelMultipleChoiceField(
        queryset=models.Course.objects.all(),
        required=False,
        label="Kurslar",
        error_messages={
            'required': 'Qaysi kursga yozilmoqchisiz',
            'invalid_choice': "Tog'ri kiriting",
        },
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-control',
        })
    )

    
    
    class Meta:
        model = models.Students
        fields = ['name', 'surname', 'phone', 'courses']
        
    
    
    def clean_phone(self):
        pattern = r'^\+998\d{2}\d{3}\d{2}\d{2}$'
        
        phone = self.cleaned_data['phone']
        print(re.match(pattern, phone), pattern)
        if re.match(pattern, phone):
            return phone
        raise forms.ValidationError("Telefon raqamini: +998 ko'rinishida yozing va joy Tashlamang")
        