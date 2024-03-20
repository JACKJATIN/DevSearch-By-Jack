from django.forms import ModelForm
from .models import Project , Review
from django import forms

# Generating form from automatic Django model Forms using forms.py 
class ProjectForm(ModelForm):
    class Meta:  # Capitalize 'Meta'
        model = Project  # Remove the parentheses after Project
        fields = ['title','description','demo_link','source_link','featured_image']
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
            
        }
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        
        #self.fields['title'].widget.attrs.update({'class':'input' , 'placeholder':'Add your Title Here'})   
        for name , field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value','body']
        labels = {
            'value':'Place Your Vote',
            'body' : 'Add a comment with Your Vote'
            }
        
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        
        #self.fields['title'].widget.attrs.update({'class':'input' , 'placeholder':'Add your Title Here'})   
        for name , field in self.fields.items():
            field.widget.attrs.update({'class':'input'})