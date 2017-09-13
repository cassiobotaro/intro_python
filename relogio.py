#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Créditos: Luciano Ramalho
import time
import tkinter

app = tkinter.Tk()
app.title('Meu primeiro relógio')
hora = tkinter.Label(app, font='Helvetica 120')
hora['text'] = '00:00:00'
hora.pack()


def tic_tac():
    'Atualiza o relógio com a hora do Sistema Operacional'
    hora['text'] = time.strftime('%H:%M:%S')
    hora.after(1000, tic_tac)  # 1 em 1 segundo


tic_tac()
app.mainloop()
