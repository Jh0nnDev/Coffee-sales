import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("data/coffee.xlsx")
y = df['coffee_name'].value_counts()

plt.barh(y.index, y.values)
plt.title("Produtos mais vendidos")
plt.xlabel("Quantidade vendida")
plt.tight_layout()
plt.savefig("output/bar_prod.png")
plt.show()