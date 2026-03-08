📊 Lâmina de Derivativos Agrícolas

Aplicação web desenvolvida em Python para geração automática de lâminas de estruturas de opções em commodities agrícolas, com visualização de payoff, histórico de preços e características da estrutura.

A aplicação utiliza Streamlit para interface interativa e permite simular diferentes estratégias de derivativos para contratos de soja e milho.

⸻

🚀 Funcionalidades

A aplicação permite ao usuário:
	•	Selecionar o ativo subjacente
	•	Escolher o tipo de estrutura de opções
	•	Definir strikes
	•	Inserir o custo da estrutura

A partir dessas informações o sistema gera automaticamente:

📄 Lâmina da estrutura

A lâmina inclui:

Coluna esquerda
	•	Ativo
	•	Estrutura
	•	Strikes
	•	Custo da estrutura
	•	Breakeven
	•	Ganho máximo
	•	Perda máxima

Coluna direita
	•	Gráfico de Payoff da Estrutura

Seção inferior
	•	Gráfico de histórico de preços (últimos 6 meses)
	•	Linhas de referência dos strikes

Também inclui gráfico interativo via TradingView.
