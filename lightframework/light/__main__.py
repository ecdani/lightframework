# -*- coding: utf-8 -*-
"""
Created on 30/03/2013
Tests y ejemplos de uso
@author: Dani
"""

from base import Tag, Style, Styles, Tags
from extended import MyNestedSpanStyle,MyGoogleLink,MyLinkStyle, Page
import sys
from light.extended import BaseHtml2

def main():
    # TODO Facilitar el acceso a elementos anidados. o facilidad para anidar.
    
    # Creo y renderizo una página html base.
    #page = Page()
    #print Page()
    
    #page.tags.insert(0, BaseHtml2())
    #page.tags[0].inner.append(Tag('title').inner.append('El título'))
    #obj = page.get(0,0,0)
    #print obj
    
    lista = Tags([Tags([Tag('title'),Tag('title'),Tag('title')]),Tag('title'),Tag('title')])
    
    print lista[0][0]
    
    # Renderizo un link predefinido
    #print MyGoogleLink()
    
    # Creo un link nuevo, igual que el anterior, pero al vuelo (sin predefinir) y lo renderizo
    tag = Tag('a', Href="https://www.google.es/",  Class="my_button_of_google")
    tag.inner.append("Direct link to Google")

    # print tag
    
    # Creo un contenedor de estilos, y añado dos estilos predefinidos
    styles = Styles()
    styles.styles.append(MyNestedSpanStyle())
    styles.styles.append(MyLinkStyle())

    # Creo una etiqueta <style></style>, meto los estilos dentro y renderizo
    styles_tag = Tag('style')
    styles_tag.inner.append(MyNestedSpanStyle())
    # print styles


if __name__ == '__main__':
    sys.exit(main())