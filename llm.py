"""
llm.py — Integração com ChatGPT (OpenAI GPT-3.5-turbo)
Mantém histórico de conversa para contexto multi-turno.
"""
import openai
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Histórico da sessão (memória de conversa)
historico: list[dict] = []


def perguntar(texto: str, idioma_resposta: str = "português") -> str:
    """
    Envia a pergunta ao ChatGPT e retorna a resposta.
    Mantém o histórico para que o modelo lembre do contexto.
    """
    if not historico:
        historico.append({
            "role": "system",
            "content": (
                f"Você é um assistente inteligente, simpático e objetivo. "
                f"Responda sempre em {idioma_resposta}. "
                f"Prefira respostas curtas e diretas quando possível, "
                f"pois elas serão convertidas em áudio."
            )
        })

    historico.append({"role": "user", "content": texto})

    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=historico,
        temperature=0.7,
        max_tokens=300
    )

    conteudo = resposta.choices[0].message.content
    historico.append({"role": "assistant", "content": conteudo})
    return conteudo


def limpar_historico() -> None:
    """Apaga o histórico da sessão atual."""
    historico.clear()


def resumo_historico() -> int:
    """Retorna o número de trocas na conversa atual."""
    trocas = sum(1 for m in historico if m["role"] == "user")
    return trocas
