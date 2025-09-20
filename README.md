## 📑 Idiomas | Languages
- <a href="#-sobre-o-projeto"><img src="https://flagcdn.com/w20/br.png" alt="Brasil"> Português</a>
- <a href="#-linguachain---english-version"><img src="https://flagcdn.com/w20/us.png" alt="English"> English</a>

<br><br><br>
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

<div align="center">
  <img src="assets/linguachain-image.gif" width="400"/>
</div>

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

---

<br><br><br>

# 🌍 LinguaChain - English Version

<div align="center">

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.28+-red.svg)
![LangChain](https://img.shields.io/badge/langchain-latest-green.svg)
![OpenAI](https://img.shields.io/badge/openai-gpt--3.5_turbo-white.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

**An intelligent translator built with LangChain, OpenAI and Streamlit**

[🚀 Live Demo](https://linguachain.streamlit.app/) • [📖 Documentation](#-installation-and-local-usage) • [🤝 Contributing](#-contributing-1)

</div>

---

## 📋 About the Project

**LinguaChain** is an intelligent web application that allows you to translate any text to your desired language in a simple and intuitive way. Built with the most modern AI and natural language processing technologies, it offers a smooth and accurate translation experience directly in your browser.

### 🎯 Why use LinguaChain?

- **Advanced precision**: Uses OpenAI API for contextual translations
- **Simplicity**: Clean and intuitive interface built with Streamlit
- **Flexibility**: Translates to any language supported by OpenAI
- **Security**: Secure API key management via environment variables
- **Speed**: Real-time processing with visual feedback

---

## ✨ Features

| Feature | Description |
|---|---|
| 📝 **Universal Translation** | Translates texts to any language with high precision |
| 🤖 **Advanced AI** | Integration with LangChain + OpenAI for contextual translations |
| ⚡ **Responsive Interface** | Modern and intuitive interface via Streamlit |
| 🔒 **API Security** | Full support for environment variables (.env) |
| 🌐 **Easy Deploy** | Simple configuration for hosting on Streamlit Cloud |
| 📱 **Multi-platform** | Works on any device with a browser |

---

## 📂 Project Structure

```
LinguaChain/
├── 📄 app.py                 # Main Streamlit interface
├── 🔧 codigo.py              # LangChain translation chain logic
├── 🚫 .gitignore             # Ignored files (venv, .env, etc.)
├── 📦 requirements.txt       # Project dependencies
├── 📖 README.md              # This file
└── 🔐 .env.example           # Environment configuration example
```

---

## 🛠️ Installation and Local Usage

### Prerequisites

- Python 3.8 or higher
- OpenAI account with API key
- Git installed

### 🚀 Step by step

#### 1️⃣ Clone the repository
```bash
git clone https://github.com/jeffersoncampina/LinguaChain.git
cd LinguaChain
```

#### 2️⃣ Create and activate virtual environment
```bash
# Linux/Mac
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

#### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

#### 4️⃣ Configure API key
```bash
# Create a .env file in the project root
echo "OPENAI_API_KEY=your_key_here" > .env
```

#### 5️⃣ Run the application
```bash
streamlit run app.py
```

#### 6️⃣ Access in browser
🎉 **Open:** [http://localhost:8501](http://localhost:8501)

---

## 🌐 Online Deploy

### Streamlit Cloud (Recommended)

1. **Push to GitHub**: Push this repository to your GitHub account

2. **Access Streamlit Cloud**: Go to [share.streamlit.io](https://share.streamlit.io)

3. **Connect your account**: Connect your GitHub account

4. **Select repository**: Choose **LinguaChain**

5. **Configure variables**: Add in settings:
   ```
   OPENAI_API_KEY = "your_key_here"
   ```

6. **Deploy**: Click "Deploy" 

🎊 **Done!** You'll have a public link to share your application.

### Other deploy options
- [Heroku](https://heroku.com)
- [Railway](https://railway.app)
- [Render](https://render.com)
- [Google Cloud Run](https://cloud.google.com/run)

---

## 📸 Preview

<div align="center">

🎬 **Check out the LinguaChain interface:**

<div align="center">
  <img src="assets/linguachain-image.gif" width="400"/>
</div>

*Fast and accurate translation with intuitive interface*

🌐 **[👉 Try the online demo](https://linguachain.streamlit.app/)**

</div>

---

## 🧩 Main Dependencies

| Library | Version | Purpose |
|---|---|---|
| `streamlit` | >=1.28.0 | Interactive web interface |
| `langchain` | >=0.0.300 | Framework for LLM applications |
| `openai` | >=1.0.0 | OpenAI API |
| `python-dotenv` | >=1.0.0 | Environment variables management |

---

## 🤝 Contributing

Contributions are always welcome! Follow the steps below:

1. **Fork** the project
2. Create a **branch** for your feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. Open a **Pull Request**

---

## 📝 License

This project is under the MIT license. See the [LICENSE](LICENSE) file for more details.

---

## 👨‍💻 Author

<div align="center">

**Jefferson Campina**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jeffersoncampina)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jeffersoncampina/)

---

**Made with 💙 and lots of ☕**

⭐ **If this project helped you, leave a star!**

</div>
