#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request

app = Flask('Ola web')
lista_comentarios = []


@app.route('/')
def principal():
    return 'Olá Mundo'


@app.route('/ola/<nome>')
def ola(nome):
    return f'Olá {nome}!'


@app.route('/comentarios', methods=['GET', 'POST'])
def como_estou_palestrando():
    if request.method == 'POST':
        lista_comentarios.append(request.form['comentario'])
    comentarios = '<br>'.join(lista_comentarios)
    return f'''
    {comentarios}
    <form action="" method="post">
        <p><input type=text name=comentario>
    </form>
    '''
