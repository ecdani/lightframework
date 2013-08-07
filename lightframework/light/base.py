# -*- coding: utf-8 -*-
"""
Created on 30/03/2013
Clases base para etiquetas html y css
@author: Dani
"""

class Styles():
    """
    Contenedor de estilos css
    """
    def __init__(self):
        self.styles = []
    def __str__(self):
        output = ''
        for key, value in enumerate(self.styles):
            output += str(value)
        return output

class Style():
    """
    Estilo css { };
    """
    def __init__(self, *args, **kwargs):
        '''for i, v in enumerate(args):
            if i == 0:
                self.sel = v'''
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
    '''def __init__(self):
        self.tags = []
    def get(self,*args,**kwargs):
        for i, v in enumerate(args):
            if i == 0:
                pass
            #obj = self.tags[v]
            #obj = obj.get(v, *args, **kwargs)
        return obj'''
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
    def render_attrs(self):
        output = ' '
        for (key, value) in self.attrs.items():
            output += key.lower() + '='
            if not isinstance(value, str):
                output += value
            else:
                output += '"' + value + '"'
        return output
    def __str__(self):
        return '< ' + self.name + self.render_attrs() + '/>'

class Tag(UTag):
    """
    Etiqueta normal html < > </ >
    """
    def __init__(self, *args, **kwargs):
        super(Tag,self).__init__(*args, **kwargs)
        self.inner = []
        try: # get(key[, default])
            self.inner.append(args[1])
        except IndexError:
            pass
    '''def get(self,*args,**kwargs):
        for i, v in enumerate(args):
            if i == 0:
                obj = self.inner[v]
            obj = obj.get(v)
        return obj'''
    def __str__(self):
        output = '<' + self.name + self.render_attrs() + '>'
        for key, value in enumerate(self.inner):
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
    def __str__(self):
        return '<!DOCTYPE ' + self.inner + '>'


