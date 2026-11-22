import os
from pathlib import Path

from dotenv import load_dotenv
from openai import APIError, APIStatusError, OpenAI

HERE = Path(__file__).parent
load_dotenv(HERE / ".env")

client = OpenAI(
    api_key=os.environ["LLM_API_KEY"],
    base_url=os.environ["LLM_BASE_URL"],
    timeout=90,
    max_retries=0,
)
MODEL = os.environ["LLM_MODEL"]
MAX_OUTPUT_TOKENS = 800  # safety cap only; with the short-answer rule replies are ~30–100 tokens


def build_system_prompt() -> str:
    instructions = (HERE / "prompts" / "system.md").read_text(encoding="utf-8")
    knowledge = (HERE / "knowledge" / "codeart.md").read_text(encoding="utf-8")
    return f"{instructions}\n\n<codeart_website>\n{knowledge}\n</codeart_website>"


SYSTEM_PROMPT = build_system_prompt()


def ask(history: list[dict], user_text: str):
    """History (user/assistant only) + new message -> answer, finish reason, usage."""
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *history,
        {"role": "user", "content": user_text},
    ]
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        max_completion_tokens=MAX_OUTPUT_TOKENS,
    )
    choice = response.choices[0]
    return choice.message.content, choice.finish_reason, response.usage


def print_usage(usage) -> None:
    details = usage.prompt_tokens_details
    cached = (details.cached_tokens or 0) if details else 0
    print(f"[tokens] input={usage.prompt_tokens} (cached {cached}) output={usage.completion_tokens}")


def main() -> None:
    history: list[dict] = []
    print("Codeart assistant. Type 'exit' to quit.")

    while True:
        user_text = input("\nYou: ").strip()
        if user_text.lower() in {"exit", "quit"}:
            break
        if not user_text:
            continue

        try:
            answer, finish_reason, usage = ask(history, user_text)
        except APIStatusError as e:  # the server answered with an error: 400, 429, 503...
            print(f"API error {e.status_code}: {e.response.text}")
            continue
        except APIError as e:  # no answer at all: timeout, connection
            print(f"API error: {e}")
            continue

        history.append({"role": "user", "content": user_text})
        history.append({"role": "assistant", "content": answer})

        print(f"\nAssistant: {answer}")
        if finish_reason == "length":
            print("[warning] answer was cut off by the token limit")
        if usage:
            print_usage(usage)


if __name__ == "__main__":
    main()