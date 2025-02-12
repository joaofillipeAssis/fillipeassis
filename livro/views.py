from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from livro.models import Livro, Valor
from livro.forms import LivroForm, ValorForm

def livros(request):
    livros = Livro.objects.all().order_by('livro')
    return render(request, 'livros.html', {'livros': livros} )

def valores(request, id):
    livro = get_object_or_404(Livro, pk=id)
    valores = Valor.objects.filter(livro=livro.id).order_by('-data')
    return render(request, 'valores.html', {'valores': valores, 'livro': livro})

def salvar_livro(request):
    if request.method == 'GET':
        return render(request, 'salvar_livro.html')
    
    elif request.method == 'POST':
        livoForm = LivroForm(request.POST, request.FILES)
        livoForm.save()
        return redirect('livros')
    
def salvar_valor(request, id):
    livro = get_object_or_404(Livro, pk=id)

    if request.method == 'GET':
        return render(request, 'salvar_valor.html', {'livro': livro})
    
    elif request.method == 'POST':
        valorForm = ValorForm(request.POST)
        valorForm.save(livro)
        return redirect('valores', livro.id)