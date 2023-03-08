import re
class Extrator_url:

    def __init__(self, url):
        self.url = self.sanatiza_url(url)
        self.validacao_url()

    def sanatiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def validacao_url(self):
        if not self.url:
            raise ValueError("A url está vazia!")

        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A url é inválida!")

    def extrair_url_base(self):
        indice_url_base = self.url.find('?')
        url_base = self.url[:indice_url_base + 1]
        return url_base

    def url_parametros(self):
        indice_url_base = self.url.find('?')
        url_parametros = self.url[indice_url_base + 1:]
        return url_parametros

    def buscar_parametro(self, url_parametros):
        indice_parametro = self.url_parametros().find(url_parametros)
        indice_valor = indice_parametro + len(url_parametros) + 1
        indice_e_comercial = self.url_parametros().find('&', indice_valor)

        if indice_e_comercial == -1:
            valor = self.url_parametros()[indice_valor:]
        else:
            valor = self.url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

extrator_url = Extrator_url("bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100")
moeda_destino = extrator_url.buscar_parametro('moedaDestino')
moeda_origem = extrator_url.buscar_parametro('moedaOrigem')
quantidade = extrator_url.buscar_parametro('quantidade')
print(Extrator_url.__len__(extrator_url))
quantidade = int(quantidade)

cotacao = float(input("Qual a cotacao da moeda destino em relacao a moeda origem?"))
print("Moeda destino =" + moeda_destino)
print("Moeda Origem =" +moeda_origem)
print(f"Quantidade ={quantidade}")
conversao = (cotacao * quantidade)
print(conversao)




