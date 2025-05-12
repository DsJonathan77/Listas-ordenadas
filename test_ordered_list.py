
from ordered_list import OrderedList

lista = OrderedList()
lista.insert("Banana", 2.5)
lista.insert("Maçã", 3.0)
lista.insert("Abacaxi", 5.5)
lista.insert("Laranja", 4.0)

print("Lista ordenada por descrição:")
lista.display()

print("\nBuscando por 'Maçã':")
res = lista.search("Maçã")
print(f"Encontrado: {res.descricao} - R${res.preco}" if res else "Não encontrado.")

print("\nRemovendo 'Banana':")
removido = lista.remove("Banana")
print("Removido com sucesso!" if removido else "Elemento não encontrado.")
lista.display()
