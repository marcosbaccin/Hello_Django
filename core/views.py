from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))

def soma(request, valor1, valor2):
    soma = valor1 + valor2
    return HttpResponse('{} + {} = {}'.format(valor1, valor2, soma))

def subtracao(request, valor1, valor2):
    subtracao = valor1 - valor2
    return HttpResponse('{} - {} = {}'.format(valor1, valor2, subtracao))

def multiplicacao(request, valor1, valor2):
    multiplicacao = valor1 * valor2
    return HttpResponse('{} * {} = {}'.format(valor1, valor2, multiplicacao))

def divisao(request, valor1, valor2):
    divisao = valor1 / valor2
    return HttpResponse('{} / {} = {}'.format(valor1, valor2, divisao))
