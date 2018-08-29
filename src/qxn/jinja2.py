from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment




def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    # more options if DEBUG is disabled
    # options['auto_reload'] = settings.DEBUG
    if not env.auto_reload:
        env.trim_blocks = True
        env.lstrip_blocks = True
    return env
