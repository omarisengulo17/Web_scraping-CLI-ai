import json

from lesson7 import (
    run_scraper,
    ask_ai_from_json
)


# ==========================================
# 1. VIEW JOBS
# ==========================================

def view_jobs():

    try:

        with open(
            "all.json",
            "r",
            encoding="utf-8"
        ) as file:

            jobs = json.load(file)

        if not jobs:

            print(
                "\nNo jobs available."
            )

            print(
                "Please scrape jobs first."
            )

            return

        print("\n=== AVAILABLE JOBS ===")

        for job in jobs:

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

    except FileNotFoundError:

        print(
            "\nNo jobs found."
        )

        print(
            "Please scrape jobs first."
        )


# ==========================================
# 2. SEARCH JOBS
# ==========================================

def search_jobs():

    try:

        with open(
            "all.json",
            "r",
            encoding="utf-8"
        ) as file:

            jobs = json.load(file)

        if not jobs:

            print(
                "\nNo jobs available."
            )

            return

        keyword = input(
            "\nSearch jobs: "
        ).strip().lower()

        found_jobs = []

        for job in jobs:

            title = job["title"].lower()

            organization = (
                job["organization"]
                .lower()
            )

            if (
                keyword in title
                or keyword in organization
            ):

                found_jobs.append(job)

        if found_jobs:

            print(
                "\n=== SEARCH RESULTS ==="
            )

            for job in found_jobs:

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

        else:

            print(
                "\nNo jobs found."
            )

    except FileNotFoundError:

        print(
            "\nNo jobs found."
        )

        print(
            "Please scrape jobs first."
        )


# ==========================================
# 3. MAIN CLI
# ==========================================

def main():

    while True:

        print("\n=== JOB SCRAPER ===")
        print("==================")
        print("1. Scrape real jobs")
        print("2. View jobs")
        print("3. Search jobs")
        print("4. Ask AI")
        print("5. Exit")

        choice = input(
            "Choose an option: "
        ).strip()

        if choice == "1":

            run_scraper()

        elif choice == "2":

            view_jobs()

        elif choice == "3":

            search_jobs()

        elif choice == "4":

            ask_ai_from_json()

        elif choice == "5":

            print(
                "\nGoodbye!"
            )

            break

        else:

            print(
                "\nInvalid option."
            )


# ==========================================
# 4. RUN CLI
# ==========================================

if __name__ == "__main__":

    main()