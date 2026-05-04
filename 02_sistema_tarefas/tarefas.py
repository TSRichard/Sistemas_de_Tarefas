"""
Sistema de Tarefas - Portfólio Python
Autor: Seu Nome
Descrição: Gerenciador de tarefas via linha de comando com persistência em JSON
"""

import json
from pathlib import Path
from datetime import datetime

DATA_DIR = Path(__file__).parent / "data"
DATA_FILE = DATA_DIR / "tasks.json"

def carregar_tarefas():
    """Carrega as tarefas do arquivo JSON"""
    if not DATA_FILE.exists():
        # Se o arquivo não existe, retorna lista vazia
        print("📁 Arquivo não encontrado. Criando novo arquivo...")
        return []
    
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            tarefas = json.load(f)
        print(f"✅ {len(tarefas)} tarefas carregadas com sucesso!")
        return tarefas
    except Exception as e:
        print(f"❌ Erro ao carregar tarefas: {e}")
        return []

def salvar_tarefas(tarefas):
    """Salva as tarefas no arquivo JSON"""
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(tarefas, f, ensure_ascii=False, indent=2)
        print(f"💾 Tarefas salvas com sucesso!")
        return True
    except Exception as e:
        print(f"❌ Erro ao salvar tarefas: {e}")
        return False

def mostrar_menu():
    """Exibe o menu principal"""
    print("\n" + "="*40)
    print("📝 SISTEMA DE TAREFAS")
    print("="*40)
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Sair")
    print("="*40)

def adicionar_tarefa(tarefas, titulo):
    """Adiciona uma nova tarefa"""
    # Gerar novo ID (maior ID atual + 1)
    if tarefas:
        novo_id = max(tarefa["id"] for tarefa in tarefas) + 1
    else:
        novo_id = 1
    
    # Criar nova tarefa
    nova_tarefa = {
        "id": novo_id,
        "titulo": titulo,
        "concluida": False,
        "criada_em": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    print(f"✅ Tarefa '{titulo}' adicionada com sucesso! (ID: {novo_id})")

def listar_tarefas(tarefas):
    """Mostra todas as tarefas formatadas"""
    if not tarefas:
        print("\n📭 Nenhuma tarefa cadastrada!")
        return
    
    print("\n" + "="*50)
    print("📋 LISTA DE TAREFAS")
    print("="*50)
    
    for i, tarefa in enumerate(tarefas, start=1):
        status = "✅" if tarefa["concluida"] else "❌"
        print(f"{i}. {status} {tarefa['titulo']} (ID: {tarefa['id']})")
        print(f"   📅 Criada em: {tarefa['criada_em']}")
        print("-"*50)

def concluir_tarefa(tarefas, indice):
    """Marca uma tarefa como concluída"""
    try:
        indice_ajustado = indice - 1  # Ajusta para índice da lista (começa em 0)
        if 0 <= indice_ajustado < len(tarefas):
            tarefa = tarefas[indice_ajustado]
            if not tarefa["concluida"]:
                tarefa["concluida"] = True
                salvar_tarefas(tarefas)
                print(f"✅ Tarefa '{tarefa['titulo']}' concluída! 🎉")
            else:
                print(f"⚠️ Tarefa '{tarefa['titulo']}' já estava concluída!")
        else:
            print(f"❌ Número inválido! Use um número entre 1 e {len(tarefas)}")
    except ValueError:
        print("❌ Por favor, digite um número válido!")

def remover_tarefa(tarefas, indice):
    """Remove uma tarefa"""
    try:
        indice_ajustado = indice - 1
        if 0 <= indice_ajustado < len(tarefas):
            tarefa_removida = tarefas.pop(indice_ajustado)
            salvar_tarefas(tarefas)
            print(f"🗑️ Tarefa '{tarefa_removida['titulo']}' removida com sucesso!")
        else:
            print(f"❌ Número inválido! Use um número entre 1 e {len(tarefas)}")
    except ValueError:
        print("❌ Por favor, digite um número válido!")

def main():
    """Função principal"""
    tarefas = carregar_tarefas()
    
    while True:
        mostrar_menu()
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            titulo = input("📝 Título da tarefa: ")
            if titulo.strip():
                adicionar_tarefa(tarefas, titulo)
            else:
                print("❌ Título não pode ser vazio!")
        
        elif opcao == "2":
            listar_tarefas(tarefas)
        
        elif opcao == "3":
            listar_tarefas(tarefas)
            if tarefas:
                try:
                    indice = int(input("\n🔢 Número da tarefa a concluir: "))
                    concluir_tarefa(tarefas, indice)
                except ValueError:
                    print("❌ Digite um número válido!")
        
        elif opcao == "4":
            listar_tarefas(tarefas)
            if tarefas:
                try:
                    indice = int(input("\n🔢 Número da tarefa a remover: "))
                    confirmar = input(f"⚠️ Tem certeza que quer remover? (s/n): ")
                    if confirmar.lower() == 's':
                        remover_tarefa(tarefas, indice)
                except ValueError:
                    print("❌ Digite um número válido!")
        
        elif opcao == "5":
            print("\n👋 Até logo! Suas tarefas foram salvas.")
            break
        
        else:
            print("❌ Opção inválida! Escolha 1, 2, 3, 4 ou 5.")
            
if __name__ == "__main__":
    # Garantir que a pasta data existe
    DATA_DIR.mkdir(exist_ok=True)
    main()