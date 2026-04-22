# Setup do Projeto

Este projeto foi desenvolvido e testado utilizando **Python 3.12.x** e pressupõe o uso de um **ambiente virtual isolado (.venv)** para garantir reprodutibilidade e evitar conflitos de dependências.

> **Pré-requisito**: este guia assume que você já possui o **pyenv** instalado e configurado em sua máquina. Caso não possua, consulte a seção **EXTRA – Primeiro setup em sua máquina** ao final deste documento.

---

## 1. Inicialização do ambiente virtual

Defina a versão do Python utilizada pelo projeto e crie o ambiente virtual local:

```PowerShell
pyenv local 3.12.6
python -m venv .venv
```

Ative o ambiente virtual:

```PowerShell
.venv\Scripts\Activate.ps1
```

Atualize o pip:

```PowerShell
python -m pip install --upgrade pip
python -m pip install --upgrade pip setuptools wheel
```

---

## 2. Instalação das dependências do projeto

Instale as bibliotecas necessárias para execução do projeto:

```PowerShell
pip install -r requirements.txt
```

Registre o kernel do ambiente virtual para uso no Jupyter:

```PowerShell
python -m ipykernel install --user --name venv --display-name "Python (.venv)"
```

**Resultado esperado:**
```text
Installed kernelspec venv in C:\Users\<user>\AppData\Roaming\jupyter\kernels\venv
```

---

## 3. Validações iniciais do ambiente

Verifique se o Python ativo pertence ao ambiente virtual:

```PowerShell
python -c "import sys; print(sys.executable)"
```

**Resultado esperado:**
```text
...\seu_projeto\.venv\Scripts\python.exe
```

Essa validação garante que o projeto será executado com o interpretador correto.

---

## 4. Premissas técnicas do projeto

- As bibliotecas abaixo fazem parte da **biblioteca padrão do Python** e **não devem ser instaladas via pip**:
  - pathlib
  - datetime
  - typing

- O projeto foi desenvolvido e validado exclusivamente com **Python 3.12.x**
- Recomenda-se fortemente manter a execução sempre dentro do ambiente virtual `.venv`

## Troubleshooting

### Recriação do ambiente virtual

Caso ocorram erros relacionados a dependências, kernel ou versão do Python, recrie o ambiente virtual:

```PowerShell
deactivate
Remove-Item .venv -Recurse -Force
```

Em seguida, repita o processo descrito na **Seção 1**.

---

## EXTRA – Primeiro setup em sua máquina (pyenv-win)

Repositório oficial:
https://github.com/pyenv-win/pyenv-win

Instale o **pyenv-win** no PowerShell:

```powershell
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
```

Reabra o PowerShell e valide a instalação:

```PowerShell
pyenv --version
```

Liste as versões disponíveis do Python:

```PowerShell
pyenv install -l
```

Instale uma versão específica:

```PowerShell
pyenv install <versão>
```

Defina a versão global do Python:

```PowerShell
pyenv global <versão>
```

Verifique a versão ativa e o caminho do interpretador:

```PowerShell
pyenv version
```

**Saída esperada:**
```text
<versão> (set by \path\to\.pyenv\pyenv-win\.python-version)
```

Valide o funcionamento do Python:

```PowerShell
python -c "import sys; print(sys.executable)"
```

**Resultado esperado:**
```text
\path\to\.pyenv\pyenv-win\versions\<versão>\python.exe
```

