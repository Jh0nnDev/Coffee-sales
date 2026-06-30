import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("data/coffee.xlsx")
y = df['cash_type'].value_counts()


plt.title("Forma de Pagamento Mais Utilizada")
traducao = {'card': 'Cartão', 'cash': 'Dinheiro'}
labels = [traducao[i] for i in y.index]
plt.pie(y, labels=labels)
plt.tight_layout() 
plt.savefig("output/pizza_cshtp.png")
plt.show()
