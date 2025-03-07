import argparse
import csv
from pubmed_fetcher.fetcher import fetch_pubmed_ids, fetch_paper_details

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed research papers.")
    parser.add_argument("query", type=str, help="Search query for PubMed.")
    parser.add_argument("-f", "--file", type=str, help="Output CSV file (optional).")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode.")

    args = parser.parse_args()

    if args.debug:
        print(f"Fetching papers for query: {args.query}")

    pubmed_ids = fetch_pubmed_ids(args.query)
    papers = fetch_paper_details(pubmed_ids)

    if args.file:
        with open(args.file, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["PubMedID", "Title", "Publication Date", "Authors", "Company Affiliation", "Corresponding Author Email"])
            writer.writeheader()
            writer.writerows(papers)
        print(f"Results saved to {args.file}")
    else:
        for paper in papers:
            print(paper)

if __name__ == "__main__":
    main()