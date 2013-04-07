# -*- coding: utf-8 -*-
"""
Created on 30/03/2013

@author: Dani
"""

class Styles(object):
    def __init__(self):
        self.styles = []
    def render(self):
        output = ''
        for key, value in enumerate(self.styles):
            output += value.render()
        return output

class Style(object):
    def __init__(self, *args, **kwargs):
        for i, v in enumerate(args):
            if i == 0:
                self.sel = v
        self.rules = kwargs
    def render(self):
        output = ''
        output += self.sel + '{'
        for (key, value) in self.rules.items():
            output += key.lower() + ':' + value + ';'
        output += '}'
        return output

class UTag(object):
    def __init__(self, *args, **kwargs):
        for i, v in enumerate(args):
            if i == 0:
                self.name = v
        self.attrs = kwargs
    def render_attrs(self):
        output = ' '
        for (key, value) in self.attrs.items():
            if not isinstance(value, str):
                output += key.lower() + '=' + value
            else:
                output += key.lower() + '="' + value + '"'
        return output
    def render(self):
        output =  '< ' + self.name + self.render_attrs() + '/>'

class Tag(UTag):
    def __init__(self, *args, **kwargs):
        super(Tag,self).__init__(*args, **kwargs)
        self.inner = []
    def render(self):
        output = '<' + self.name + self.render_attrs() + '>'
        for key, value in enumerate(self.inner):
            if type(value) is not str:
                output += value.render()
            else:
                output += value
        output += '</' + self.name + '>'
        return output
