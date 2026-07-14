# 🤖 Voice ChatGPT — Whisper + GPT + gTTS

Converse **por voz** com o ChatGPT em múltiplos idiomas, diretamente pelo terminal.

> Projeto desenvolvido como desafio da [DIO](https://www.dio.me) — Bootcamp de IA com Python.

---

## 🏗️ Arquitetura

```
Microfone
    │
    ▼
🎙️ Gravação (sounddevice)
    │
    ▼
📝 Transcrição (OpenAI Whisper)
    │
    ▼
🧠 Resposta (OpenAI GPT-3.5-turbo)
    │
    ▼
🔊 Síntese de voz (Google TTS)
    │
    ▼
Alto-falante
```

---

## ✨ Diferenciais deste projeto

| Recurso | Descrição |
|---------|-----------|
| 🧠 Memória de conversa | O ChatGPT lembra o contexto da sessão inteira |
| 🌍 10 idiomas no TTS | PT, EN, ES, FR, DE, IT, JA, ZH, RU, AR |
| 🖥️ Multi-plataforma | Windows, Linux e macOS |
| 🔐 Chave segura | API key via `.env`, nunca no código |
| 🗂️ Arquitetura modular | `stt.py`, `llm.py`, `tts.py` separados |
| ⌨️ Comandos no terminal | `limpar`, `idiomas`, `sair` |

---

## 🚀 Como rodar

### 1. Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/voice-chatgpt.git
cd voice-chatgpt
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

> **Linux** — instale também o player de áudio:
> ```bash
> sudo apt install mpg321
> # ou
> sudo apt install ffmpeg
> ```

### 3. Configure sua chave da OpenAI
```bash
cp .env.example .env
# Edite o arquivo .env e cole sua chave:
# OPENAI_API_KEY=sk-...
```

> Obtenha sua chave em: https://platform.openai.com/api-keys

### 4. Execute
```bash
python src/main.py
```

---

## 🎮 Comandos disponíveis

| Comando | Ação |
|---------|------|
| `ENTER` | Iniciar gravação da pergunta |
| `idiomas` | Listar idiomas disponíveis no TTS |
| `limpar` | Apagar histórico e iniciar nova conversa |
| `sair` | Encerrar o programa |

---

## 🌍 Idiomas suportados

| Nome | Código |
|------|--------|
| Português | `pt` |
| Inglês | `en` |
| Espanhol | `es` |
| Francês | `fr` |
| Alemão | `de` |
| Italiano | `it` |
| Japonês | `ja` |
| Chinês | `zh` |
| Russo | `ru` |
| Árabe | `ar` |

Para trocar o idioma, edite a variável `IDIOMA` no topo do `src/main.py`.

---

## 🛠️ Tecnologias

- [OpenAI Whisper](https://openai.com/research/whisper) — reconhecimento de fala
- [OpenAI GPT-3.5-turbo](https://platform.openai.com/docs/models) — modelo de linguagem
- [gTTS](https://gtts.readthedocs.io/) — síntese de voz via Google
- [sounddevice](https://python-sounddevice.readthedocs.io/) — captura de áudio
- [python-dotenv](https://pypi.org/project/python-dotenv/) — gerenciamento de variáveis de ambiente

---

## 📁 Estrutura do projeto

```
voice-chatgpt/
├── src/
│   ├── main.py        # Pipeline principal
│   ├── stt.py         # Speech-to-Text (Whisper)
│   ├── llm.py         # ChatGPT + histórico
│   └── tts.py         # Text-to-Speech (gTTS)
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## 📚 Referências

- [Artigo DIO — Conversando por voz com o ChatGPT](https://web.dio.me/articles/conversando-por-voz-com-o-chatgpt-utilizando-whisper-openai-e-python)
- [Código original no Google Colab](https://bit.ly/41XfKaM)
- [Live no YouTube da DIO](https://bit.ly/44e9Nrw)

---

## 📝 Licença

MIT © 2024
