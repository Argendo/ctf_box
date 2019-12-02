from django import forms
from .models import Category, Task
from django.core.exceptions import ValidationError

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control' }),
            'slug': forms.TextInput(attrs={'class': 'form-control' })
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('This slug is forbidden!')

        if Category.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Blog has already have slug "{}"!'.format(new_slug))


        return new_slug

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'slug', 'body', 'categories', 'flag']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control' }),
            'slug': forms.TextInput(attrs={'class': 'form-control' }),
            'body': forms.Textarea(attrs={'class': 'form-control' }),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control' }),
            'flag': forms.TextInput(attrs={'class': 'form-control' })
        }

        def clean_slug(self):
            new_slug = self.cleaned_data['slug'].lower()

            if new_slug == 'create':
                raise ValidationError('This slug is forbidden!')

            return new_slug
