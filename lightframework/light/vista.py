# -*- coding: utf-8 -*-
'''
Created on 30/03/2013

@author: Dani
'''

class UTag(object):
    def __init__(self, *args, **kwargs):
        for i, v in enumerate(args):
            if i == 0:
                self.nombre = v
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
        output =  '< ' + self.nombre + self.render_attrs() + '/>'

class Tag(UTag):
    def __init__(self, *args, **kwargs):
        super(Tag,self).__init__(*args, **kwargs)
        self.inner = {}
    def render(self):
        output = '<' + self.nombre + self.render_attrs() + '>'
        for key, value in self.inner.items():
            if type(value) is not str:
                output += value.render()
            else:
                output += value
        output += '</' + self.nombre + '>'
        return output

class myGoogleLink (Tag):
    def __init__(self, *args, **kwargs):
        super(myGoogleLink,self).__init__(*args, **kwargs)
        self.nombre = 'a'
        self.attrs['class'] = 'my_button_of_google'
        self.attrs['href'] = 'https://www.google.es/'
        self.inner['text'] = 'Direct link to Google'
