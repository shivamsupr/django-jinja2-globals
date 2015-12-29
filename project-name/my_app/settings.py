# Snippets from Actual Settings.py

TEMPLATES = [
    {
        'BACKEND': 'django_jinja.backend.Jinja2',
        "DIRS": "PROJECT_ROOT_DIRECTORY",
        'APP_DIRS': True,
        'OPTIONS': {
            'match_extension': '.html',
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz'
            ],
            'globals': {
            },
            'extensions': DEFAULT_EXTENSIONS + [
                'pipeline.templatetags.ext.PipelineExtension',
            ],
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True
    },
]

# Auto Register Template Globals
_template_globals = {}
for object_name in dir(app_template_globals):
    _obj = getattr(app_template_globals, object_name)
    if callable(_obj) and not object_name.startswith('__'):
        _template_globals[object_name] = _obj.__module__ + '.' + _obj.__qualname__
TEMPLATES[0]['OPTIONS']['globals'].update(_template_globals)
