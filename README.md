# django-jinja2-globals

##### Django Jinja2 Globals is a way to register all the global functions you need in your templates to do perform Python operations inside your templates.


After Initializing templates configuration in project's settings.py

    TEMPLATES = [
    {
        'BACKEND': 'django_jinja.backend.Jinja2',
        "DIRS": ["PROJECT_ROOT_DIRECTORY", "..."],
        'APP_DIRS': True,
        'OPTIONS': {
            'match_extension': '.html',
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
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


Create a file `app_template_globals.py` in your project's main directory and write all your global functions inside that file which you will need in your templates.

Create a dict and put all the function signature inside that dict:

    _template_globals = {}
	for object_name in dir(app_template_globals):
    _obj = getattr(app_template_globals, object_name)
    if callable(_obj) and not object_name.startswith('__'):
        _template_globals[object_name] = _obj.__module__ + '.' + _obj.__qualname__


Once the `_template_globals` dict is prepared update the Actual `TEMPLATES` globals:

    TEMPLATES[0]['OPTIONS']['globals'].update(_template_globals)

#### And you're done, now you can use all the global functions inside your templates by just calling them like python functions.
#### In the same manner you can register jinja2 constants and jinja2 filters. Enjoy :)
