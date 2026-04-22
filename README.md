# OSINT Profile Builder

## Overview

OSINT Profile Builder is a Python-based tool designed to extract and structure publicly available information from developer profiles on GitHub. The project focuses on automating the collection of relevant user metadata and presenting it in a structured and analyzable format.

Rather than replacing manual profile lookup, the tool demonstrates how publicly accessible data can be programmatically aggregated and processed for basic open-source intelligence (OSINT) workflows.

---

## Objectives

* Automate extraction of publicly available profile data
* Structure unorganized web data into meaningful formats
* Enable batch processing for multiple usernames
* Provide exportable outputs for further analysis

---

## Features

* Extracts GitHub profile information including:

  * Name
  * Bio
  * Followers and following count
  * Repository count
* Retrieves a list of repositories associated with the user
* Supports batch processing of multiple usernames
* Exports structured data in JSON format
* Modular design for extending support to additional platforms

---

## Technologies Used

* Python
* requests
* BeautifulSoup (bs4)

---

## Methodology

1. Accepts one or more GitHub usernames as input
2. Sends HTTP requests to user profile and repository pages
3. Parses HTML content using BeautifulSoup
4. Extracts relevant metadata using targeted selectors
5. Structures extracted data into dictionaries
6. Outputs results to the console and exports to JSON

---

## Usage

### 1. Clone the repository

```bash
git clone https://github.com/divyanshigupta31/osint-profile-builder.git
cd osint-profile-builder
```

### 2. Install dependencies

```bash
pip install requests beautifulsoup4
```

### 3. Run the program

```bash
python main.py
```

### 4. Input format

Provide one or more usernames separated by commas:

```
username1, username2, username3
```

---

## Example Output

```
===== OSINT PROFILE =====

Platform: GitHub
Name: John Doe
Bio: Developer and Open Source Contributor
Followers: 120
Following: 45
Repositories:
- project-one
- project-two
- project-three
Profile: https://github.com/johndoe
```

---

## Output Files

* Individual or aggregated profile data is exported as JSON
* JSON files are generated locally and excluded from version control using `.gitignore`

---

## Use Cases

* Basic OSINT and reconnaissance workflows
* Automated developer profile summarization
* Batch analysis of multiple GitHub users
* Data collection for further processing or visualization

---

## Limitations

* Relies on HTML structure of GitHub pages, which may change over time
* Does not use official APIs, which may impact reliability
* Limited to publicly accessible information
* Repository extraction is restricted to a subset for performance and clarity

---

## Future Improvements

* Integration with GitHub API for improved reliability
* Support for additional platforms
* Enhanced data extraction (languages, contributions, etc.)
* Command-line interface with argument support
* Data visualization and reporting features

---

## Project Scope

This project is intended as an introductory implementation of OSINT concepts using web scraping techniques. It emphasizes understanding data extraction, structuring, and automation rather than building a production-grade intelligence system.

---

## Author

Developed as part of a practical exploration into cybersecurity and open-source intelligence techniques.
