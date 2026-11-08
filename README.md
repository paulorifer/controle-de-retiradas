# 📦 Sistema de Controle e Rastreio de Retiradas

## 📖 História & Motivação
Na minha vivência na área de logística, o controle de mercadorias vindas de outras lojas era um verdadeiro desafio manual. Muitas vezes, os itens chegavam e a dificuldade para localizar a posição física exata no estoque gerava atrasos no atendimento ao cliente. A motivação para criar este projeto nasceu justamente da necessidade de automatizar e organizar esse fluxo, transformando uma dificuldade operacional real em uma solução digital prática.

## 💡 O que é o projeto hoje?
Atualmente, este projeto funciona como um **protótipo funcional** de estudo e automação, desenvolvido para validar regras de negócio aplicadas ao ambiente logístico e servir de base para o meu portfólio de desenvolvimento.

## 🛠️ Decisões Técnicas
- **Por que Python?** Pela agilidade no desenvolvimento, clareza da sintaxe e facilidade na manipulação de estruturas de dados e lógica.
- **Por que JSON para persistência?** Para manter o sistema leve, sem a necessidade de configurar um banco de dados relacional complexo logo no início, garantindo que os cadastros fiquem salvos localmente em arquivo (`estoque.json`) de forma simples e direta.

## 🚀 Como Executar
1. Certifique-se de ter o **Python 3** instalado na sua máquina.
2. Clone este repositório ou baixe os arquivos para o seu computador.
3. Abra a pasta do projeto no seu terminal ou editor (como o VS Code).
4. Execute o script principal rodando o comando: `python projeto_controle_retiradas.py`

## 🧠 Aprendizados e dificuldades
O maior desafio aqui foi garantir que o sistema não apagasse os cadastros anteriores toda vez que salvasse os dados no JSON. Tive que quebrar a cabeça um pouco com a lógica de leitura e escrita do arquivo e com a validação do que o usuário digita. No fim das contas, apanhar disso me deu uma clareza sobre como manipular arquivos e tratar erros em Python.

## ⚠️ Limitações Conhecidas & Visão de Futuro
Como o sistema roda direto no terminal (CLI) e salva em um arquivo JSON local, ele é perfeito para estudos e pequenos volumes, mas não consegue que várias pessoas usem ao mesmo tempo.
- **Onde quero chegar:** O próximo passo é evoluir isso para um banco de dados relacional (como SQL) e, futuramente, estruturando consultas avançadas e integrando futuras rotinas de automação e análise de dados para o setor de logística.