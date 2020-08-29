from django import forms
from .models import Post
from .models import CV
from .models import Work
from .models import Education
from django.forms.models import inlineformset_factory



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
        fields = ('profile_picture','name', 'job_title', 'email','mobile','professional_profile','additional_skills_description')

class WorkForm(forms.ModelForm):


    class Meta:
        model=Work
        fields = ('work_experience_location','work_experience_date',
        'work_experience_description')

class EducationForm(forms.ModelForm):

    class Meta:
        model=Education
        fields = ('education_location','education_date','education_description')

