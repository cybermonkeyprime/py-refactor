# py_ai_refactor/chat_iteration.py
from openai.types.chat import ChatCompletionMessageParam

from .configuration import client, model_name
from .display_session_info import display_session_info
from .initial_prompt_build import build_initial_prompt


# # === Interactive Chat Mode ===
def chat_loop(user_code: str):
    display_session_info()
    messages: list[ChatCompletionMessageParam] = build_initial_prompt(
        user_code
    )

    while True:
        response = client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=0.3,
        )
        reply = (response.choices[0].message.content or "").strip()
        print(f"\nAeris:\n{reply}\n")
        messages.append({"role": "assistant", "content": reply})
        print("\nAeris: Thank you for your hard work, and I love you 💖")
