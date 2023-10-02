from lxml import etree
from beartype import beartype

class GeradorRSS():
    def __init__(self, dict_channel: dict) -> None:
        """
        Gerador de documento XML a partir de notícias
        Parâmetro: dict_channel (dict)
        Elementos do dicionário:
            titulo
            descricao
            link
            idioma
        """
        self.dict_channel = dict_channel
        self.tag_base_rss = etree.Element('rss',version="2.0")        
        self.documento = etree.ElementTree(self.tag_base_rss)        
        self.channel_tag = self.construir_channel()

    def construir_channel(self) -> etree._Element:
        """
        Constrói a tag channel, serve de base para tags item\n
        Contém informações do canal de notícias\n
        Preenchido com dados do dict_channel\n

        Retorna: (etree._Element)
        """
        channel_tag = etree.SubElement(self.tag_base_rss, "channel")

        titulo = etree.SubElement(channel_tag, "title")
        link = etree.SubElement(channel_tag, "link")
        descricao = etree.SubElement(channel_tag, "description")
        idioma = etree.SubElement(channel_tag, "language")

        titulo.text = self.dict_channel["titulo"]
        link.text = self.dict_channel["link"]
        descricao.text = self.dict_channel["descricao"]
        idioma.text = self.dict_channel["idioma"]

        return channel_tag
    
    def adicionar_item(self, noticia: object) -> etree._Element:
        """
        Adiciona um elemento item com notícia na tag channel de base
        Parâmetro: dict_item (dict)\n
        Elementos do dicionário:\n
            titulo\n
            descricao\n
            link\n
            data
        """
        
        item = etree.SubElement(self.channel_tag, "item")

        titulo = etree.SubElement(item, "title")
        link = etree.SubElement(item, "link")
        descricao = etree.SubElement(item, "description")
        data = etree.SubElement(item, "pubDate")

        titulo.text = noticia.titulo
        link.text = noticia.url
        data.text = noticia.data
        # https://stackoverflow.com/questions/44549514/cdata-getting-stripped-in-lxml-even-after-using-strip-cdata-false
        descricao.text = etree.CDATA(noticia.chamada + "\n" + noticia.conteudo)
        return item
    
    def gravar_xml(self, nome_arquivo: str) -> None:
        """Grava em disco o arquivo XML do feed RSS resultante da raspagem

        Args:
            nome_arquivo (str): nome do arquivo a ser gravado
        """
        self.documento.write(
            nome_arquivo, 
            encoding='utf-8', 
            xml_declaration=True, 
            pretty_print=True
            )