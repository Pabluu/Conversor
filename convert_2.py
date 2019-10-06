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

# from reportlab.pdfgen import canvas
# from glob import glob
# from PIL import Image


from pdb import set_trace



class Converter(object):

    _ext = {'.cbr':'r.rar',
            '.cbt':'t.tar',
            '.cbz':'z.zip'}

    _obj = {'.rar': RarFile,
            '.tar': TarFile,
            '.zip': ZipFile}


    def __init__(self, *files):
        
        # nome dos arquivos originais.
        self.files_orig = [ str(Path(file).absolute()) for file in files ]

        # nome dos arquivos pos renomeados.
        self.files_ren = []

        # local das imgs que serao inseridas.
        self.directorys = []

        # Local onde sera extraidos os arquivos
        self.local_extract = str(Path().cwd()) + sep + 'Conv' + sep

        # cria uma pasta.
        Path(self.local_extract).mkdir()

        set_trace()

        self.Main()

        # chdir("Conv") #talvez nn irá funcionar

        # self.Extract(self.files_ren) # arrumar... irá usar o for


    def Main(self):
        try:
            self.Rename(self.files_orig)

            self.Extract(self.files_ren)

        except Exception as error:
            pass #depois vejo melhor

        return True


    def Rename(self, files):
        '''Renomeia o arquivo conforme sua extenção.'''

        for file in files:
            # nome e extensao do arquivo.
            file = path_os.basename(file)
            name_file, ext_file = path_os.splitext(file)

            # juntando o nome do arquivo e a extensao .
            new_name = name_file + self._ext.get(ext_file)

            local_path = self.local_extract + new_name

            # renomeando o arquivo.
            Path(file).absolute().rename(local_path)

            # add o diretorio do arquivo que foi renomeado
            self.files_ren.append(local_path)


    def Extract(self, files):
        '''Extrai todos os arquivos conforme sua extenção.'''

        for file in files:

            # cria um diretorio para extracao
            self.MakeDir(path_os.basename(file))

            # nome e extensao do arquivo
            name_file, ext_file = path_os.splitext(file)

            # add todos os diretorios a uma variavel para quando for desenhar
            self.directorys.append(path_os.abspath(name_file))

            get_obj_extract = self._obj.get(ext_file)

            # obtendo o objeto(rar, tar ou zip)
            obj_extract = get_obj_extract(file)

            # extraindo o arquivo.
            obj_extract.extractall()
        

    def MakeDir(self, name):
        '''Funcao que cria um diretorio'''

        Path(name).mkdir()

        return True


    # def Draw(self, path_imgs):
        # '''Desenha as imagens no arquivo .pdf.'''

        #pdf.setPageSize(self.GetSize(img))


    # def GetSize(self, imagem):
    #     '''Retorna o tamanho da imagem(largura e altura).'''

    #     img = Image.open(imagem)
    #     return img.width, img.height


if __name__ == '__main__':
    try:
        rmtree('Conv')
    except FileNotFoundError:
        pass

    Converter('pablo.cbz', 'pablo.cbr')