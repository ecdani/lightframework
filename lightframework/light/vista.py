'''
Created on 30/03/2013

@author: Dani
'''

class UTag:
    nombre = ''
    attrs = {}
    def render_attrs(self):
        output = ' '
        for (key, value) in self.attrs.items():
            if not isinstance(value, str):
                output += key + '=' + value
            else:
                output += key + '="' + value + '"'
        return output
    def render(self):
        output =  '<' + self.nombre + self.render_attrs() + '/>'
    def __init__(self, **kwargs):
        self.attrs['href'] = kwargs['href']

class Tag(UTag):
    def __init__(self):
        inner = {}
    def render(self):
        output = '<' + self.nombre + self.render_attrs() + '>'
        for key, value in self.inner.items():
            if type(value) is not str:
                output += value.render()
            else:
                output += value
        output += '</' + self.nombre + '>'
        return output
    
class Foo():

    def __init__(self):
            self.name = 'name'
            self.foo_objects = {}
    def print_name(self):
        output = self.name
        for key, value in self.foo_objects.items():
            output += value.print_name()
        return output
    
class Link (Tag):
    nombre = 'a'

class Paragraph (Tag):
    nombre = 'p'
