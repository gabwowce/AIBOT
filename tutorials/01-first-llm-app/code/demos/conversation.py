"""Demo for filming (D5, D9): a scripted English conversation.

The questions are "typed" automatically, but every answer and token count
comes from a real call to main.ask(). Run from the code/ folder:

    uv run demos/conversation.py
"""
import random
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from openai import RateLimitError  # noqa: E402

from main import ask, print_usage  # noqa: E402

# Free tier allows a limited number of tokens per minute, and every turn
# sends ~62k. The pause keeps us under it; cut the waiting out when editing.
PAUSE_BETWEEN_TURNS = 20

TURNS = [
    "How much would an app cost where I can track all my sent parcels in one place?",
    "I'd like the statuses to update automatically from the couriers. We use Omniva and DPD.",
    "Around 200 parcels a month, just me and one colleague using it.",
    "ok",
    "And how long would it take?",
]


def type_out(text: str) -> None:
    """Print text like a person typing it."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(random.uniform(0.02, 0.06))
    print()


def main() -> None:
    history: list[dict] = []
    print("Codeart assistant. Type 'exit' to quit.")
    time.sleep(1.5)

    for user_text in TURNS:
        sys.stdout.write("\nYou: ")
        sys.stdout.flush()
        time.sleep(0.6)
        type_out(user_text)

        while True:
            try:
                answer, finish_reason, usage = ask(history, user_text)
                break
            except RateLimitError:
                print("[rate limit: free tier tokens per minute used up, waiting 30 s]")
                time.sleep(30)
        history.append({"role": "user", "content": user_text})
        history.append({"role": "assistant", "content": answer})

        print(f"\nAssistant: {answer.strip()}")
        if finish_reason == "length":
            print("[warning] answer was cut off by the token limit")
        if usage:
            print_usage(usage)
        time.sleep(PAUSE_BETWEEN_TURNS)

    print()


if __name__ == "__main__":
    main()
