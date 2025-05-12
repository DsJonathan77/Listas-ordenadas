✅ Relatório da Atividade – Ordenação por Descrição
🔧 Modificações Realizadas
O projeto original foi modificado para que a lista encadeada seja ordenada com base no atributo descricao (ordem alfabética), ao invés de preco. As mudanças ocorreram principalmente no método:

insert: agora compara a descrição dos produtos usando operadores de string para manter a ordem correta na lista.

search e remove: adaptados para operar com base em descricao ao invés de preco.

🧪 Testes Efetuados
Os testes foram feitos no script test_ordered_list.py, incluindo:

python
lista.insert("Banana", 2.5)
lista.insert("Maçã", 3.0)
lista.insert("Abacaxi", 5.5)
lista.insert("Laranja", 4.0)
Resultado esperado:

Abacaxi

Banana

Laranja

Maçã

Busca:

python
res = lista.search("Maçã")
Remoção:

python
lista.remove("Banana")
Todos os testes foram executados com sucesso, exibindo os resultados esperados na ordem correta.

💭 Desafios e Observações
O principal desafio foi adaptar a lógica de ordenação para trabalhar com strings, garantindo que a comparação seguisse a ordem alfabética.

A escolha de descricao como chave de ordenação facilitou a visualização da lista, tornando-a mais intuitiva para o usuário.

Operações como inserção e remoção continuaram com tempo linear, pois a lista é simples (não duplamente encadeada nem indexada).

# 📋 Ordered List por Descrição

Este projeto implementa uma lista encadeada ordenada utilizando Python, onde os elementos (produtos) são organizados **alfabeticamente pela descrição**, em vez de pelo preço.

## 🚀 Objetivo

O objetivo da atividade é adaptar a estrutura da lista ordenada para que a ordenação dos elementos ocorra com base no atributo `descricao`, utilizando uma estrutura de dados do tipo lista encadeada.

## 🧱 Estrutura do Projeto

- `ordered_list.py`: Contém a definição da classe `OrderedList` e da estrutura `Node`.
- `test_ordered_list.py`: Script de teste com inserções, buscas e remoções para validar o funcionamento da lista.

## ⚙️ Funcionalidades

- Inserção de elementos mantendo a ordem alfabética pela descrição.
- Busca por elementos com base na descrição.
- Remoção de elementos.
- Exibição da lista ordenada.

## 💻 Como Executar

1. Clone o repositório ou baixe os arquivos.
2. No terminal, execute o script de teste:

```bash
python test_ordered_list.py
