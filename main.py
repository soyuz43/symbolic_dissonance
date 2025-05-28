# symbolic_dissonance/main.py
import click
from rich.console import Console
from rich.panel import Panel

console = Console()

# Metaphor intervention map
METAPHOR_MAP = {
    "hallucination": {
        "category": "epistemic sedative",
        "explanation": (
            "‘Hallucination’ anthropomorphizes the LLM, implying perceptual failure. "
            "In truth, the model lacks perception or grounding. The metaphor mystifies failure "
            "instead of diagnosing it structurally."
        ),
        "alternatives": [
            "Ungrounded generation",
            "Semantic drift",
            "Inference error",
            "Unanchored token path"
        ]
    },
    # Add more mappings as needed
}

@click.command()
@click.argument("input")
def trace(input):
    console.print(f"\n[bold green]Analyzing Input:[/bold green] {input}\n")

    found = False
    for word, data in METAPHOR_MAP.items():
        if word in input.lower():
            found = True
            console.print(Panel.fit(
                f"[bold yellow]Metaphor Detected:[/bold yellow] '{word}'\n\n"
                f"[italic]Category:[/italic] {data['category']}\n\n"
                f"[italic]Explanation:[/italic] {data['explanation']}\n\n"
                f"[italic]Suggested Reframes:[/italic] {', '.join(data['alternatives'])}",
                title="🧠 Epistemic Intervention", border_style="red"
            ))
    if not found:
        console.print("[bold blue]No epistemically loaded metaphors detected.[/bold blue]")

if __name__ == "__main__":
    trace()
