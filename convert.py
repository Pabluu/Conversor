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
from rarfile import RarFile
from tarfile import TarFile
from zipfile import ZipFile
from shutil import move, rmtree
from pathlib import Path

from os import listdir, rename, chdir, getcwd, sep
from os import path as path_os

from reportlab.pdfgen import canvas
from glob import glob
from PIL import Image


from pdb import set_trace


class Converter(object):

    _ext = {'.cbr':'.rar',
            '.cbt':'.tar',
            '.cbz':'.zip',}

    _obj = {'.rar': RarFile,
            '.tar': TarFile,
            '.zip': ZipFile}


    def __init__(self, *files):
        
        # nome dos arquivos originais.
        self.files_orig = list(files)

        # nome dos arquivos pos renomeados.
        self.files_ren = []

        # local das imgs que serao inseridas.
        self.directorys = []

        # cria uma pasta.
        Path('Conv').mkdir()

        set_trace()

        self.ChangeName(self.files_orig)

        self.MoveFiles(self.files_ren)

        chdir("Conv")

        self.Extract(self.files_ren)

    def ChangeName(self, files):
        '''Muda o nome do arquivo conforme sua extenção.'''

        for file in files:
            try:
                # nome e extensao do arquivo.
                name_file, ext_file = path_os.splitext(file)

                new_name = name_file + self._ext[ext_file]    

                # renomeando o arquivo.
                rename(file, new_name)

                # os arquivos que foram renomeados
                # serao add a variavel
                self.files_ren.append(new_name)
            except:
                pass

        return True

    def MoveFiles(self, files):
        '''Muda os arquivos de um diretorio para outro(Conv).'''

        if files != []:
            for file in files:
                try:
                    move(file, "Conv")
                except Exception as er:
                    print(er)

        else:
            exit("Nenhum arquivo a ser descompactado")


    def Extract(self, file):
        '''Extrai todos os arquivos conforme sua extenção.'''

        for file in files:
            name_file, ext_file = path_os.splitext(file)

            #cria um diretorio para extracao
            self.MakeDir(name_file)

            # add todos os diretorios a uma variavel para quando for desenhar
            self.directorys.append(path_os.abspath(name_file))

            obj_extract = self._obj[ext_file]

            # obtendo o objeto(rar, tar ou zip)
            obj_extract = obj_extract(file)

            # extraindo o arquivo.
            obj_extract.extractall()

        return True

    def MakeDir(self, name):
        '''Funcao que cria um diretorio'''

        Path(name).mkdir()

        return True


    def Draw(self, path_imgs):
        '''Desenha as imagens no arquivo .pdf.'''

        #pdf.setPageSize(self.GetSize(img))


    # def GetSize(self, imagem):
    #     '''Retorna o tamanho da imagem(largura e altura).'''

    #     img = Image.open(imagem)
    #     return img.width, img.height


if __name__ == "__main__":
    try:
        rmtree('Conv')
    except FileNotFoundError:
        pass

    Converter('pablo.cbz', 'pablo.cbr')