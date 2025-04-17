# Texto ou link para gerar o QR Code
data = "https://www.linkedin.com/in/raiquesilva/"

import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

# Configurações do cartão
dpi = 600
largura, altura = int(9 * dpi / 2.54), int(5 * dpi / 2.54)  # Conversão cm → pixels
margem = int(largura * 0.05)
qr_tamanho = int(altura * 0.65)  # Ajuste do QR Code

# Carregar fontes
try:
    fonte_padrão = ImageFont.truetype("arial.ttf", int(altura * 0.15))  # Fonte inicial grande
    fonte_menor = ImageFont.truetype("arial.ttf", int(altura * 0.08))  # Fonte do rodapé
except:
    fonte_padrão = ImageFont.load_default()
    fonte_menor = fonte_padrão

# Diretório de salvamento (Downloads)
caminho_pasta = os.path.join(os.path.expanduser("~"), "Downloads")

while True:
    # Solicita o número do equipamento
    equipamento_num = input("\nDigite o número do equipamento (ou 'sair' para encerrar): ").strip()
    if equipamento_num.lower() == "sair":
        print("Encerrando o programa...")
        break

    equipamento_id = f"{equipamento_num}"

    # Gera o QR Code
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(equipamento_id)
    qr.make(fit=True)
    qr_img = qr.make_image(fill="black", back_color="white")
    qr_img = qr_img.resize((qr_tamanho, qr_tamanho))

    # Cria o cartão
    cartao = Image.new("RGB", (largura, altura), "white")
    draw = ImageDraw.Draw(cartao)

    # Ajusta tamanho do texto do equipamento
    fonte_numero = fonte_padrão
    max_largura_texto = largura - margem - qr_tamanho - margem  # Espaço disponível
    while draw.textlength(equipamento_id, font=fonte_numero) > max_largura_texto:
        tamanho_atual = fonte_numero.size
        fonte_numero = ImageFont.truetype("arial.ttf", max(tamanho_atual - 5, 10))

    # Posições dos elementos
    pos_qr_x = largura - margem - qr_tamanho  # QR Code à direita
    pos_qr_y = (altura - qr_tamanho) // 2 - int(altura * 0.08)  # Ajuste para subir
    pos_texto_x = margem  # Número do equipamento à esquerda
    pos_texto_y = (altura - qr_tamanho) // 2 + (qr_tamanho // 4)

    # Desenha número do equipamento
    draw.text((pos_texto_x, pos_texto_y), equipamento_id, fill="black", font=fonte_numero)

    # Insere o QR Code na imagem
    cartao.paste(qr_img, (pos_qr_x, pos_qr_y))

    # Linha separadora
    linha_y = altura - int(altura * 0.3)
    draw.line([(margem, linha_y), (largura - margem, linha_y)], fill="black", width=5)

    # Rodapé com nome da empresa e telefone
    rodape_texto = "Empresa   |   (11) telefone"
    rodape_y = linha_y + int(altura * 0.05)
    draw.text(((largura - draw.textlength(rodape_texto, fonte_menor)) // 2, rodape_y), rodape_texto, fill="black", font=fonte_menor)

    # Salva o arquivo
    caminho_arquivo = os.path.join(caminho_pasta, f"QR_{equipamento_id}.png")
    cartao.save(caminho_arquivo, dpi=(dpi, dpi))
    print(f"✅ QR Code gerado e salvo em: {caminho_arquivo}")

print("Programa finalizado.")
