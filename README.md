# Ambiente Conda Controlado - Setor Dados

Este repositório contém o arquivo `environment.yml` que define um ambiente Conda controlado, contendo as bibliotecas necessárias para uso no setor de dados.

---

## Como usar

### Pré-requisitos

- Ter o [Anaconda](https://www.anaconda.com/products/distribution) ou [Miniconda](https://docs.conda.io/en/latest/miniconda.html) instalado no seu computador.
- Ter acesso à internet para baixar os pacotes Conda no primeiro uso.

---

### Passos para criar o ambiente

1. Clone este repositório ou faça o download dos arquivos.
   
2. Criar o ambiente controlado executando o comando abaixo na pasta onde está o arquivo `environment.yml`
   conda env create -f environment.yml

3. Ativar o ambiente
   conda activate setor_dados


Após ativar, você poderá usar as bibliotecas já instaladas conforme o projeto.

Não execute comandos para instalar novas bibliotecas (ex: conda install ou pip install), para manter o ambiente controlado.

Caso precise de alguma biblioteca adicional, solicite à equipe responsável para atualizar o ambiente e o arquivo environment.yml.
