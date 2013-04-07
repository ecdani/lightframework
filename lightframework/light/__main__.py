# -*- coding: utf-8 -*-
"""
Created on 30/03/2013

@author: Dani
"""

from vista import Tag, myGoogleLink , Style
import sys

def main():
    print myGoogleLink().render()
    tag = Tag('a', Href="https://www.google.es/",  Class="my_button_of_google") # Class pertenece a la lógica frontend
    tag.inner.append("Direct link to Google")

    print tag.render()
    
    style = Tag('style')
    style.inner.append(Style('a', Color='pink'))
    print style.render()


if __name__ == '__main__':
    sys.exit(main())