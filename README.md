# Web Scraping

PR: https://github.com/moayadalhaj/web-scraper/pull/1

## Proplem Domain

Scrape a Wikipedia page and record which passages need citations.

- The web scraper report the number of citations needed.
- The web scraper identify those cases AND include the relevant passage.
- Consider the “relevant passage” to be the parent element that contains the passage, often a paragraph element.

## Implementation

- Create a count function called get_citations_needed_count that takes in a url and returns an integer
- Create function called get_citations_needed_report that takes in a url and returns a string
the string should be formatted with each citation needed on own line, in order found.
