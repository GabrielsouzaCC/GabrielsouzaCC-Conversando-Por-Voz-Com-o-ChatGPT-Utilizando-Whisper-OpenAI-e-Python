"""
tts.py — Text-to-Speech usando Google TTS (gTTS)
Compatível com Windows, Linux e macOS.
"""

from gtts import gTTS
import tempfile
import os
import platform

# Mapeamento de idiomas suportados
IDIOMAS: dict[str, str] = {
    "português": "pt",
    "inglês":    "en",
    "espanhol":  "es",
    "francês":   "fr",
    "alemão":    "de",
    "italiano":  "it",
    "japonês":   "ja",
    "chinês":    "zh",
    "russo":     "ru",
    "árabe":     "ar",
}


def falar(texto: str, idioma: str = "português", lento: bool = False) -> None:
    """
    Converte texto em fala e reproduz o áudio.
    
    Args:
        texto:  Texto a ser falado.
        idioma: Nome do idioma (ver IDIOMAS acima).
        lento:  Se True, fala mais devagar (útil para aprendizado).
    """
    lang = IDIOMAS.get(idioma.lower(), "pt")
    tts  = gTTS(text=texto, lang=lang, slow=lento)

    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        tts.save(f.name)
        _reproduzir(f.name)
        os.unlink(f.name)


def _reproduzir(caminho: str) -> None:
    """Reproduz um arquivo MP3 de acordo com o sistema operacional."""
    sistema = platform.system()
    if sistema == "Darwin":                          # macOS
        os.system(f"afplay '{caminho}'")
    elif sistema == "Linux":
        # Tenta mpg321, cai para ffplay se não estiver instalado
        codigo = os.system(f"mpg321 '{caminho}' 2>/dev/null")
        if codigo != 0:
            os.system(f"ffplay -nodisp -autoexit '{caminho}' 2>/dev/null")
    else:                                            # Windows
        os.system(f'start "" "{caminho}"')
        import time; time.sleep(3)                  # aguarda reprodução


def listar_idiomas() -> None:
    """Imprime os idiomas disponíveis."""
    print("\n Idiomas suportados:")
    for nome, cod in IDIOMAS.items():
        print(f"   {nome:<12} → '{cod}'")
    print()
