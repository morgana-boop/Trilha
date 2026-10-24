PDV com Descontos — Nível 1

## O que o código faz

Este programa simula um Ponto de Venda (PDV). 
Para cada compra, recebe o valor, a idade do cliente, a quantidade de itens e um possível cupom de fidelidade. 
Calcula os descontos aplicáveis, mostra o valor final e registra a compra numa lista. 
Quando o usuário digita `0` no valor da compra, o sistema encerra a entrada de dados, apresenta o resumo do dia e salva o resumo e o histórico em `resumo.txt`.


## Como ele faz

1. Solicita o valor da compra. É possível digitar os centavos com ponto ou vírgula.
2. Se o valor for `0`, encerra o loop. Se for negativo, mostra um aviso e solicita outra compra.
3. Solicita a idade do cliente. Se a idade for negativa, mostra um aviso e solicita a idade novamente.
4. Solicita a quantidade de itens e não aceita quantidades negativas.
5. Solicita o cupom de fidelidade. Se não houver cupom, pressionar Enter.
6. Se a idade for maior ou igual a 65 anos, aplica 20% de desconto.
7. Depois do desconto por idade, verifica se o valor restante é maior que R$ 100,00. Se for, aplica mais 10% sobre esse valor.
8. Se a quantidade de itens for maior que 3, aplica mais 5% sobre o valor já descontado.
9. Se o cupom for exatamente `FIDELIDADE10`, aplica mais 10% sobre o valor já descontado.
10. Calcula o desconto total da compra e armazena os dados numa lista usando `append()`.
11. Ao encerrar, percorre a lista com `for` e calcula a quantidade de compras, o total bruto, o total de descontos e o total final.
12. Usa `open("resumo.txt", "w", encoding="utf-8")` para salvar o resumo e percorre novamente a lista com `for` para registrar os detalhes das compras.

Os descontos são sequenciais: cada desconto percentual é calculado sobre o valor que restou após os descontos anteriores.
O valor `0` usado para encerrar não é registrado como compra. O arquivo `resumo.txt` é criado no diretório em que o comando Python for executado que se já existir será sobrescrito.


## Como rodar

No terminal, entre na pasta `nivel_1` e execute: python pdv.py


## Validação

Para verificar o encerramento, digite `0` quando o programa solicitar o valor da próxima compra.
Para verificar a validação, teste um valor negativo e uma idade negativa.


## Tabela de exemplos e casos de teste

Para reproduzir os eventos deixe o cupom vazio em cada compra e quantidade 1.


## Testes dos bônus

Para reproduzir os eventos coloque o cupom FIDELIDADE10 em cada compra (ou algumas) e quantidade a escolha.


