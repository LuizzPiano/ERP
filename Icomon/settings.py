

from pathlib import Path
import os



BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'paginas.apps.PaginasConfig',
    'usuarios.apps.UsuariosConfig',
    'cadastros.apps.CadastrosConfig',
    'django_cleanup.apps.CleanupConfig',
    'crispy_forms',
    'crispy_bootstrap4',
    'escalas',
   
 
    
    
]

# Crispy Forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Icomon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Icomon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
    
#     }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


<<<<<<< HEAD
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'icomonerp',
        'USER': 'admin',
        'PASSWORD': 'asdwasdw123',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
        'charset': 'utf8mb4',
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'icomonerp',
#         'USER': 'admin',
#         'PASSWORD': 'asdwasdw123',
#         'HOST': 'localhost',
#         'PORT': '3306',
        
#     }
# }


MYSQL_URL = 'mysql://root:hpGGwSmzkleLR9XYg4YZ@containers-us-west-102.railway.app:7125/railway'
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
=======
>>>>>>> b7d80aef4eb141fc96d396a6a191219fb0cfbb02

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Arquivos de Media/upload
MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")
MEDIA_URL = "/uploads/"

# Configurações de Autenticação
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL = 'login'


# Updade do Django 2 para 3
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'



JAZZMIN_SETTINGS = {
    
    "site_title": "Icomon",
    "site_header": "Icomon",
    "site_brand": "Icomon",
    "welcome_sign": "Seja bem vindo ao ERP Icomon",
    "copyright": "Icomon",

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "auth.Perfils": "fas fa-users",  
        },

}

