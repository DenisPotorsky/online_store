from django import forms


class ClientForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    phone_number = forms.IntegerField()
    address = forms.CharField(max_length=255)



class ImageForm(forms.Form):
    image = forms.ImageField()


class GoodForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.DecimalField(max_digits=15, decimal_places=2)
    quantity = forms.IntegerField()
    image = forms.ImageField(required=False)


# class OrderForm(forms.Model):
#     client = forms.ForeignKey(ClientForm, on_delete=forms.CASCADE)
#     goods = forms.ManyToManyField(GoodsForm)
#     date_ordered = forms.DateField(auto_now_add=True)
#     total_price = forms.DecimalField(max_digits=8, decimal_places=2)
