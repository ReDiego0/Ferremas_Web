from django import template

register = template.Library()

@register.filter()
def clp(value):
    try:
        value = int(round(float(value)))
        return f"${value:,}".replace(",", ".")
    except (ValueError, TypeError):
        return value
