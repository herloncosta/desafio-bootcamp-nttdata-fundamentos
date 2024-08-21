# Sistema Bancário em Python

## Desafio do módulo de fundamentos do curso

Este é um simples sistema bancário implementado em Python, permitindo aos usuários realizar depósitos, saques e consultar o extrato de uma conta. O sistema utiliza um menu interativo para que o usuário possa escolher as operações desejadas.

## Funcionalidades

- **Depósito:** Permite ao usuário adicionar fundos à conta, desde que o valor seja positivo.
- **Saque:** Permite ao usuário retirar fundos da conta, com as seguintes restrições:
  - O saque só pode ser realizado se houver saldo suficiente.
  - O limite máximo de saques por sessão é de 3 operações.
  - O valor máximo para cada saque é de R$500.
- **Extrato:** Exibe o histórico de depósitos e saques, bem como o saldo atual da conta.
- **Sair:** Encerra o sistema.

## Como Utilizar

1. Clone ou baixe o código-fonte deste repositório.

2. Execute o arquivo `main.py` no seu ambiente Python.

3. Siga as instruções no menu interativo:
   - Digite **[d]** para realizar um depósito.
   - Digite **[s]** para realizar um saque.
   - Digite **[e]** para visualizar o extrato da conta.
   - Digite **[q]** para sair do sistema.

## Estrutura do Código

- **menu:** Uma string que exibe as opções do sistema.
- **depositos:** Lista que armazena os valores de todos os depósitos realizados.
- **saques:** Lista que armazena os valores de todos os saques realizados.
- **LIMITE_SAQUES:** Variável que controla o número máximo de saques permitidos.
- **valor_maximo:** O valor máximo permitido para um saque (R$500).
- **saldo:** O saldo atual da conta, que começa em 0.

### Funções

- **mostrar_menu():** Exibe o menu com as opções disponíveis.
- **depositar(valor):** Realiza um depósito, se o valor for válido, e atualiza o saldo.
- **sacar(valor):** Realiza um saque, se o valor for válido, e atualiza o saldo e o limite de saques.
- **mostrar_extrato():** Exibe o extrato da conta, mostrando depósitos, saques e o saldo atual.
- **main():** Função principal que executa o loop do menu até que o usuário decida sair.

## Exemplo de Uso

```bash
    SISTEMA BANCÁRIO
    ------------------------
    [d] Depósito
    [s] Saque
    [e] Extrato
    [q] Sair

Digite a opção desejada: d
Digite o valor do depósito: 1000
Depositado 1000.00 reais.

Digite a opção desejada: s
Digite o valor do saque: 200
Saque realizado com sucesso. Saldo atual: 800.00 reais.

Digite a opção desejada: e

========== EXTRATO ==========
DEPÓSITOS:
+ R$ 1000.00
SAQUES:
- R$ 200.00
SALDO: R$ 800.00

Digite a opção desejada: q
Saindo do sistema...
```

## Requisitos

- Python 3.x

## Como Contribuir

Sinta-se à vontade para contribuir com melhorias no código ou novas funcionalidades. Para isso, faça um fork deste repositório, implemente suas mudanças e abra um pull request.

## Licença

Este projeto é de domínio público.

---

Este README oferece uma visão geral do sistema bancário, orienta o usuário sobre como utilizar as funcionalidades, e descreve a estrutura do código para facilitar o entendimento e contribuições futuras.
