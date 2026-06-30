# 📊 Relatório de Receita de uma cafeteria

Projeto Python que automatiza a análise de dados de vendas e gera gráficos a partir de uma planilha `.xlsx`.

## 🔧 Tecnologias utilizadas

- Python
- Pandas
- Matplotlib
- Openpyxl

## 📁 Estrutura do projeto

```
coffee-sales-report/
│
├── data/
│   └── coffee.xlsx
├── output/
│   ├── pizza_cshtp.png
│   ├── bar_prod.png
│   └── linha_mes.png
├── data_control.py     (lê o csv original, mostra informações da tabela e mostra se tem algum valor nulo)
├── main.py          (lê o csv original, salva como xlsx)
├── gerar_graficos.py (lê o xlsx, gera os 3 gráficos)
└── README.md
```

## ▶️ Como rodar

1. Instale o Python em [python.org](https://www.python.org/)

2. Instale as dependências:
```bash 
pip install pandas matplotlib openpyxl
```

3. Instale o arquivo csv na pasta `data/`

4. Gere a planilha de dados:
```bash
python main.py
```
5. (Opcional) Verifique a qualidade dos dados:
```bash
python data_control.py
```
6. Gere os gráficos:
```bash
python gerar_graficos.py
```

Os gráficos serão salvos na pasta `output/`.