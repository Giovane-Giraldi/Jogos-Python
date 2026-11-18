



#  Coleção de Jogos em Python

Um mini-projeto desenvolvido em Python com dois jogos clássicos de terminal: **Jogo da Forca** e **Jogo de Adivinhação**. Este projeto foi construído para praticar lógica de programação, modularização, manipulação de arquivos de texto e laços de repetição.

##  Funcionalidades

- **Menu Interativo (`jogos.py`)**: Permite escolher qual jogo você deseja jogar.
- **Jogo da Forca (`forca.py`)**: 
  - Lê palavras secretas de um arquivo externo (`dados/palavra.txt`).
  - Desenha a forca progressivamente a cada erro do jogador.
  - Informa a quantidade de erros restantes.
- **Jogo de Adivinhação (`adivinhacao.py`)**:
  - Sistema de níveis de dificuldade (Fácil, Médio, Difícil e Impossível).
  - Sistema de pontuação dinâmica que diminui conforme os erros.

---

## 📂 Estrutura do Projeto

```text
Jogos-Python/
│
├── 📁 dados/
│   └── palavra.txt      # Lista de palavras para o jogo da forca
│
├── __init__.py          # Arquivo de inicialização do pacote
├── adivinhacao.py       # Lógica do jogo de adivinhação
├── forca.py             # Lógica do jogo da forca
└── jogos.py             # Menu principal para selecionar o jogo

```

---

## ⚙️ Como Executar

Certifique-se de ter o **Python** instalado em sua máquina.

1. Clone ou baixe este repositório para o seu computador.
2. Abra o terminal na pasta principal do projeto (`projeto_jogos`).
3. Execute o script do menu principal:

```bash
python jogos.py

```

4. Siga as instruções na tela para escolher e jogar!

---

## 🛠️ Tecnologias Utilizadas

* **Python 3** (Linguagem principal)
* **Módulo `random**` (Para sorteio de números e palavras)
* **Manipulação de Arquivos de Texto (`open/read`)**


