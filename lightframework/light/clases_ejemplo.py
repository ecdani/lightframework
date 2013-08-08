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

# Etiquetas html:

class Link(Tag):
    """
    Definición genérica para todas las etiquetas tipo Link,
    en este caso todas son 'a' y llevan los Estilos genéricos para links
    # TODO, hacer el sistema inteligente, evitar repetir estilos (uff!)
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'a'
        self.styles.append(EstiloGenericoLinks())

class LinkGoogle(Link):
    """
    Ejemplo de etiqueta html (link a google)
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs['class'] = 'link_g'
        self.attrs['href'] = 'https://www.google.es/'
        self.inner.append(Tag('span','G'))
        self.inner.append(Tag('span','o'))
        self.inner.append(Tag('span','o'))
        self.inner.append(Tag('span','g'))
        self.inner.append(Tag('span','l'))
        self.inner.append(Tag('span','e'))
        self.styles.append(EstiloLinkGoogle())

# Estilos css:

class EstiloLinkGoogle(Styles):
    """
    Ejemplo contenedor de estilos (colores del link del google)
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.append(Style('.link_g span:nth-child(1)',Color='#3369E8'))
        self.append(Style('.link_g span:nth-child(2)',Color='#D50F25'))
        self.append(Style('.link_g span:nth-child(3)',Color='#EEB211'))

        self.append(EstiloLetrasGoogle(' span:nth-child(4)',Color='#3369E8'))
        self.append(EstiloLetrasGoogle(' span:nth-child(5)',Color='#009925'))
        self.append(EstiloLetrasGoogle(' span:nth-child(6)',Color='#D50F25'))
        
class EstiloLetrasGoogle(Style):
    """
    Ejemplo de estilo css (Estilo compartido para las letras)
    En este caso apenas si se comparte parte del selector para las letras
    (sólo lo uso las 3 últimas, aunque se puede aplicar a todas)
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sel = '.link_g' + self.sel

class EstiloGenericoLinks(Style):
    """
    Clase con todas las propiedades para enlaces
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sel = 'a'
        self.rules['font-family'] = 'Georgia'
        self.rules['font-size'] = '60px'
        self.rules['margin'] = '200px auto'
        self.rules['width'] = '600px'
        self.rules['height'] = '200px'
        self.rules['text-align'] = '100px'
        self.rules['text-shadow'] = '0px 3px 3px rgba(0,0,0,0.25)'
        
class EstiloLinkYahoo(EstiloGenericoLinks):
    """
    Ejemplo de herencia de estilos (comparten propiedades)
    Hereda los estilos de 'EstiloGenericoLinks' pero cambia el selector y añade
    otra regla
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sel = '.link_g:nth-child(2)' + self.sel
        self.rules['color'] = 'purple'