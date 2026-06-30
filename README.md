# 📊 Relatório de Receita

Projeto Python que automatiza a análise de dados de vendas e gera gráficos a partir de uma planilha `.xlsx`.

## 🔧 Tecnologias utilizadas

- Python
- Pandas
- Matplotlib
- Openpyxl

## 📁 Estrutura do projeto

```
sales-report/
│
├── data/
│   └── vendas.xlsx
├── output/
│   └── (gráficos gerados aqui)
├── main.py
└── gerar_graficos.py
```

## ▶️ Como rodar

1. Instale o Python em [python.org](https://www.python.org/)

2. Instale as dependências:
```bash 
pip install pandas matplotlib openpyxl
```

3. Gere a planilha de dados:
```bash
python main.py
```

4. Gere os gráficos:
```bash
python gerar_graficos.py
```

Os gráficos serão salvos na pasta `output/`.