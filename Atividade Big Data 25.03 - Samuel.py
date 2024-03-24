import pandas as pd
import matplotlib.pyplot as plt

jogosQts = {
    "Grand Theft Auto VI": 27,
    "FIFA 24": 15,
    "Call of Duty: Black Ops V": 13,
    "The Legend of Zelda: Echoes of Courage": 11,
    "Assassin's Creed: Ragnarok": 9
}

serie2 = pd.Series(jogosQts)

serie2.plot(marker='o', linestyle='-')

plt.title('Quantidade de Vendas de Jogos')
plt.xlabel('Jogos')
plt.ylabel('Quantidade Vendida (em milhões)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


