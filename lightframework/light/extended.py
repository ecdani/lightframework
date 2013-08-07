# -*- coding: utf-8 -*-
"""
Created on 07/04/2013
Estilos predefinidos
@author: Dani
"""
from base import Tag, Tags, Style, Doctype, Styles

# Auxiliares: No se usan, son html genérico como el doctype y el body...


class Page(Tags):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.tags.append(Doctype())
        self.tags.append(BaseHtml())

class Page2(Page):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)

class BaseHtml(Tag):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'html'
        self.inner.append(Tag('head'))
        self.inner.append(Tag('body'))

class BaseHtml2(BaseHtml):
    """
    Un test para modificar BaseHtml
    """
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.inner.insert(0, Tag('head2'))
        self.inner.insert(1, Tag('body2'))
# Ejemplos:

class MyGoogleLink(Tag):
    """
    Ejemplo de etiqueta html (link a google)
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'a'
        self.attrs['class'] = 'my_button_of_google'
        self.attrs['href'] = 'https://www.google.es/'
        self.inner.append(Tag('span','G'))
        self.inner.append(Tag('span','o'))
        self.inner.append(Tag('span','o'))
        self.inner.append(Tag('span','g'))
        self.inner.append(Tag('span','l'))
        self.inner.append(Tag('span','e'))
        
class MyGoogleLettersStyles(Styles):
    """
    Ejemplo contenedor de estilos (colores del link del google)
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.styles.append(Style('.my_button_of_google span:nth-child(1)',Color='#3369E8'))
        self.styles.append(Style('.my_button_of_google span:nth-child(2)',Color='#D50F25'))
        self.styles.append(Style('.my_button_of_google span:nth-child(3)',Color='#EEB211'))

        self.styles.append(MyGoogleLinkStyle(' span:nth-child(4)',Color='#3369E8'))
        self.styles.append(MyGoogleLinkStyle(' span:nth-child(5)',Color='#009925'))
        self.styles.append(MyGoogleLinkStyle(' span:nth-child(6)',Color='#D50F25'))
        
class MyGoogleLinkStyle(Style):
    """
    Ejemplo de estilo css (Estilo genérico para letras)
    En este caso apenas si se comparte un selector para las letras
    (las 3 últimas, aunque se puede aplicar a todas)
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sel = '.my_button_of_google' + self.sel

class MyGoogleFont(MyGoogleLinkStyle):
    """
    Fuente de las letras de google, (no funciona aún)
    """
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.sel = '@font-face'
        self.rules['font-family'] = 'Catull'
        self.rules['src'] = 'url(font/catull.ttf)'
        self.rules['font-weight'] = '400px auto'

class MyGenericLink(MyGoogleLinkStyle):
    """
    Ejemplo de herencia de estilos
    Hereda el selector my_button_of_google, que también tiene el link de yahoo
    """
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.rules['font-family'] = 'Catull,Sans-Serif'
        self.rules['font-size'] = '60px'
        self.rules['margin'] = '200px auto'
        self.rules['width'] = '600px'
        self.rules['height'] = '200px'
        self.rules['text-align'] = '100px'
        self.rules['text-shadow'] = '0px 3px 3px rgba(0,0,0,0.25)'
        
class AnotherLink(MyGenericLink):
    """
    Ejemplo de herencia de estilos (comparten propiedades)
    Hereda la mayoría de estilos de 'MyGenericLink' y cambia el selector y una propiedad
    """
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.sel = '.my_button_of_google:nth-child(2)' + self.sel
        self.rules['background-color'] = 'grey'
