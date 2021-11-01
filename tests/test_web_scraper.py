from web_scraper import __version__
from web_scraper.scraper import get_citations_needed_count as counts, get_citations_needed_report as report

def test_version():
    assert __version__ == '0.1.0'

def test_count():
    expected = 5
    actual = counts("https://en.wikipedia.org/wiki/History_of_Mexico")
    assert  actual == expected

def test_report():
    expected = 'The first people to settle in Mexico encountered'
    actual = report("https://en.wikipedia.org/wiki/History_of_Mexico")[:48]
    assert actual == expected

def test_report2():
    expected = 'The Mexica people arrived in the Valley of Mexico in 1248 AD.'
    location = report("https://en.wikipedia.org/wiki/History_of_Mexico").find('The Mexica')
    actual = report("https://en.wikipedia.org/wiki/History_of_Mexico")[location:location+61]
    assert actual == expected
