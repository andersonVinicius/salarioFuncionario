from Funcionario import Funcionario
# func1= Funcionario(444,"andersn",100000)
# func1.salario = 12432

list_name = ['ana','carlos','joao','carmem']
list_sal = [4000,3000,2500,3566]
list_id = [565,554,565, 554]
list_func = []
quant = len(list_name)

for i in range(quant):

   # verificar id repetido no arrya
   try:
       print("A",next(filter(lambda x: x.id == list_id.__getitem__(i), list_func)).nome,
             "tem o mesmo ID que,",list_name.__getitem__(i) )
       if quant == i+1:
          break # se for a ultima posicao e tiver um valor repetido, parar o loop
       else:
           i = i + 1 # caso contrario, pule uma posicao no array

   except:

       # criar funcionario se na houver ID repetido
       novoFunc = Funcionario(list_id.__getitem__(i),
                              list_name.__getitem__(i),
                              list_sal.__getitem__(i))

       #armazenamento de objeto Funcionario
       list_func.append(novoFunc)

#escolha um funcionario eleito=============================
taxa = 10# 10%
empregadoEleito_id = 554


print("Quantidade de empregados: ",quant)
print("================================")
for i in range(len(list_func)):
        print("Empregado #",i+1,":")
        print("ID: ", list_func[i].id)
        print("Nome: ", list_func[i].nome)
        print("Salario: $", list_func[i].salario)
        print("================================")

print("Taxa de aumento: ",taxa,"%")
print("      ")
print("ID empregado do Empregado Sortudo:",empregadoEleito_id )
print("      ")

try:
    print("Sistema ----> O", next(filter(lambda x: x.id == empregadoEleito_id, list_func)).id,"Existe!")
    # Mostrar valores novos de salario
    print(" ")
    print("Empregados ATUALIZADOS-------------------------->")
    for i in range(len(list_func)):
        if (empregadoEleito_id == list_func[i].id):
            list_func[i].calcula_salario(taxa/100)
        print(list_func[i].id,",", list_func[i].nome,",", list_func[i].salario)
        # list_func[i].salario =9292929
        print("================================")
    print("--------------------------------------------------")
except:
    print("Sitema -----> O empregado n existe!!, aborta operacao!")


