# CEFET

Import.

##Como desenvolver?

1. Clone o repositório.
2. Crie um vitualenv com python 3.5.2
3. Ative o vitrualenv.
4. Insntale as dependências.
5. Configure a instância com o .env

```console
git clone git@github.com:iuryamorim/reportGenerator.git reportGenerator
cd reportGenerator
python -m venv .reportGenerator
source .reportGenerator/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
```