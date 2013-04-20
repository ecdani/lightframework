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
        self.tags.append(BaseHtml())

class Page2(Page):
    def __init__(self,*args,**kwargs):
        super(Page2,self).__init__(*args, **kwargs)

class BaseHtml(Tag):
    def __init__(self,*args,**kwargs):
        super(BaseHtml,self).__init__(*args, **kwargs)
        self.name = 'html'
        self.inner.append(Tag('head'))
        self.inner.append(Tag('body'))

class BaseHtml2(BaseHtml):
    def __init__(self,*args,**kwargs):
        super(BaseHtml2,self).__init__(*args, **kwargs)
        self.inner.insert(0, Tag('head2'))
        self.inner.insert(1, Tag('body2'))
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
