
# NC COVID-19 college dashboard tracker

A collaborative effort to track COVID-19 data across colleges and universities in North Carolina. Our aim is to work in public, so this project is subject to frequent change.

Want to collaborate? Contact [Tyler Dukes](http://twitter.com/mtdukes).

## Target institutions

For a detailed list of the colleges and universities we're hoping to track, see the `dashboard_details` tab of this [Google Spreadsheet](https://docs.google.com/spreadsheets/d/1Yr1FJcgGgMxFTD8d35LAQHXAuCi4zWTbd5VObVjBFS4/edit?usp=sharing).

To start, we're going to focus on UNC System institutions with simple HTML or HTML table-based dashboards, which are easier to scrape.

Dashboards using Tableau or other visualization software may be a little more difficult, so we're thinking through other potential solutions for those... stay tuned.

## Current contributors
[Tyler Dukes](http://twitter.com/mtdukes), WRAL
[Lucille Sherman](http://twitter.com/_lucysherman), The News & Observer
[Kate Martin](http://twitter.com/katereports), Carolina Public Press

## Methodology
On our first pass, we're going to write simple scrapers using the [Selenium](https://selenium-python.readthedocs.io/) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) libraries in Python, ideally running every TK hours using a cron job. Scrapers will eventually use the [Google Sheets API](https://developers.google.com/sheets/api/guides/concepts) to push to a public repository for data accessible to all.

See the `data_dictionary` tab of [our tracking spreadsheet](https://docs.google.com/spreadsheets/d/1Yr1FJcgGgMxFTD8d35LAQHXAuCi4zWTbd5VObVjBFS4/edit?usp=sharing) to learn more about the layout of our proposed dataset.

## Current scrapers

Here's a list of the current scrapers we have mocked up for the project. This is a work in progress.

### ncsu.py
Scrapes the data dashboard for North Carolina State University formatted as of Aug. 27, 2020.

**Usage**

    python ncsu.py https://www.ncsu.edu/coronavirus/testing-and-tracking/
