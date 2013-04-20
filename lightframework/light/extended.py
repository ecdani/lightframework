# -*- coding: utf-8 -*-
"""
Created on 07/04/2013
Estilos predefinidos
@author: Dani
"""
from base import Tag, Tags, Style, Doctype

# Auxiliares:

class Page(Tags):
    def __init__(self,*args,**kwargs):
        super(Page,self).__init__(*args, **kwargs)
        self.tags.append(Doctype())
        self.tags.append(Tag('html'))
        self.tags[1].inner.append(Tag('head'))
        self.tags[1].inner.append(Tag('body'))

# Ejemplos:

class MyGoogleLink(Tag):
    """
    Ejemplo de etiqueta html (link a google)
    """
    def __init__(self, *args, **kwargs):
        super(MyGoogleLink,self).__init__(*args, **kwargs)
        self.name = 'a'
        self.attrs['class'] = 'my_button_of_google'
        self.attrs['href'] = 'https://www.google.es/'
        self.inner.append('Direct link to Google')
        
class MyLinkStyle(Style):
    """
    Ejemplo de estilo css (Estilos a link)
    """
    def __init__(self, *args, **kwargs):
        super(MyLinkStyle,self).__init__()
        self.sel = 'a'
        self.rules['color'] = 'darkgreen'
        self.rules['background-color'] = 'lightblue'

class MyNestedSpanStyle(MyLinkStyle):
    """
    Ejemplo de herencia de estilos (comparten propiedades)
    """
    def __init__(self, *args, **kwargs):
        super(MyNestedSpanStyle,self).__init__()
        self.sel += ' span'
        self.rules['color'] = 'red'
