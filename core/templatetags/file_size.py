from django import template

register = template.Library()

@register.filter
def filesizeformat(value):
    if not value:
        return "0 Bytes"
    bytes = float(value)
    if bytes < 1024:
        return f"{bytes:.0f} Bytes"
    elif bytes < 1048576:
        kilobytes = bytes / 1024
        return f"{kilobytes:.0f} KB"
    elif bytes < 1073741824:
        megabytes = bytes / 1048576
        return f"{megabytes:.1f} MB"
    else:
        gigabytes = bytes / 1073741824
        return f"{gigabytes:.1f} GB"
