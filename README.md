##Instalação e Configuração

##Clone o repositório:
git clone https://github.com/Brunocodigoestudo/Projeto_validador_excel

Configure a versão correta do Python com pyenv:
pyenv install 3.11.5
pyenv local 3.11.5

Instale as dependências do projeto:
python -m venv .venv
# O padrao é utilizar venv
source venv/bin/activate

# Usuários Linux e mac
venv\Scripts\Activate

# Instalar dependências 
pip install -r requirements.txt  