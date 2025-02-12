from django.db import models

class Livro(models.Model):
    id = models.AutoField(primary_key=True)
    livro = models.CharField(max_length=100)
    paginas = models.IntegerField()
    autor = models.CharField(max_length=75)
    data = models.DateField()
    foto = models.ImageField(upload_to = 'static/livro', blank=True, null=True)
    
    def __str__(self):
        return self.livro

class Valor(models.Model):
    id = models.AutoField(primary_key=True)
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name='valor_livro')
    valor = models.FloatField()
    data = models.DateField()