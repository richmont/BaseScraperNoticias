import urllib3
import requests
import logging
from .Noticia import Noticia

logger_scraper = logging.getLogger("Scraper")
logging.basicConfig(level=logging.DEBUG)
# desliga mensagens repetitivas a cada conexão
logger_urllib = logging.getLogger('urllib3.connectionpool')
logger_urllib.setLevel(logging.ERROR)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Scraper():
    def __init__(self, url: str) -> None:
        """Obtém e extrai informações da página de notícias

        Args:
            url (str): Endereço da página a ser extraída
        """
        self._url = url
        logger_scraper.debug("url recebido: %s", self._url)
        self._pagina_completa = self.obter_pagina()
    
    def obter_pagina(self) -> str:
        """Recebe o HTML bruto da página

        Raises:
            errors.URL_invalido: URL não possui "http"
            errors.URL_invalido: Falha de conexão

        Returns:
            str: html completo da página
        """
        try:
            pagina_completa = requests.get(self._url, verify=False)
            
            if pagina_completa.status_code == 200:
                logger_scraper.debug("Status  200, retornando texto da página recebida")
                return pagina_completa.text
            else:
                logger_scraper.error("Código de status: %s", pagina_completa.status_code)
        except requests.exceptions.MissingSchema:
            raise errors.URL_invalido("URL inválido, verifique arquivo .env")
        except requests.exceptions.ConnectionError:
            raise errors.FalhaConexao("Conexão com o URL malsucedida, verifique arquivo .env")

    def parse_pagina_lista_noticias(self) -> list:
        """Interpreta o HTML bruto para localizar informações de cada notícia na página

        Returns:
            list: lista de elementos do tipo Noticia
        """
        pass

    def parse_conteudo_noticia(self, url_noticia: str) -> Noticia:
        """Extrai o conteúdo em forma de HTML de uma notícia

        Args:
            url_noticia (str): endereço direto da notícia

        Returns:
            Noticia: objeto Noticia com conteúdo de uma única notícia
        """
        pass
  
            
                
    
class errors():
    class URL_invalido(Exception):
        pass

    class FalhaConexao(Exception):
        pass
