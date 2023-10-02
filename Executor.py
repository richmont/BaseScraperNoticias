from Scraper import Scraper
from GeradorRSS import GeradorRSS
from conf.configuracoes import URL_SITE_BASE, URL_SITE_NOTICIAS, IDIOMA, DESCRICAO, TITULO




if __name__ == "__main__":


    scraper  = Scraper(URL_SITE_NOTICIAS)
    dict_channel = {"titulo": TITULO, "link": URL_SITE_NOTICIAS, "descricao": DESCRICAO, "idioma": IDIOMA}
    rss = GeradorRSS(dict_channel)
    for x in scraper.lista_ultimas_noticias:
        rss.adicionar_item(x)
    rss.gravar_xml("docs/rss.xml")