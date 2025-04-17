# -Gerador-de-Cart-es-com-QR-Code
🧾 Gerador de Cartões com QR Code para Equipamentos
Este script em Python gera automaticamente cartões com QR Code personalizados para identificação de equipamentos. O cartão contém o número do equipamento, o QR Code correspondente, e um rodapé com nome da empresa e telefone.

🛠️ Requisitos
Python 3.10+

Bibliotecas:

qrcode

Pillow

Instale com:

bash
Copiar
Editar
pip install qrcode[pil]
📄 Descrição do Funcionamento
Entrada do Usuário: O programa solicita o número do equipamento.

Geração do QR Code: Com base no número inserido, o QR Code é gerado.

Criação do Cartão: O cartão é montado com:

Número do equipamento à esquerda.

QR Code à direita.

Linha separadora e rodapé com informações da empresa.

Ajuste Dinâmico de Texto: O tamanho da fonte é ajustado automaticamente para caber no espaço disponível.

Exportação: O cartão é salvo em alta resolução (600 dpi) na pasta de Downloads como QR_<número>.png.

📐 Dimensões
Formato do cartão: 9cm x 5cm

DPI: 600 (alta qualidade para impressão)

📁 Estrutura de Saída
text
Copiar
Editar
Downloads/
├── QR_001.png
├── QR_002.png
└── ...
🔁 Loop Interativo
O script permanece em execução até que o usuário digite sair.
