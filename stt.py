"""
stt.py — Speech-to-Text usando OpenAI Whisper
"""

import openai
import sounddevice as sd
import soundfile as sf
import tempfile
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def gravar_audio(segundos: int = 5, sample_rate: int = 16000) -> tuple:
    """Grava áudio do microfone e retorna o array de amostras."""
    print(f"Gravando por {segundos}s... fale agora!")
    audio = sd.rec(
        int(segundos * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="float32"
    )
    sd.wait()
    print("Gravação concluída.\n")
    return audio, sample_rate


def transcrever(audio, sample_rate: int, idioma: str = None) -> str:
    """
    Transcreve o áudio usando o modelo Whisper da OpenAI.
    Se 'idioma' for None, o Whisper detecta automaticamente.
    Códigos de idioma: 'pt', 'en', 'es', 'fr', 'de', 'it', 'ja' ...
    """
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        sf.write(f.name, audio, sample_rate)
        with open(f.name, "rb") as af:
            kwargs = {"model": "whisper-1", "file": af}
            if idioma:
                kwargs["language"] = idioma
            resultado = client.audio.transcriptions.create(**kwargs)
        os.unlink(f.name)
    return resultado.text
