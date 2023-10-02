import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

URL_SITE_NOTICIAS = os.environ.get("URL_SITE_NOTICIAS")
URL_SITE_BASE = os.environ.get("URL_SITE_BASE")
TITULO = os.environ.get("TITULO")
DESCRICAO = os.environ.get("DESCRICAO")
IDIOMA = os.environ.get("IDIOMA")