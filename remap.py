import pandas as pd
import os
import shutil

excel_path = "nomes_cpf.xlsx"
folder_path = "arquivos"
output_folder = "alterados"
log_path = "log_nomes_nao_encontrados.xlsx"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Pasta '{output_folder}' criada.")

try:
    df = pd.read_excel(excel_path, header=None)
    df.columns = ['Nome', 'CPF']
    
    print("=== DEBUG: Lendo arquivo Excel ===")
    print(f"Colunas detectadas: {list(df.columns)}")
    print(f"Total de linhas no Excel: {len(df)}")
    
    nome_cpf_map = {}
    
    for index in range(len(df)):
        row = df.iloc[index]
        nome_original = str(row['Nome']).strip()
        cpf_original = str(row['CPF']).strip()
        
        if pd.notna(row['Nome']) and pd.notna(row['CPF']) and nome_original and cpf_original:
            nome_limpo = nome_original.lower().strip()
            cpf_limpo = cpf_original.replace(".", "").replace("-", "").strip()
            nome_cpf_map[nome_limpo] = cpf_limpo
            print(f"Linha {index + 1}: '{nome_original}' -> '{nome_limpo}' = CPF: {cpf_limpo}")
        else:
            print(f"✗ AVISO: Linha {index + 1} ignorada (Nome ou CPF inválido): Nome='{nome_original}', CPF='{cpf_original}'")
    
    print(f"Total de {len(nome_cpf_map)} nomes carregados do Excel.\n")
    
except FileNotFoundError:
    print(f"Erro: O arquivo {excel_path} não foi encontrado.")
    exit(1)
except Exception as e:
    print(f"Erro ao ler o arquivo Excel: {e}")
    exit(1)

nomes_nao_encontrados = []
arquivos_renomeados = 0
total_arquivos = 0

if not os.path.exists(folder_path):
    print(f"Erro: A pasta {folder_path} não foi encontrada.")
    exit(1)

for arquivo in os.listdir(folder_path):
    if arquivo.lower().endswith((".jpg", ".png", ".pdf")):
        total_arquivos += 1
        nome_sem_extensao = os.path.splitext(arquivo)[0].strip()
        nome_busca = nome_sem_extensao.lower().strip()
        extensao = os.path.splitext(arquivo)[1]
        
        print(f"=== Processando arquivo: {arquivo} ===")
        print(f"Nome sem extensão: '{nome_sem_extensao}'")
        print(f"Nome para busca: '{nome_busca}'")
        
        cpf = nome_cpf_map.get(nome_busca)
        if cpf:
            arquivo_original = os.path.join(folder_path, arquivo)
            arquivo_renomeado = os.path.join(output_folder, cpf + extensao)
            try:
                shutil.copy2(arquivo_original, arquivo_renomeado)
                print(f"✓ SUCESSO: Copiado e renomeado: {arquivo} -> {cpf + extensao}")
                arquivos_renomeados += 1
            except Exception as e:
                print(f"✗ ERRO ao copiar/renomear {arquivo}: {e}")
                nomes_nao_encontrados.append(f"{arquivo} (Erro: {e})")
        else:
            print(f"✗ NÃO ENCONTRADO: '{nome_busca}' não está no mapeamento")
            print("Nomes disponíveis no Excel (primeiros 5):")
            for nome_excel in list(nome_cpf_map.keys())[:5]:
                print(f"  - '{nome_excel}'")
            if len(nome_cpf_map) > 5:
                print(f"  ... e mais {len(nome_cpf_map) - 5} nomes")
            nomes_nao_encontrados.append(arquivo)
        print()

try:
    resumo_data = [
        ["RESUMO DO PROCESSAMENTO", ""],
        ["Total de arquivos processados", total_arquivos],
        ["Arquivos copiados e renomeados com sucesso", arquivos_renomeados],
        ["Arquivos não encontrados/com erro", len(nomes_nao_encontrados)],
        ["", ""],
        ["ARQUIVOS NÃO ENCONTRADOS/COM ERRO", ""]
    ]
    
    for arquivo in nomes_nao_encontrados:
        resumo_data.append([arquivo, ""])
    
    log_df = pd.DataFrame(resumo_data, columns=["Descrição", "Valor"])
    log_df.to_excel(log_path, index=False)
    
    print(f"\n=== RESUMO ===")
    print(f"Total de arquivos processados: {total_arquivos}")
    print(f"Arquivos copiados e renomeados com sucesso: {arquivos_renomeados}")
    print(f"Arquivos não encontrados/com erro: {len(nomes_nao_encontrados)}")
    print(f"Arquivos renomeados salvos na pasta: {output_folder}")
    print(f"Processamento concluído. Log detalhado salvo em: {log_path}")
except Exception as e:
    print(f"Erro ao salvar o log: {e}")