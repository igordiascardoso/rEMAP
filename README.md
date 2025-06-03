# 📋 Renomeador de Arquivos com CPF via Excel

> **Automatize a organização de documentos convertendo nomes para CPFs de forma segura e eficiente**

## 🎯 Sobre o Projeto

Este script Python foi desenvolvido para **automatizar o processo de renomear arquivos com base em um mapeamento entre nomes e CPFs contido em uma planilha Excel**.

**Cenário típico:** Você tem arquivos como `joao_silva.pdf`, `maria_fernanda.jpg`, `carlos_santos.png` e uma planilha Excel que relaciona esses nomes aos CPFs correspondentes. O script usa essa planilha para renomear automaticamente os arquivos para `12345678900.pdf`, `98765432100.jpg`, etc.

### ✨ O que o script faz:
- 📊 Lê uma planilha Excel com o mapeamento nome → CPF
- 🔍 Localiza arquivos na pasta que correspondem aos nomes da planilha
- 📁 Cria cópias dos arquivos renomeados com o CPF correspondente
- 📝 Gera relatório de arquivos que não puderam ser encontrados/renomeados

---

## 🏗️ Estrutura do Projeto

```
📦 Projeto/
├── 🐍 script.py                     # Script principal
├── 📊 nomes_cpf.xlsx               # Planilha com mapeamento
├── 📁 arquivos/                    # Pasta com arquivos originais
│   ├── joao_silva.pdf
│   ├── maria_fernanda.jpg
│   └── carlos_santos.png
├── ✅ alterados/                   # Pasta de saída (criada automaticamente)
│   ├── 12345678900.pdf
│   ├── 98765432100.jpg
│   └── 11122233344.png
└── 📋 log_nomes_nao_encontrados.xlsx # Log de erros
```

---

## 🛠️ Configuração e Instalação

### Pré-requisitos
- **Python 3.7+** instalado no sistema
- Gerenciador de pacotes `pip`

### Instalação das Dependências
```bash
pip install pandas openpyxl
```

---

## 📋 Como Usar

### 1️⃣ **Prepare a Planilha Excel**
Crie o arquivo `nomes_cpf.xlsx` com o seguinte formato:

| Nome               | CPF            |
|--------------------|----------------|
| João da Silva      | 123.456.789-00 |
| Maria Fernanda     | 987.654.321-00 |
| Carlos Santos      | 111.222.333-44 |

### 2️⃣ **Organize os Arquivos**
Coloque todos os arquivos a serem renomeados na pasta `arquivos/`

### 3️⃣ **Execute o Script**
```bash
python script.py
```

### 4️⃣ **Verifique os Resultados**
- ✅ Arquivos renomeados em `alterados/`
- 📋 Log de erros em `log_nomes_nao_encontrados.xlsx`

---

## 🚀 Funcionalidades

| Recurso | Descrição |
|---------|-----------|
| **📄 Múltiplos Formatos** | Suporta `.pdf`, `.jpg`, `.png` |
| **🧹 Limpeza Automática** | Remove espaços e normaliza maiúsculas/minúsculas |
| **🔍 Busca Inteligente** | Ignora diferenças pequenas na formatação dos nomes |
| **📊 Relatório Completo** | Log detalhado de arquivos não encontrados |
| **⚡ Processamento Rápido** | Otimizado para grandes volumes de arquivos |
| **🛡️ Segurança** | Cria cópias, preservando arquivos originais |

---

## ⚠️ Limitações e Considerações

### Limitações Técnicas
- Os nomes na planilha devem corresponder exatamente aos nomes dos arquivos (sem extensão)
- CPF final será usado sem formatação (apenas números)

### 🔒 Segurança e Privacidade

> **⚠️ IMPORTANTE:** Nunca faça upload de planilhas com dados reais (nomes e CPFs verdadeiros) para repositórios públicos. Use sempre dados fictícios ou anonimizados em ambientes de teste.

---

## 🤝 Contribuindo

Contribuições são muito bem-vindas! Aqui estão algumas formas de ajudar:

- 🐛 Reportar bugs através das Issues
- 💡 Sugerir novas funcionalidades
- 🔧 Enviar Pull Requests com melhorias
- 📖 Melhorar a documentação

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License** - veja o arquivo LICENSE para detalhes.

---

## 📞 Suporte

Encontrou algum problema ou tem sugestões? Abra uma **Issue** no repositório ou entre em contato!

---


**⭐ Se este projeto foi útil para você, considere dar uma estrela!**



