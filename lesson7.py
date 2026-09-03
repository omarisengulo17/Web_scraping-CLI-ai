from bs4 import BeautifulSoup
import requests
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def clean_text(text):
    return " ".join(text.split())


def fetch_page_safe(url):

    try:

        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=15
        )

        response.raise_for_status()

        print("STATUS:", response.status_code)

        return response.text

    except requests.exceptions.RequestException as error:

        print("Request failed:", error)

        return None

def scrape_html(html):

    soup = BeautifulSoup(html, "html.parser")

    jobs = []

    rows = soup.select("table tbody tr")

    for row in rows:

        cells = row.select("td")

        if not cells:
            continue

        row_text = clean_text(row.get_text(" ", strip=True))

        
        if not row_text:
            continue

        
        links = row.select("a")

        job_link = None

        for link in links:

            link_text = clean_text(link.get_text(" ", strip=True))

            href = link.get("href")

            if href and (
                "detail" in link_text.lower()
                or "apply" in link_text.lower()
                or "vacancy" in href.lower()
            ):

                job_link = href

                break

        title = "Not provided"
        organization = "Not provided"
        deadline = "Not provided"

        cell_texts = []

        for cell in cells:

            text = clean_text(
                cell.get_text(" ", strip=True)
            )

            if text:

                cell_texts.append(text)

        for text in cell_texts:

            if any(month in text.lower() for month in [
                "jan",
                "feb",
                "mar",
                "apr",
                "may",
                "jun",
                "jul",
                "aug",
                "sep",
                "oct",
                "nov",
                "dec"
            ]):

                deadline = text

                break


        image_alt = None

        image = row.select_one("img")

        if image:

            image_alt = image.get("alt")

            if image_alt:

                image_alt = clean_text(image_alt)

        cleaned_text = row_text

        for unwanted in [
            "Details",
            "Apply",
            "Read More"
        ]:

            cleaned_text = cleaned_text.replace(
                unwanted,
                ""
            )

        cleaned_text = clean_text(cleaned_text)


        heading = row.select_one(
            "h1, h2, h3, h4, h5, h6"
        )

        if heading:

            title = clean_text(
                heading.get_text(" ", strip=True)
            )

        if title == "Not provided" and image_alt:

            title = image_alt

        organization_element = row.select_one(
            ".company, "
            ".organization, "
            ".employer, "
            ".company-name"
        )

        if organization_element:

            organization = clean_text(
                organization_element.get_text(
                    " ",
                    strip=True
                )
            )

     
        if title == "Not provided":

            parts = [
                part.strip()
                for part in cleaned_text.split("|")
                if part.strip()
            ]

            if parts:

                title = parts[0]

        if title != "Not provided":

            job = {
                "title": title,
                "organization": organization,
                "location": "Tanzania",
                "deadline": deadline,
                "url": job_link or "Not provided"
            }

            jobs.append(job)

    return jobs

def remove_duplicates(jobs):

    seen = set()

    unique_jobs = []

    for job in jobs:

        key = (
            job["title"].lower()
            + "|"
            + job["organization"].lower()
        )

        if key in seen:

            continue

        seen.add(key)

        unique_jobs.append(job)

    return unique_jobs

def save_to_json(data, filename):

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(
        f"Saved {len(data)} jobs to {filename}"
    )


def load_from_json(filename):

    try:

        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except FileNotFoundError:

        return []

def prepare_jobs_for_ai(jobs):

    jobs_text = ""

    for job in jobs:

        jobs_text += (
            f"Job: {job['title']}\n"
        )

        jobs_text += (
            f"Organization: "
            f"{job['organization']}\n"
        )

        jobs_text += (
            f"Location: "
            f"{job['location']}\n"
        )

        jobs_text += (
            f"Deadline: "
            f"{job.get('deadline', 'Not provided')}\n"
        )

        jobs_text += (
            f"URL: {job['url']}\n\n"
        )

    return jobs_text

def create_ai_prompt(
    jobs_text,
    user_question
):

    prompt = f"""
You are a job assistant.

Here are the available jobs:

{jobs_text}

User question:
{user_question}

Answer based only on the available jobs.

If the requested job does not exist,
clearly say that no matching job was found.

Do not invent jobs or information.
"""

    return prompt

def ask_ai(prompt):

    client = OpenAI()

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    return response.output_text

def run_scraper():

    print("\nStarting REAL scraper...")

    url = (
        "https://www.ajiramarket.co.tz/"
        "public/index.php"
    )

    html = fetch_page_safe(url)

    if html is None:

        print(
            "Could not fetch Ajira Market."
        )

        return []

    jobs = scrape_html(html)

    print(
        f"\nScraped {len(jobs)} jobs."
    )

    unique_jobs = remove_duplicates(jobs)

    print(
        f"After removing duplicates: "
        f"{len(unique_jobs)} jobs."
    )

    save_to_json(
        unique_jobs,
        "all.json"
    )

    print("\n=== SCRAPED JOBS ===")

    for job in unique_jobs[:10]:

        print(
            f"\nTitle: {job['title']}"
        )

        print(
            f"Organization: "
            f"{job['organization']}"
        )

        print(
            f"Location: "
            f"{job['location']}"
        )

        print(
            f"Deadline: "
            f"{job.get('deadline', 'Not provided')}"
        )

        print(
            f"URL: {job['url']}"
        )

    return unique_jobs

def ask_ai_from_json():

    jobs = load_from_json("all.json")

    if not jobs:

        print(
            "\nNo jobs available."
        )

        print(
            "Please scrape jobs first."
        )

        return

    question = input(
        "\nAsk AI: "
    )

    jobs_text = prepare_jobs_for_ai(
        jobs
    )

    prompt = create_ai_prompt(
        jobs_text,
        question
    )

    try:

        answer = ask_ai(prompt)

        print("\n=== AI ANSWER ===")
        print(answer)

    except Exception as error:

        print("\nAI request failed:")
        print(error)

if __name__ == "__main__":

    run_scraper()