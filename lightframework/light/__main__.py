
"""
Created on 30/03/2013
Tests y ejemplos de uso
@author: Dani
"""

from base import Tag, Styles, Tags
from extended import MyGoogleLettersStyles,MyGoogleLinkStyle,MyGenericLink,AnotherLink, MyGoogleLink,MyGoogleFont
import sys
#from light.extended import BaseHtml2
from wsgiref.simple_server import make_server

def main():
    # TODO Facilitar el acceso a elementos anidados. o facilidad para anidar.
    
    # Creo y renderizo una página html base.
    #page = Page()
    #print Page()
    
    #page.tags.insert(0, BaseHtml2())
    #page.tags[0].inner.append(Tag('title').inner.append('El título'))
    #obj = page.get(0,0,0)
    
    # Empiezo mi contenedor de etiquetas, con mi link de google prefabricado y
    # un br
    etiquetas = Tags([MyGoogleLink(),Tag('br')])
    
    # Creo un link nuevo, igual que el anterior, pero al vuelo (sin predefinir)
    tag = Tag('a', Href="http://www.es.yahoo.com/",  Class="my_button_of_google")
    tag.inner.append("Yahoo!")
    etiquetas.append(tag)
    
    # Creo un contenedor de estilos, añado otro contenedor y mas estilos
    # TODO, hacer que Styles herede de list igual que Tags
    styles = Styles()
    styles.styles.append(AnotherLink())
    styles.styles.append(MyGoogleFont())
    styles.styles.append(MyGoogleLettersStyles())
    styles.styles.append(MyGoogleLinkStyle())
    styles.styles.append(MyGenericLink())
    styles.styles.append(AnotherLink())
    

    # Creo una etiqueta <style></style>, meto los estilos dentro
    styles_tag = Tag('style')
    styles_tag.inner.append(styles)
    
    # Creo que también se podria haber hecho así:
    # styles_tag = Tag('style',str(styles))
    # O sin el str, si, sin el str mejor.
    
    # Añado la última etiqueta de estilos
    etiquetas.append(styles_tag)
    
    # Devuelvo al server en forma de string todo el HTML
    return  str(etiquetas)


def hello_world(environ, start_response):
    """
    Manejo de peticiones al servidor
    """
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [main().encode(encoding='utf_8')]
    
if __name__ == '__main__':
    srv = make_server('localhost', 8080, hello_world)
    srv.serve_forever()
    #sys.exit(main())
