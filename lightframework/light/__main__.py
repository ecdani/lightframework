
"""
Created on 30/03/2013
Tests y ejemplos de uso
@author: Dani
"""

from tags_core import Tag, UTag, Tags
from clases_ejemplo import LinkGoogle, Page
import sys
from wsgiref.simple_server import make_server

def main():
    # Empiezo el contenedor html 'Page', que ya tiene lo básico de una página
    # y añado mi link de google prefabricado y un br
    pagina_web = Page()
    body = pagina_web[1][1] # Me traigo el body, para trabajar comodamente
    body.append(Tags([LinkGoogle(),UTag('br')]))
    
    # Creo un link nuevo, igual que el anterior, pero al vuelo (sin predefinir)
    tag = Tag('a', Href="http://www.es.yahoo.com/",  Class="link_g")
    tag.append("Yahoo!")
    body.append(tag)

    # Creo una etiqueta <style></style>, meto los estilos dentro
    styles_tag = Tag('style')
    styles_tag.append(pagina_web.get_styles())
    
    # También se puede escribir así:
    # pagina_web[1][0].append(Tag('style',etiquetas.get_styles()))
    
    # Añado al head el título y los estilos
    pagina_web[1][0].append(Tag('title','Lightframework'))
    pagina_web[1][0].append(UTag('meta',Charset='UTF-8'))
    pagina_web[1][0].append(styles_tag)
    
    # Devuelvo al server en forma de string todo el HTML
    return  str(pagina_web)

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
