from django import forms
from livro.models import Livro, Valor

class LivroForm (forms.Form):
    livro = forms.CharField(max_length=100)
    paginas = forms.IntegerField()
    autor = forms.CharField(max_length=75)
    data = forms.DateField()
    foto = forms.ImageField()

    def save (self):

        livro_novo = Livro(
            livro= self.data['livro'],
            paginas=self.data['paginas'],
            autor=self.data['autor'],
            data=self.data['data'],
            foto=self.files['foto'],
        )

        livro_novo.save()
        return livro_novo
    
class ValorForm (forms.Form):
    livro = forms.ModelChoiceField(Valor.objects.all())
    valor = forms.FloatField()
    data = forms.DateField()

    def save (self, Livro):

        valor_novo = Valor(
            livro= Livro,
            valor=self.data['valor'],
            data=self.data['data'],
        )

        valor_novo.save()
        return valor_novo