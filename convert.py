#! -*- coding: utf-8 -*-

'''
Passo-a-passo (resumidamente)

1) Recebe os arquivos.

2) Faz um copia do arquivo para .rar/.tar/.zip

3) Copia para uma pasta os arquivos do item 2.

4) Extrai o arquivo .rar/.tar.

5) Insira cada imagem no file .pdf

6) acaba o programa.

'''

# IMPORTS
from pathlib import Path
from os import path as path_os
from os import listdir, sep
from rarfile import RarFile
from tarfile import TarFile
from zipfile import ZipFile
from shutil import move, rmtree, copyfile
# from reportlab.pdfgen import canvas
from glob import glob
# from PIL import Image


from pdb import set_trace

_ext = {'.cbr':'r.rar',
        '.cbt':'t.tar',
        '.cbz':'z.zip'}

_obj = {'.rar': RarFile,
        '.tar': TarFile,
        '.zip': ZipFile}

path_main = str(Path.cwd()) + sep + 'Conv' # path principal


def caminho_abs(arquivo):
    '''Obtem o caminho absoluto do arquivo.'''
    return str(Path(arquivo).absolute())

def obter_nome_arquivo(arquivo):
    '''Obtem o nome do arquivo'''

    return path_os.basename(arquivo)

def quebrar_arquivo(arquivo):
    '''Retorna o nome e a extensao do arquivo.'''

    return path_os.splitext(arquivo)

def criar_novo_nome(stem, suffix):
    '''cria um novo nome para o arquivo.'''
    return path_main + sep + stem + _ext.get(suffix)

def criar_pasta(pasta, nome):
    local = pasta + sep + nome
    Path(local).mkdir()

    return local

def renomear_arquivo(arquivo):
    '''renomeia os arquivos.'''

    #quebra o arquivo em nome e extensao
    nome_arquivo, ext_arquivo = quebrar_arquivo(arquivo)
    #cria um novo nome do arquivo
    novo_nome = criar_novo_nome(nome_arquivo, ext_arquivo)
    #renomeia o arquivo e ja o leva para outro diretorio
    copyfile(arquivo, novo_nome)

    return novo_nome

def extrair_arquivo(arquivo):
    '''Extrai o arquivo compactado.'''

    # pegando a extensao
    nome_arquivo, ext_arquivo = quebrar_arquivo(arquivo)
    # nome do arquivos sem as pastas
    nome_arquivo = path_os.basename(nome_arquivo)
    # cria uma nova pasta     
    pasta_referente = criar_pasta(path_main, nome_arquivo)
    # obtendo o objeto referenciando o arquivo
    obj_extract = _obj.get(ext_arquivo)
    # extrair arquivo
    obj_extract(arquivo).extractall(pasta_referente)

    return pasta_referente

def procurar_imagens(pasta):
    '''Procura por imagens.'''

    ext_imagens = ['.jpg', '.png', '.jpeg']
    for imagem in ext_imagens:
        # set_trace()
        img = glob(f"{pasta + sep}*{imagem}")
        if(img != []):
            yield img


if __name__ == '__main__':
    try:
        rmtree('Conv')
    except FileNotFoundError as error:
        Path(path_main).mkdir()
    else:
        Path(path_main).mkdir()

#     Converter('pablo.cbz', 'pablo.cbr')