\# Web Scraping CLI AI



A Python job scraping project that collects real job listings, removes duplicates, stores the data in JSON, provides CLI search functionality, and integrates AI-powered job assistance.



\## Features



\- Real job scraping using Requests and BeautifulSoup

\- Clean and structure scraped job data

\- Remove duplicate job listings

\- Save jobs to JSON

\- View available jobs

\- Search jobs by keyword

\- AI-powered job assistant

\- Environment variables for API key security

\- CLI interface



\## Project Structure



```text

Web\_scraping-CLI-ai/

│

├── cli.py

├── lesson1.py

├── lesson2.py

├── lesson3.py

├── lesson4.py

├── lesson5.py

├── lesson6.py

├── lesson7.py

├── lesson8.py

├── lesson9.py

├── all.json

├── opportunities.json

├── .gitignore

└── .env

Main Files
cli.py

This is the main entry point of the application.

Run the project using:

py cli.py

The CLI provides:

1. Scrape jobs
2. View jobs
3. Search jobs
4. Ask AI
5. Exit

lesson7.py

This file contains the core functionality of the project, including:

Web scraping
HTML parsing
Data cleaning
Duplicate removal
JSON storage
Preparing job data for AI
Creating AI prompts
OpenAI integration
Installation

Clone the repository:

git clone https://github.com/omarisengulo17/Web_scraping-CLI-ai.git

Enter the project directory:
cd Web_scraping-CLI-ai

Create a virtual environment:
py -m venv .venv

Activate it on Windows:

.venv\Scripts\activate

Install dependencies:

pip install requests beautifulsoup4 python-dotenv openai
Environment Variables

Create a .env file in the project root:

OPENAI_API_KEY=your_api_key_here

Never commit your real API key to GitHub.

The .env file is excluded using .gitignore.

**Running the Application**

Start the CLI:

py cli.py

**Choose an option from the menu.**

For example:

=== JOB SCRAPER ===
==================
1. Scrape jobs
2. View jobs
3. Search jobs
4. Ask AI
5. Exit

**Choose an option:**

Select 1 to scrape real jobs.

Select 2 to view saved jobs.

Select 3 to search jobs.

Select 4 to ask the AI assistant questions about the available jobs.

**Technologies**
Python
Requests
BeautifulSoup
JSON
python-dotenv
OpenAI API
Security

API keys and other environment secrets should be stored in .env and must not be committed to the repository.

**Author**

Omarisengulo17
