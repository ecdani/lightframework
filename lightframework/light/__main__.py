'''
Created on 30/03/2013

@author: Dani
'''

from vista import Tag, Link, Paragraph, Foo
import sys

def main():
    link = Link(href='http://www.facebook.es')
    link.inner['texto'] = "Enlace facebook"
    link.inner['otro enlace'] = Paragraph(href='http://www.google.es')
    #foo = Foo()
    #foo.foo_objects['key'] = Foo()
    print link.render()
    
if __name__ == '__main__':
    sys.exit(main())