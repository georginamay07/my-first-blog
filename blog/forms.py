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
        self.fields['profile_title'].disabled = True
        self.fields['work_experience_title'].disabled = True
        self.fields['education_title'].disabled = True
        self.fields['additional_skills_title'].disabled = True

    class Meta:
        model = CV
        fields = ('name', 'job_title', 'email','mobile','profile_title','profile_text','work_experience_title','work_experience_header','work_experience_date',
        'work_experience_text','work_experience_header_2','work_experience_date_2',
        'work_experience_text_2','education_title','education_header','education_date','education_text','additional_skills_title','additional_skills_text')