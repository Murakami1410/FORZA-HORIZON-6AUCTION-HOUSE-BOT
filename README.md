# FH6 Auction House Bot

Bot automatizado para a Casa de Leilões do Forza Horizon 4, desenvolvido em Python.

## Como funciona

O bot monitora pixels específicos da tela para detectar o estado do jogo e simula teclas automaticamente para buscar e comprar carros no leilão.

**Fluxo:**
1. Detecta a tela de busca pelo pixel de start
2. Aperta Enter para abrir a busca
3. Aperta Enter para confirmar
4. Verifica se o carro foi encontrado pelo pixel da tela de resultado
5. Se encontrou → aperta Y, desce, confirma a compra
6. Se não encontrou → aperta ESC e reinicia

## Requisitos

- Python 3.10+
- Resolução: 1720x1080 (padrão) — veja a seção de calibração para outras resoluções

## Instalação

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/fh4-auction-bot.git
cd fh4-auction-bot
```

**2. Crie um ambiente virtual**
```bash
python -m virtualenv venv
venv\Scripts\activate.bat
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

## Como usar

1. Abra o Forza Horizon 4
2. Vá até a Casa de Leilões → Buscar Carros
3. Configure os filtros de busca desejados
4. Execute o bot:
```bash
python main.py
```
5. Troque rapidamente para o jogo

## Calibração para outras resoluções

Se sua resolução for diferente de 1720x1080, você precisa ajustar as variáveis no início do `main.py`:

```python
PIXEL_START   = (151, 662)   # Pixel da tela de busca
PIXEL_CAR     = (382, 1015)  # Pixel do resultado
COR_START     = (4, 4, 5)    # Cor esperada na tela de busca
COR_CAR_FOUND = (255, 255, 255) # Cor quando carro é encontrado
TOLERANCIA    = 20           # Variação permitida por canal RGB
```

Para descobrir os valores corretos para sua resolução, use o script de calibração:

```bash
python calibrar.py
```

## Aviso

Este bot é para uso educacional. O uso de bots pode violar os Termos de Serviço do jogo.#
