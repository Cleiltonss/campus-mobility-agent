from pathlib import Path

from arquivo in Path("documentos/regras_fretados").glob("*.md"):
    nome = arquivo.stem
    conteudo = arquivo.read_text(enconding="utf-8")

def monta_texto(nome, conteudo):
    for
    return cortar_documento(nome, conteudo)

def cortar_documento(documento, TEXTO):
    texto_cortado = TEXTO.split("##") # array com 3 dimensões
    resultado = []
    for i in range(len(texto_cortado)):
        if i > 0:
            texto_cortado[i] = "##" + texto_cortado[i] 
        resultado.append({"documento": documento, "texto": texto_cortado[i]})    
    return resultado    


