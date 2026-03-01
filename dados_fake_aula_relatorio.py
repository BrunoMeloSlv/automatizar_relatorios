import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()
np.random.seed(42)

# -------------------------
# Criar vendedores
# -------------------------
vendedores = ["Ana", "Bruno", "Carlos", "Daniela"]

# -------------------------
# Gerar vendas fake
# -------------------------
dados_vendas = []

for i in range(200):
    vendedor = np.random.choice(vendedores)
    valor = round(np.random.uniform(100, 5000), 2)
    comissao_individual = round(valor * 0.03, 2)  # comissão base 3%
    
    dados_vendas.append({
        "id_venda": i + 1,
        "vendedor": vendedor,
        "cliente": fake.company(),
        "item_vendido": fake.word().capitalize(),
        "valor_venda": valor,
        "comissao_individual": comissao_individual
    })

vendas_df = pd.DataFrame(dados_vendas)

# -------------------------
# Gerar metas fake
# -------------------------
metas_df = pd.DataFrame({
    "vendedor": vendedores,
    "meta_mensal": [50000, 60000, 45000, 70000]
})

# Salvar planilhas
vendas_df.to_csv("vendas.csv", index=False)
metas_df.to_csv("metas.csv", index=False)

print("Planilhas geradas com sucesso!")