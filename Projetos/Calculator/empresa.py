faturamento=1200 # tipo:int -> número inteiro
custo=750 # tipo:float -> ponto flutuante (casa decimal)

novas_vendas=100
faturamento=faturamento+novas_vendas

imposto=faturamento *0.1
lucro=faturamento-custo-imposto

margem_lucro=lucro/faturamento

print('O Faturamneto foi de',faturamento)
print('O custo foi de',custo)
print('O lucro foi de',lucro)
print('A margem de lucro foi de',round(margem_lucro, 2)) # round -. arredondar números decimais

mensagem='O faturamento da loja foi de tanto' #
email='emailqualquer@gmail.com' # tipo:string -. texto

teve_lucro=True #variável tipo:boolean

# Mod -> % resto da divisão 
tempo_contrato=170
tempo_anos=170/12
print('Tempo em anos', int(tempo_anos))
tempo_meses=170%12
print('Tempo em mêses',tempo_meses)