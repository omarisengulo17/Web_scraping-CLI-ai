from bs4 import BeautifulSoup


def scrape_html(html):
    soup = BeautifulSoup(html, "html.parser")

    jobs = soup.select(".opportunity")

    jobs_data = []

    for job in jobs:
        title = job.select_one("h2").text.strip()
        organization = job.select_one(".organization").text.strip()

        jobs_data.append({
            "title": title,
            "organization": organization
        })

    return jobs_data

def scrape_pages(start_page, end_page):
    all_jobs = []

    for page in range(start_page, end_page + 1):
        print(f"Scraping page {page}")

        html = f"""
        <div class="opportunity">
            <h2>Job from page {page}</h2>
            <p class="organization">Company {page}</p>
        </div>
        """

        page_jobs = scrape_html(html)

        print("Page jobs:", page_jobs)

        all_jobs.extend(page_jobs)

    return all_jobs


jobs = scrape_pages(1, 3)

print("All jobs:")
print(jobs)