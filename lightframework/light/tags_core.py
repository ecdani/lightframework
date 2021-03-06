# -*- coding: utf-8 -*-
"""
Created on 30/03/2013
Clases base para etiquetas html y css
@author: Dani
"""

class Styles(list):
    """
    Contenedor de estilos css
    """
    def __str__(self):
        output = ''
        for key, value in enumerate(self):
            output += str(value)
        return output

class Style():
    """
    Estilo css { };
    TODO: Tal vez debería heredar de diccionario
    """
    def __init__(self, *args, **kwargs):
        self.sel = ''
        try:
            self.sel = args[0]
        except IndexError:
            pass
        self.rules = kwargs
    def __str__(self):
        output = ''
        output += self.sel + '{'
        for (key, value) in self.rules.items():
            output += key.lower() + ':' + value + ';'
        output += '}'
        return output

class Tags(list):
    """
    Contenedor de etiquetas html
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.styles = Styles()
    
    def get_styles(self):
        output = Styles()
        output.append(self.styles)
        for key, value in enumerate(self):
            output.append(value.get_styles())
        return output

    def render_styles(self):
        output = str(self.styles)
        for key, value in enumerate(self):
            output += value.render_styles()
        return output
    def __str__(self):
        output = ''
        for key, value in enumerate(self):
            output += str(value)
        return output

class UTag():
    """
    Etiqueta autocontenida html < />
    """
    def __init__(self, *args, **kwargs):
        try:
            self.name = args[0]
        except IndexError:
            pass
        self.attrs = kwargs
        self.styles = Styles()
    
    def get_styles(self):
        return self.styles

    def render_styles(self):
        return str(self.styles)

    def render_attrs(self):
        output = ''
        for (key, value) in self.attrs.items():
            output += ' ' + key.lower() + '='
            if not isinstance(value, str):
                output += value
            else:
                output += '"' + value + '"'
        return output
    def __str__(self):
        return '<' + self.name + self.render_attrs() + '/>'

class Tag(UTag,list):
    """
    Etiqueta normal html < > </ >
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.inner = []
        try:
            self.append(args[1])
        except IndexError:
            pass

    def get_styles(self):
        output = Styles()
        output.append(self.styles)
        for key, value in enumerate(self):
            if not isinstance(value, str):
                output.append(value.get_styles())     
        return output
    
    def render_styles(self):
        output = str(self.styles)
        for key, value in enumerate(self):
            output += value.render_styles()
        return output

    def __str__(self):
        output = '<' + self.name + self.render_attrs() + '>'
        for key, value in enumerate(self):
                output += str(value)
        output += '</' + self.name + '>'
        return output

class Doctype():
    """
    Etiqueta <!DOCTYPE >
    """
    def __init__(self,inner=None):
        if inner is None:
            self.inner = 'html'
        else:
            self.inner = inner
            
    def get_styles(self): #TODO: Si esta mierda no se puede esquivar, estudiar la posibilidad de una interfaz
        return Styles()

    def render_styles(self):
        return ''

    def __str__(self):
        return '<!DOCTYPE ' + self.inner + '>'
