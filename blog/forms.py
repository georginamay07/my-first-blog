from django import forms

from .models import Post
from .models import CV

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CVForm(forms.ModelForm):

    def __init__(self, *args, **kwargs): 
        super(CVForm, self).__init__(*args, **kwargs)                       
        self.fields['name'].disabled = True

    class Meta:
        model = CV
        fields = ('name', 'job_title', 'email','mobile','professional_profile','work_experience_location','work_experience_date',
        'work_experience_description','education_location','education_date','education_description','additional_skills_description')

