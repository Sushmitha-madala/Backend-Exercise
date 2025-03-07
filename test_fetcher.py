import unittest
from pubmed_fetcher.fetcher import fetch_pubmed_ids

class TestPubMedFetcher(unittest.TestCase):
    def test_fetch_pubmed_ids(self):
        query = "cancer"
        ids = fetch_pubmed_ids(query, max_results=5)
        self.assertTrue(len(ids) > 0)

if __name__ == "__main__":
    unittest.main()