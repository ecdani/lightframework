# -*- coding: utf-8 -*-
"""
Created on 30/03/2013
Tests y ejemplos de uso
@author: Dani
"""

from base import Tag, Style, Styles
from extended import MyNestedSpanStyle,MyGoogleLink,MyLinkStyle, Page
import sys

def main():
    # TODO Facilitar el acceso a elementos anidados. o facilidad para anidar.
    
    # Creo y renderizo una página html base.
    page = Page()
    print page.render()
    
    # Renderizo un link predefinido
    print MyGoogleLink().render()
    
    # Creo un link nuevo, igual que el anterior, pero al vuelo (sin predefinir) y lo renderizo
    tag = Tag('a', Href="https://www.google.es/",  Class="my_button_of_google")
    tag.inner.append("Direct link to Google")

    print tag.render()
    
    # Creo un contenedor de estilos, y añado dos estilos predefinidos
    styles = Styles()
    styles.styles.append(MyNestedSpanStyle())
    styles.styles.append(MyLinkStyle())
    
    # Creo una etiqueta <style></style>, meto los estilos dentro y renderizo
    styles_tag = Tag('style')
    styles_tag.inner.append(MyNestedSpanStyle())
    print styles.render()


if __name__ == '__main__':
    sys.exit(main())