# -*- coding: utf-8 -*-
"""
Created on 30/03/2013

@author: Dani
"""

from base import Tag, Style, Styles
from extended import myNestedSpanStyle,myGoogleLink,myLinkStyle
import sys

def main():
    print myGoogleLink().render()
    tag = Tag('a', Href="https://www.google.es/",  Class="my_button_of_google") # Class pertenece a la lógica frontend
    tag.inner.append("Direct link to Google")

    print tag.render()
    
    styles = Styles()
    styles.styles.append(myNestedSpanStyle())
    styles.styles.append(myLinkStyle())
    
    
    style = Tag('style')
    style.inner.append(myNestedSpanStyle())
    print styles.render()


if __name__ == '__main__':
    sys.exit(main())