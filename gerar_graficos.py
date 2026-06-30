import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("data/coffee.xlsx")

def pizza_grafic(df):
    y = df['cash_type'].value_counts()
    traducao = {'card': 'Cartão', 'cash': 'Dinheiro'}
    labels = [traducao[i] for i in y.index]

    plt.title("Forma de Pagamento Mais Utilizada")
    plt.pie(y, labels=labels)
    plt.tight_layout() 
    plt.savefig("output/pizza_cshtp.png")
    plt.show()

def sales_mes(df):
    receita_mes = df.groupby('mes')['money'].sum()

    traducao_meses = {
        1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
        5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
        9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
    }

    receita_mes.index = receita_mes.index.map(traducao_meses)
    plt.bar(receita_mes.index, receita_mes.values)
    plt.title("Receita de vendas em cada mês")
    plt.xlabel("Mês")
    plt.ylabel("Receita")
    plt.tight_layout()
    plt.savefig("output/linha_mes.png")
    plt.show()

def sales_prod(df):
    y = df['coffee_name'].value_counts()

    plt.barh(y.index, y.values)
    plt.title("Produtos mais vendidos")
    plt.xlabel("Quantidade vendida")
    plt.tight_layout()
    plt.savefig("output/bar_prod.png")
    plt.show()

sales_mes(df)
sales_prod(df)
pizza_grafic(df)