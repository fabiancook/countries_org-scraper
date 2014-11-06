# This is a template for a Python scraper on Morph (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries. You can use whatever libraries are installed
# on Morph for Python (https://github.com/openaustralia/morph-docker-python/blob/master/pip_requirements.txt) and all that matters
# is that your final data is written to an Sqlite database called data.sqlite in the current working directory which
# has at least a table called data.
import scraperwiki
import lxml.html

html = scraperwiki,scrape("http://countrycode.org/")

root = lxml.html.fromstring(html)

i = 0

for tr in root.cssselect("#main_table_blue tbody tr")
    i++
    tds = tr.select("td")

    iso = tds[1].text_content()
    countryCode = tds[2].text_content()

    isoSplit = iso.split('/')

    data = {
        'name': tds[0[.text_content().strip(),
        'countryCode': int(countryCode),
        'countryCodeUnique': i,
        'ISO2': isoSplit[0].strip(),
        'ISO3': isoSplit[1].strip()
    }

