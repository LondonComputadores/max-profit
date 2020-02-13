"""
O senhor e-Deployer gostaria de comprar uma ação e vendê-la em um curto espaço
de tempo, mas apenas se esta operação dê lucro. Para isso, é passado um array
K com os valores das ações nos determinados dias, onde ele poderá escolher onde
comprar e vender.

Determine o maior lucro dado esse array K de preços.

Exemplo 1:

Input: [7,1,5,3,6,4]

Output: 5

Explicação: Este valor acontece quando compramos a ação no 2o dia e a
vendemos no 5o dia (6 - 1)
"""

def max_lucro(precos):
    lucro = 0
    for i in range(len(precos)):
        preco_compra = precos[i]
        max_preco_venda = max(precos[i:])
        melhor_preco_venda = max_preco_venda - preco_compra
        if melhor_preco_venda > lucro:
            lucro = melhor_preco_venda
            return lucro

print(max_lucro([7, 1, 5, 3, 6, 4]))
