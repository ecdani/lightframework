# -*- coding: utf-8 -*-
"""
Created on 30/03/2013

@author: Dani
"""

from vista import Tag, myGoogleLink
import sys

def main():
    print myGoogleLink().render()
    tag = Tag('a', Href="https://www.google.es/",  Class="my_button_of_google")
    tag.inner['text'] = "Direct link to Google"

    print tag.render()


if __name__ == '__main__':
    sys.exit(main())