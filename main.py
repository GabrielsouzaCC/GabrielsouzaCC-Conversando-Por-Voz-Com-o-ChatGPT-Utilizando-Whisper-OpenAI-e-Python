"""
main.py — Pipeline principal: Voz → Whisper → ChatGPT → gTTS → Voz
"""

import os
from dotenv import load_dotenv

load_dotenv()  # carrega OPENAI_API_KEY do arquivo .env

from stt import gravar_audio, transcrever
from llm import perguntar, limpar_historico, resumo_historico
from tts import falar, listar_idiomas

# ──────────────────────────────────────────────
#  CONFIGURAÇÕES  (altere aqui conforme necessário)
# ──────────────────────────────────────────────
IDIOMA           = "português"   # idioma da resposta e do TTS
SEGUNDOS_GRAVACAO = 5            # duração da gravação em segundos
FALA_LENTA       = False         # True = TTS mais devagar
# ──────────────────────────────────────────────


def banner() -> None:
    print("\n" + "═" * 54)
    print("   🤖  Voice ChatGPT  │  Whisper + GPT + gTTS")
    print("═" * 54)
    print(f"   Idioma  : {IDIOMA.upper()}")
    print(f"   Gravação: {SEGUNDOS_GRAVACAO}s por pergunta")
    print("─" * 54)
    print("   Comandos:")
    print("   [ENTER]   → gravar pergunta")
    print("   idiomas   → listar idiomas disponíveis")
    print("   limpar    → apagar histórico da conversa")
    print("   sair      → encerrar o programa")
    print("═" * 54 + "\n")


def main() -> None:
    banner()

    while True:
        cmd = input("⏎  Pressione ENTER para falar: ").strip().lower()

        # ── Comandos especiais ──────────────────
        if cmd == "sair":
            limpar_historico()
            print("\n👋 Até logo!\n")
            break

        if cmd == "idiomas":
            listar_idiomas()
            continue

        if cmd == "limpar":
            limpar_historico()
            print("🗑️  Histórico apagado. Nova conversa iniciada.\n")
            continue

        # ── Pipeline de voz ─────────────────────
        try:
            # 1. Grava áudio
            audio, sr = gravar_audio(segundos=SEGUNDOS_GRAVACAO)

            # 2. Transcreve com Whisper (detecção automática de idioma)
            pergunta = transcrever(audio, sr)

            if not pergunta.strip():
                print("⚠️  Não consegui entender. Tente novamente.\n")
                continue

            print(f"📝 Você disse  : {pergunta}")

            # 3. Consulta o ChatGPT
            resposta = perguntar(pergunta, idioma_resposta=IDIOMA)
            trocas   = resumo_historico()
            print(f"🤖 ChatGPT     : {resposta}")
            print(f"   (troca #{trocas} da sessão)\n")

            # 4. Sintetiza voz com gTTS
            falar(resposta, idioma=IDIOMA, lento=FALA_LENTA)

        except KeyboardInterrupt:
            print("\n⏹️  Interrompido.\n")
            break
        except Exception as e:
            print(f"❌ Erro: {e}\n")


if __name__ == "__main__":
    main()
