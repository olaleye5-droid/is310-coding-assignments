
# Documenting Gender Inequality in the WNBA

## Project Overview

This project collects and organizes documented events and public accounts related to gender inequality in the Women's National Basketball Association (WNBA). It focuses on preserving the context behind each event instead of labeling a person, team, or game without supporting evidence.

## Research Question

How do documented cases involving gender discrimination, compensation, and working conditions reveal inequalities within the WNBA?

## Research Scope

The project focuses on professional women's basketball in the WNBA. Records may address pregnancy discrimination, compensation, working conditions, media representation, or other issues relevant to gender inequality.

## Data Collection and Inclusion Criteria

Each record should describe a specific event or public account and include a traceable source, such as a credible news article, research publication, official statement, or report.

The dataset records:
- Event title and date
- Team or institution involved
- Issue category
- Source title and URL
- What the source reports
- Documented institutional responses
- Uncertainty and additional context

A source's allegations are distinguished from established findings. A keyword alone is not treated as proof of discrimination. Official statements are identified as the accounts of the organizations that published them.

## Project Files

- `cli_data_entry.py` — Python command-line interface for collecting and reviewing research records.
- `index.html` — Browser-based interface for entering, reviewing, and confirming records.
- `basketball_data.json` — Structured data containing confirmed research records.
- `requirements.txt` — Python package dependencies.
- `README.md` — Project description, research scope, and instructions.

## Python Requirements

The command-line interface uses Python and the Rich library.

## How to Run the Python Interface

From the main `is310-coding-assignments` folder, activate the virtual environment:

```bash
.venv\Scripts\activate.bat
```

Then run:

```bash
python python-scripting\python-libraries\cli_data_entry.py
```

If the virtual environment is already active, run only the Python command.

## How to Run the HTML Interface

Open `index.html` in a web browser. Complete the fields, review each record, confirm it, and use the download button to export the confirmed records as JSON.

## Data Limitations and Ethical Considerations

The dataset is a curated collection, not a complete record of gender inequality in the WNBA. The sources may reflect different perspectives and may not independently establish every allegation.

The project distinguishes reported claims from documented responses and findings. It avoids inferring personal identities and records only details relevant to the research question.

## Reflection on the Interfaces

The Python interface supports structured data entry through the command line. The HTML interface provides a browser-based form with a review and confirmation process.

Both interfaces aim to collect consistent information. Their usefulness can be evaluated by comparing ease of use, clarity of prompts, record accuracy, and the ability to preserve source context.
