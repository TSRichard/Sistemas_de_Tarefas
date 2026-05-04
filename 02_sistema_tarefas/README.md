# 📝 Sistema de Tarefas (To-Do CLI)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![JSON](https://img.shields.io/badge/JSON-Persist%C3%AAncia-green.svg)](https://www.json.org)
[![CLI](https://img.shields.io/badge/CLI-Interativo-orange.svg)](https://en.wikipedia.org/wiki/Command-line_interface)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🎯 O que este projeto faz

Um gerenciador de tarefas completo que roda no terminal, permitindo:
- ✅ Adicionar novas tarefas
- ✅ Listar tarefas com status (✅ concluída / ❌ pendente)
- ✅ Marcar tarefas como concluídas
- ✅ Remover tarefas
- ✅ Persistência automática em JSON (dados não somem!)

## 🚀 Como usar

### Pré-requisitos
- Python 3.8 ou superior

### Instalação

```bash
# Clone o repositório
git clone https://github.com/TSRichard/analisador-vendas.git

# Entre na pasta do projeto
cd analisador-vendas

# Execute o sistema de tarefas
python 02_sistema_tarefas/tarefas.py


DEMONSTRAÇÃO
========================================
📝 SISTEMA DE TAREFAS
========================================
1. Adicionar tarefa
2. Listar tarefas
3. Concluir tarefa
4. Remover tarefa
5. Sair
========================================

Escolha uma opção: 1
📝 Título da tarefa: Estudar Python
✅ Tarefa 'Estudar Python' adicionada! (ID: 1)

Escolha uma opção: 2
==================================================
📋 LISTA DE TAREFAS
==================================================
1. ❌ Estudar Python (ID: 1)
   📅 Criada em: 2026-04-20 21:30:15
--------------------------------------------------

📁 Estrutura do Projeto
02_sistema_tarefas/
├── data/
│   └── tasks.json          # Arquivo de persistência
├── tarefas.py              # Código principal
└── README.md               # Documentação


💾 Formato dos Dados (tasks.json)
[
  {
    "id": 1,
    "titulo": "Estudar Python",
    "concluida": false,
    "criada_em": "2026-04-20 21:30:15"
  }
]

🛠️ Tecnologias Utilizadas
Python 3.8+ - Linguagem principal
JSON - Persistência de dados
pathlib - Manipulação de caminhos de arquivos
datetime - Registro de timestamps

📚 Funcionalidades em Detalhe
Função	Descrição	Comando
Adicionar	Cria nova tarefa com ID automático	Opção 1
Listar	Mostra todas as tarefas formatadas	Opção 2
Concluir	Marca tarefa como ✅	Opção 3
Remover	Exclui tarefa permanentemente	Opção 4
Persistência	Salva automaticamente após cada ação	Automático

🎓 Habilidades Demonstradas
✅ Manipulação de arquivos JSON (leitura/escrita)
✅ CRUD completo (Create, Read, Update, Delete)
✅ Tratamento de erros e exceções
✅ Listas e dicionários em Python
✅ Interface de linha de comando interativa
✅ Organização de código com funções
✅ Persistência de dados

🔧 Próximas Melhorias
Adicionar data de vencimento nas tarefas
Implementar categorias (trabalho, pessoal, estudo)
Adicionar busca por texto
Exportar tarefas para CSV
Interface colorida com colorama
Notificações de tarefas atrasadas

🐛 Tratamento de Erros
O sistema foi desenvolvido com validações robustas:
✅ Impede títulos vazios
✅ Verifica se número da tarefa existe
✅ Confirmação antes de remover
✅ Lida com arquivo JSON corrompido
✅ Trata entradas não numéricas

👨‍💻 Autor
Richard Teixeira

Estudante de Sistemas de Informação apaixonado por tecnologia.
📚 Atualmente: Python, JSON
🎯 Meta: Primeira oportunidade como desenvolvedor

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/TSRichard)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tsrichard/)

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

🌟 Projetos Relacionados
Analisador de Vendas - Projeto anterior do portfólio
Próximo: Dashboard com Streamlit (em breve)