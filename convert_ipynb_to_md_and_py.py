# %%
# -*- coding: utf-8 -*-


# %% [markdown]
# # Converter um arquivo do tipo Jupyter Notebook file (`.ipynb`) para Markdown (`.md`) e Python (`.py`)

# %% [markdown]
# ## Resumo
# 
# Este arquivo converte todos os arquivos com o nome `README.ipynb` para `.md` e `.py` a partir da pasta raiz e percorrendo as subpastas.
# 
# ## _Abstract_
# 
# _This file converts all files with the name `README.ipynb` to `.md` and `.py` starting from the root folder and traversing the subfolders._

# %% [markdown]
# # 1. Converter um arquivo do tipo Jupyter Notebook file (`.ipynb`) para Markdown (`.md`) e Python (`.py`)
# 
# Para executar o código fornecido em todos os arquivos `README.ipynb` na pasta raiz e subpastas, você precisará realizar executar o código abaixo. Uma abordagem eficaz é usar o módulo `os` do Python para percorrer todos os diretórios e subdiretórios, encontrando arquivos que correspondam ao nome `README.ipynb`. A seguir, apresento um exemplo de como você pode fazer isso:
# 
# Esse código utiliza `os.walk()` para percorrer todos os diretórios e subdiretórios da pasta atual (indicada por '.'). Ele verifica se algum dos arquivos nos diretórios é um `README.ipynb` e, em seguida, realiza o processo de conversão para Markdown, como especificado no seu código original. O caminho completo do arquivo é usado para garantir que o arquivo correto seja convertido, independente de onde ele esteja na estrutura de pastas.

# %%
# ! pip install nbconvert

# %%
import os
import json

try:
    from nbconvert import MarkdownExporter, PythonExporter  # type: ignore
    _HAVE_NBCONVERT = True
except Exception:  # pragma: no cover - fallback when nbconvert is missing
    _HAVE_NBCONVERT = False

# Definindo o nome do arquivo que deve ser excluído das subpastas
excluded_file = 'convert_ipynb_to_md.ipynb'

# Obtendo o caminho absoluto da pasta raiz
root_path = os.path.abspath('.')

# Funções auxiliares para converter sem nbconvert
def _convert_with_nbconvert(full_path: str) -> None:
    markdown_exporter = MarkdownExporter()
    python_exporter = PythonExporter()

    markdown_code, _ = markdown_exporter.from_filename(full_path)
    python_code, _ = python_exporter.from_filename(full_path)

    markdown_output_filename = full_path.replace('.ipynb', '.md')
    python_output_filename = full_path.replace('.ipynb', '.py')

    with open(markdown_output_filename, 'w', encoding='utf-8') as file:
        file.write(markdown_code)
    with open(python_output_filename, 'w', encoding='utf-8') as file:
        file.write(python_code)

    print(f'{full_path} was successfully converted to {markdown_output_filename} and {python_output_filename}')


def _convert_fallback(full_path: str) -> None:
    with open(full_path, 'r', encoding='utf-8') as file:
        nb = json.load(file)

    md_lines: list[str] = []
    py_lines: list[str] = []

    for cell in nb.get('cells', []):
        source = ''.join(cell.get('source', []))
        if cell.get('cell_type') == 'markdown':
            md_lines.append(source + '\n\n')
            for line in source.splitlines():
                py_lines.append('# ' + line + '\n')
        elif cell.get('cell_type') == 'code':
            md_lines.append('```python\n' + source + '\n```\n\n')
            py_lines.append('\n' + source + '\n')

    markdown_output_filename = full_path.replace('.ipynb', '.md')
    python_output_filename = full_path.replace('.ipynb', '.py')

    with open(markdown_output_filename, 'w', encoding='utf-8') as file:
        file.writelines(md_lines)
    with open(python_output_filename, 'w', encoding='utf-8') as file:
        file.writelines(py_lines)

    print(f'{full_path} was successfully converted to {markdown_output_filename} and {python_output_filename} (fallback)')


def convert_file(full_path: str) -> None:
    if _HAVE_NBCONVERT:
        _convert_with_nbconvert(full_path)
    else:
        _convert_fallback(full_path)


# Percorrendo todos os diretórios e subdiretórios a partir da pasta atual
for dirpath, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        full_path = os.path.join(dirpath, filename)

        if filename == 'README.ipynb':
            convert_file(full_path)

        # Verificando se o arquivo é o que deve ser excluído e se não está na pasta raiz
        elif filename == excluded_file and os.path.abspath(dirpath) != root_path:
            os.remove(full_path)
            print(f'Deleted file: {full_path}')


# %% [markdown]
# ## Referências
# 
# [1] OPENAI.
# ***Converter vários README.ipynb para .md e .py.***
# Disponível em: <https://chat.openai.com/c/50f64d4d-cfe7-40ac-a8aa-27ffa4eb5a5e>.
# ChatGPT.
# Acessado em: 26/01/2024 11:35.
