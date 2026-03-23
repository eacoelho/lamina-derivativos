# 📊 Lâmina de Estruturas de Opções — Mesa de Derivativos

Aplicativo web desenvolvido em **Streamlit** para geração de lâminas profissionais de estruturas de opções em agrocommodities. Voltado para mesas de derivativos que precisam comunicar estratégias a clientes de forma visual, clara e exportável.

-----

## 🖥️ Demo

![screenshot](docs/screenshot.png)

-----

## ✨ Funcionalidades

### Ativos suportados

|Commodity|Bolsa |Ticker (Yahoo Finance)|Unidade|
|---------|------|----------------------|-------|
|Soja     |CBOT  |`ZS=F`                |¢/bu   |
|Milho    |CBOT  |`ZC=F`                |¢/bu   |
|Algodão  |ICE NY|`CT=F`                |¢/lb   |

### Estruturas disponíveis

|Estrutura            |Legs|Níveis    |
|---------------------|----|----------|
|Long Put             |1   |K1        |
|Long Call            |1   |K1        |
|Put Spread           |2   |K1, K2    |
|Call Spread          |2   |K1, K2    |
|Bear Zero Cost Collar|2   |K1, K2    |
|Bull Zero Cost Collar|2   |K1, K2    |
|Bear Fence           |3   |K1, K2, K3|
|Bull Fence           |3   |K1, K2, K3|

### A lâmina gerada inclui

- **Header** com commodity, estrutura, vencimento e data
- **Cards informativos** com descrição técnica da estrutura e recomendação de uso
- **Gráfico duplo**: histórico de preços dos últimos 12 meses com linhas sobrepostas dos strikes + diagrama de payoff
- **Tabela de payoff** com simulação de cenários: −20%, −10%, 0%, +10%, +20%
- **Exportação em PNG** de alta resolução, pronta para envio ao cliente

-----

## 🚀 Como executar

### Pré-requisitos

- Python 3.10 ou superior

### Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/lamina-derivativos.git
cd lamina-derivativos

# Crie e ative um ambiente virtual (recomendado)
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows

# Instale as dependências
pip install -r requirements.txt
```

### Execução

```bash
streamlit run app.py
```

O app abrirá automaticamente em `http://localhost:8501`.

-----

## 🗂️ Estrutura do projeto

```
lamina-derivativos/
├── app.py              # Aplicativo principal
├── requirements.txt    # Dependências Python
├── README.md           # Este arquivo
└── docs/
    └── screenshot.png  # Captura de tela para o README
```

-----

## ⚙️ Fluxo de uso

1. **Selecione a commodity** e o **vencimento** no painel lateral
1. O **spot de referência** é preenchido automaticamente via Yahoo Finance (editável)
1. **Escolha a estrutura** — os campos de strike aparecem dinamicamente conforme a estratégia
1. Informe os **níveis (K1/K2/K3)** e o **custo/prêmio líquido** (quando aplicável)
1. Clique em **⚡ Gerar Lâmina**
1. Use o botão **⬇️ Baixar Lâmina (PNG)** para exportar o relatório

-----

## 📦 Dependências

|Biblioteca  |Uso                                        |
|------------|-------------------------------------------|
|`streamlit` |Interface web e interatividade             |
|`yfinance`  |Dados históricos de preços (Yahoo Finance) |
|`pandas`    |Manipulação de dados e tabelas             |
|`numpy`     |Cálculo do payoff e simulações             |
|`matplotlib`|Geração dos gráficos e da lâmina exportável|
|`Pillow`    |Suporte a exportação de imagem             |

-----

## 📐 Lógica de payoff

Cada estrutura implementa sua função de payoff analítica. Exemplo para **Bear Zero Cost Collar**:

```
Payoff = max(K1 − S, 0) − max(S − K2, 0)
```

Onde `S` é o preço do ativo no vencimento, `K1` o strike da put comprada e `K2` o strike da call vendida.

-----

## ⚠️ Aviso legal

Este software tem caráter exclusivamente **informativo e educacional**. Não constitui oferta, solicitação ou recomendação de compra ou venda de qualquer instrumento financeiro. Operações com derivativos envolvem riscos significativos e podem resultar em perdas superiores ao capital inicialmente comprometido. Consulte sua mesa de operações e verifique as especificações completas dos contratos antes de operar.

-----

## 📄 Licença

MIT License. Consulte o arquivo `LICENSE` para detalhes.
