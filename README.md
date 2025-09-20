# 🌍 LinguaChain

<div align="center">

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.28+-red.svg)
![LangChain](https://img.shields.io/badge/langchain-latest-green.svg)
![OpenAI](https://img.shields.io/badge/openai-gpt--3.5_turbo-white.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

**Um tradutor inteligente construído com LangChain, OpenAI e Streamlit**

[🚀 Demo Online](https://linguachain.streamlit.app/) • [📖 Documentação](#-instalação-e-uso-local) • [🤝 Contribuir](#-contribuindo)

</div>

---

## 📋 Sobre o Projeto

**LinguaChain** é uma aplicação web inteligente que permite traduzir qualquer texto para o idioma desejado de forma simples e intuitiva. Construída com as mais modernas tecnologias de IA e processamento de linguagem natural, oferece uma experiência de tradução fluida e precisa diretamente no navegador.

### 🎯 Por que usar o LinguaChain?

- **Precisão avançada**: Utiliza a API da OpenAI para traduções contextuais
- **Simplicidade**: Interface limpa e intuitiva construída com Streamlit
- **Flexibilidade**: Traduz para qualquer idioma suportado pela OpenAI
- **Segurança**: Gerenciamento seguro de chaves de API via variáveis de ambiente
- **Rapidez**: Processamento em tempo real com feedback visual

---

## ✨ Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| 📝 **Tradução Universal** | Traduz textos para qualquer idioma com alta precisão |
| 🤖 **IA Avançada** | Integração com LangChain + OpenAI para traduções contextuais |
| ⚡ **Interface Responsiva** | Interface moderna e intuitiva via Streamlit |
| 🔒 **Segurança de API** | Suporte completo a variáveis de ambiente (.env) |
| 🌐 **Deploy Fácil** | Configuração simples para hospedagem no Streamlit Cloud |
| 📱 **Multi-plataforma** | Funciona em qualquer dispositivo com navegador |

---

## 📂 Estrutura do Projeto

```
LinguaChain/
├── 📄 app.py                 # Interface principal em Streamlit
├── 🔧 codigo.py              # Lógica do chain de tradução LangChain
├── 🚫 .gitignore             # Arquivos ignorados (venv, .env, etc.)
├── 📦 requirements.txt       # Dependências do projeto
├── 📖 README.md              # Este arquivo
└── 🔐 .env.example           # Exemplo de configuração de ambiente
```

---

## 🛠️ Instalação e Uso Local

### Pré-requisitos

- Python 3.8 ou superior
- Conta na OpenAI com chave de API
- Git instalado

### 🚀 Passo a passo

#### 1️⃣ Clone o repositório
```bash
git clone https://github.com/jeffersoncampina/LinguaChain.git
cd LinguaChain
```

#### 2️⃣ Crie e ative o ambiente virtual
```bash
# Linux/Mac
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

#### 3️⃣ Instale as dependências
```bash
pip install -r requirements.txt
```

#### 4️⃣ Configure a chave da API
```bash
# Crie um arquivo .env na raiz do projeto
echo "OPENAI_API_KEY=sua_chave_aqui" > .env
```

#### 5️⃣ Execute a aplicação
```bash
streamlit run app.py
```

#### 6️⃣ Acesse no navegador
🎉 **Abra:** [http://localhost:8501](http://localhost:8501)

---

## 🌐 Deploy Online

### Streamlit Cloud (Recomendado)

1. **Suba para o GitHub**: Faça push deste repositório para sua conta GitHub

2. **Acesse o Streamlit Cloud**: Vá para [share.streamlit.io](https://share.streamlit.io)

3. **Conecte sua conta**: Conecte sua conta GitHub

4. **Selecione o repositório**: Escolha **LinguaChain**

5. **Configure as variáveis**: Adicione nas configurações:
   ```
   OPENAI_API_KEY = "sua_chave_aqui"
   ```

6. **Deploy**: Clique em "Deploy" 

🎊 **Pronto!** Você terá um link público para compartilhar sua aplicação.

### Outras opções de deploy
- [Heroku](https://heroku.com)
- [Railway](https://railway.app)
- [Render](https://render.com)
- [Google Cloud Run](https://cloud.google.com/run)

---

## 📸 Preview

<div align="center">

🎬 **Confira a interface do LinguaChain:**

![LinguaChain Demo](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ2FwNDJuanRhNWRjeDRtOG5yMDk2c3NocHZzMWtrdXVpdWRjdXA2biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/zTVHDjLKD36gSflgC7/giphy.gif)

*Tradução rápida e precisa com interface intuitiva*

🌐 **[👉 Experimente a demo online](https://linguachain.streamlit.app/)**

</div>

---

## 🧩 Dependências Principais

| Biblioteca | Versão | Propósito |
|---|---|---|
| `streamlit` | >=1.28.0 | Interface web interativa |
| `langchain` | >=0.0.300 | Framework para aplicações com LLM |
| `openai` | >=1.0.0 | API da OpenAI |
| `python-dotenv` | >=1.0.0 | Gerenciamento de variáveis de ambiente |

---

## 🤝 Contribuindo

Contribuições são sempre bem-vindas! Siga os passos abaixo:

1. **Fork** o projeto
2. Crie uma **branch** para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. **Push** para a branch (`git push origin feature/AmazingFeature`)
5. Abra um **Pull Request**

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 Autor

<div align="center">

**Jefferson Campina**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jeffersoncampina)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jeffersoncampina/)

---

**Feito com 💙 e muito ☕**

⭐ **Se este projeto te ajudou, deixe uma estrela!**

</div>
