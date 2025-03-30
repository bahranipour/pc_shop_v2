from django import forms
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,ProductReview
from django.contrib.auth import get_user_model

User = get_user_model()


class OrderForm(forms.Form):
    quantity = forms.IntegerField(
        label='تعداد',
        min_value=1,
        max_value=20,
        validators=[MinValueValidator(0)],
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': '1',
            'id': 'quantity-input'
        })
    )
    
    def __init__(self, *args, max_quantity=None, **kwargs):
        super().__init__(*args, **kwargs)
        if max_quantity:
            self.fields['quantity'].validators.append(MaxValueValidator(max_quantity))
            self.fields['quantity'].widget.attrs['max'] = str(max_quantity)




class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True, label='شماره تماس')
    address = forms.CharField(widget=forms.Textarea, required=True, label='آدرس')
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'address', 'password1', 'password2')


    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('ایمیل قبلا استفاده شده است')
            
        return data 
    






class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'rows': 3,
                'class': 'form-control',
                'placeholder': 'دیدگاه خود را بنویسید...'
            }),
        }
        labels = {
            'rating': 'امتیاز شما',
            'comment': 'دیدگاه'
        }



class SearchForm(forms.Form):
    query = forms.CharField(label='جستجو',max_length=100,widget=forms.TextInput(attrs={'class':'form-control rounded-0'}))
        