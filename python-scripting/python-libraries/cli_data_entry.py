
import json
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm

console = Console()

DATA_FILE = Path(__file__).with_name("basketball_data.json")

FIELDS = [
    "event_title",
    "date",
    "institution_involved",
    "issue_category",
    "source_title",
    "source_url",
    "source_description",
    "documented_response",
    "uncertainty_context",
]


def collect_record():
    console.print(Panel(
        "Document a sourced account of gender inequality in the WNBA.",
        title="WNBA Research Data Entry"
    ))

    record = {
        "event_title": Prompt.ask("Event title"),
        "date": Prompt.ask("Date or approximate year"),
        "institution_involved": Prompt.ask(
            "WNBA team or institution involved"
        ),
        "issue_category": Prompt.ask(
            "Issue category (compensation, working conditions, "
            "media representation, other)"
        ),
        "source_title": Prompt.ask("Source title"),
        "source_url": Prompt.ask("Source URL"),
        "source_description": Prompt.ask(
            "What does the source report?"
        ),
        "documented_response": Prompt.ask(
            "Documented response (enter 'Not found' if unavailable)"
        ),
        "uncertainty_context": Prompt.ask(
            "Uncertainty or additional context (enter 'None noted' if unavailable)"
        ),
    }

    console.print("\n[bold yellow]Review your record:[/bold yellow]")
    console.print_json(data=record)

    if Confirm.ask("Confirm and save this record?"):
        return record

    console.print("[yellow]Record not saved. You can enter it again.[/yellow]")
    return None


def main():
    records = []

    if DATA_FILE.exists():
        try:
            with DATA_FILE.open("r", encoding="utf-8") as file:
                records = json.load(file)
            if not isinstance(records, list):
                records = []
        except (json.JSONDecodeError, OSError):
            console.print(
                "[yellow]Existing data could not be read. "
                "Starting a new list.[/yellow]"
            )

    while True:
        record = collect_record()

        if record:
            records.append(record)
            with DATA_FILE.open("w", encoding="utf-8") as file:
                json.dump(records, file, indent=2, ensure_ascii=False)
            console.print(
                f"[green]Saved! Total records: {len(records)}[/green]"
            )

        if not Confirm.ask("Enter another record?", default=False):
            break

    console.print(f"\n[bold green]Data saved to:[/bold green] {DATA_FILE}")


if __name__ == "__main__":
    main()
