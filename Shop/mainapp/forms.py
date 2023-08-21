from django import forms
from mainapp.models import Book, News, Quote, Comment, ImageBook, Authors, Genre


class BoorCreateUpdateForm(forms.Form):
    name = forms.CharField(max_length=64)
    author = forms.CharField(max_length=64)
    foto = forms.ImageField(widget=forms.FileInput(), required=False)
    article = forms.IntegerField()
    date_receipt = forms.DateField()
    category = forms.CharField(max_length=64)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=8, decimal_places=2)


    # class Meta:
    #     model = Book
    #     fields = (
    #         'name',
    #         'author',
    #         'foto',
    #         'article',
    #         'date_receipt',
    #         'category',
    #         'description',
    #         'price',
    #     )

    def __init__(self, *args, **kwargs):
        super(BoorCreateUpdateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите название'
        self.fields['author'].widget.attrs['placeholder'] = 'Укажите автора'
        self.fields['article'].widget.attrs['placeholder'] = 'Укажите артикул'
        self.fields['category'].widget.attrs['placeholder'] = 'Выберете жанр'
        self.fields['description'].widget.attrs['placeholder'] = 'Описание'

        self.fields['date_receipt'] = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'u-full-width'


class ImagesForBookForm(forms.ModelForm):
    foto = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = ImageBook
        fields = (
            'guid',
            'foto',
        )

    def __init__(self, *args, **kwargs):
        super(ImagesForBookForm, self).__init__(*args, **kwargs)
        self.fields['foto'].widget.attrs['class'] = 'u-full-width'


class NewsCreateUpdateForm(forms.ModelForm):
    foto = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = News
        fields = (
            'name',
            'description',
            'text',
            'foto',
        )

    def __init__(self, *args, **kwargs):
        super(NewsCreateUpdateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите название'
        self.fields['description'].widget.attrs['placeholder'] = 'Введите краткое содержание'
        self.fields['text'].widget.attrs['placeholder'] = 'Введите текст'

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'u-full-width'


class QuoteCreateUpdateForm(forms.ModelForm):

    class Meta:
        model = Quote
        fields = (
            'name',
            'text',
            'author',
            'is_active'
        )

    def __init__(self, *args, **kwargs):
        super(QuoteCreateUpdateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите название'
        self.fields['text'].widget.attrs['placeholder'] = 'Введите текст'
        self.fields['author'].widget.attrs['placeholder'] = 'Введите автора'

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'u-full-width'


class CommentCreateUpdateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = (
            'text',
            'starts',
            'user',
            'book'
        )

        widgets = {
            "book": forms.HiddenInput(),
            "user": forms.HiddenInput(),
            "starts": forms.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        super(CommentCreateUpdateForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['placeholder'] = 'Введите текст'
        self.fields['text'].widget.attrs['class'] = 'u-full-width'


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Authors
        fields = (
            'person',
        )

    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        self.fields['person'].widget.attrs['placeholder'] = 'Укажите автора'


class GenreForm(forms.ModelForm):

    class Meta:
        model = Genre
        fields = (
            'category',
        )

    def __init__(self, *args, **kwargs):
        super(GenreForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs['placeholder'] = 'Укажите жанр'