from PIL import Image
from reportlab.pdfgen import canvas
from os.path import basename, splitext


def Draw(nome_pdf, titulo_pdf, imagens):
    '''Desenha as imagens no arquivo .pdf.'''

    # cria um novo pdf
    pdf = canvas.Canvas(f"{nome_pdf}.pdf")
    # ordena a lista de imagens
    imagens.sort()

    print("Inserindo as imagens")
    for img in imagens:        
        #aplicar um tamanho a pagina
        pdf.setPageSize(GetSize(img))
        #desenhar a imagem em uma posicao x e y
        pdf.drawImage(img, 0,0)
        #criar uma nova pagina
        pdf.showPage()

    
    pdf.setTitle(titulo_pdf) #titulo    
    pdf.save() # salvar
    
    print("Terminado.")

    return True


def GetSize(imagem):
    '''Retorna o tamanho da imagem(largura e altura).'''

    return Image.open(imagem).size