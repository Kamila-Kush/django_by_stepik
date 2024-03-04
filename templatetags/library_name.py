from django import template
#  Этот файл наша библиотека тегов
register = template.Library()

# регистрация фильтра через декоратор
@register.filter(name="splitl")
def splitl_func(value: str):
    return value.replace("_", " ")

# для того чтобы можно было использовать в шаблоне пропишем
#    {% load <library_name> %}

# регистрация через метод класса
def splitlvl_func(value: str, rplv: str):
    return value.replace(rplv, " ")
register.filter("split_vl", splitlvl_func)

# {% load library_name %}
# <h1> Hello {{ some_value|split_vl:'/' }} </h1>
