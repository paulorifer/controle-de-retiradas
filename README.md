# Controle de Retiradas — Sistema de Gestão de Retiradas de Mercadorias

Sistema em Python desenvolvido para resolver um problema real da empresa onde trabalhei: organizar o recebimento de itens vindos de outras lojas para facilitar a localização e agilizar a retirada pelo cliente na loja.

## Funcionalidades

- Cadastro de produto com código RP, loja, cliente, CPF, localização física, número do pedido, nota fiscal e data de chegada
- Busca de produto por CPF do cliente
- Marcação de produto como retirado
- Persistência completa dos dados em arquivo JSON

## Tecnologias

- Python 3
- Módulo `json` para persistência de dados
- Módulo `datetime` para registro de data/hora do cadastro

## Como executar

```bash
python projeto_controle_retiradas.py
