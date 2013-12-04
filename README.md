lightframework
==============

Generador html/css experimental

Utiliza el propio lenguaje python para escribir html y css, permitiendo crear clases y objetos que son etiquetas o conjuntos de etiquetas, permitiendo utilizar los mecanismos de herencia y POO de python.

Supongamos una lista de enlaces, sacado de la web de Jinga:

```python
{% for user in users %}
    <li><a href="{{ user.url }}">{{ user.username }}</a></li>
{% endfor %}
```


Necesitamos "pasar" 2 variables y un bucle for, el documento necesita ser parseado y procesado por el engine.

La alternativa que intento es:

```
for user in users:
  tags.append(li(userlink(user.username, Href=user.url)))
```

A simple vista, no parece aportar mucho, sin embargo, podemos usar TODA la potencia de python, dado que ES python.

Supongamos otra página en nuestra web vamos a reutilizar nuestro userlink, que es una clase python; tan sencillo como invocarlo:

```
  userlink(user.username, Href=user.url)
```

Incluso, dado que es una clase definida por nosotros podriamos abreviarla:

```
  userlink(user)
```

Ésta podría ser nuestra clase:

```
class userlink(Tag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'a'
        self.append = args[0].username
        self.attrs = {'href': args[0].url}
```

Más complicado que:

```
<a href="{{ user.url }}">{{ user.username }}</a>
```

Pero infinitamente más reutilizable

También se pueden utilizar los mecanismos de herencia de python, un ejemplo, añadir el tratamiento a los nombres (Don / Doña)

```
class userlink_trat(userlink):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if args[0].sexo == 'V':
            list.insert(0,'Don.' + args[0].username)
        else
            list.insert(0,'Doña.' + args[0].username)
```
         
Ya podemos usar el link con tratamiento en cualquier parte sin miedo:

```
  userlink_trat(user)
```

Para poder hacer lo mismo en jinga habria que replicar lo siguiente en todos los lugares en que hiciera falta:

```
 {% if user.sexo == 'V' %}
   <a href="{{ user.url }}">Don.{{ user.username }}</a>
 {% else %}
   <a href="{{ user.url }}">Doña.{{ user.username }}</a>
 {% endif %}
```
