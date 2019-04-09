from django import template

register = template.Library()

@register.filter(name='cuttt')
def cuttt(value, arg):
    """
        this function takes in value as input and argument, then cuts it
    """

    return value.replace(arg, '')
