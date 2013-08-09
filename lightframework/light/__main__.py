
"""
Created on 30/03/2013
Tests y ejemplos de uso
@author: Dani
"""

from tags_core import Tag, UTag, Tags
from clases_ejemplo import LinkGoogle, Page
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
    # un br, el accesso por indice puede resultar algo duro, hay que ver si hay 
    # otras maneras.
    etiquetas = Page()
    etiquetas[1][1].append(Tags([LinkGoogle(),UTag('br')]))
    
    # Creo un link nuevo, igual que el anterior, pero al vuelo (sin predefinir)
    tag = Tag('a', Href="http://www.es.yahoo.com/",  Class="link_g")
    tag.append("Yahoo!")
    etiquetas[1][1].append(tag)

    # Creo una etiqueta <style></style>, meto los estilos dentro
    styles_tag = Tag('style')
    styles_tag.append(etiquetas.get_styles())
    
    # Añado al head el título y los estilos
    etiquetas[1][0].append(Tag('title','Lightframework'))
    etiquetas[1][0].append(UTag('meta',Charset='UTF-8'))
    etiquetas[1][0].append(styles_tag)
    
    # También se puede escribir así:
    # etiquetas.append(Tag('style',etiquetas.get_styles()))
    
    # Devuelvo al server en forma de string todo el HTML
    return  str(etiquetas)


def dev_test_server_handler(environ, start_response):
    """
    Manejo de peticiones al servidor
    """
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [main().encode(encoding='utf_8')]
    
if __name__ == '__main__':
    srv = make_server('localhost', 8080, dev_test_server_handler)
    srv.serve_forever()
    #sys.exit(main())
