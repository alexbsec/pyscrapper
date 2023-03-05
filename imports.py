import requests
from requests_html import HTML, HTMLSession
from simple_chalk import chalk
import time


def googleScrapper(
    query, 
    brute_search=True, 
    filetype=None, 
    url=None,
    in_url=None,
    in_title=None,
    pages=1,
    verbose=False,
    delay=5):

    google_domains = ('https://www.google.', 
                      'https://google.', 
                      'https://webcache.googleusercontent.', 
                      'http://webcache.googleusercontent.', 
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')

    
    if filetype != None:
        query += f" filetype:{filetype}"
    
    if url != None:
        query += f" url:{url}"

    if in_url != None:
        query += f" inurl:{in_url}"

    if in_title != None:
        query += f" intitle:{in_title}"

    if brute_search:
        query = '"' + query + '"'

    if int(pages) == 1:
        URL = f"https://google.com/search?q={query}"
        res = get_source(URL)
        results = parse_results(res, verbose=verbose)
    elif int(pages) > 1:
        URL = f"https://google.com/search?q={query}&start="
        results = []
        for i in range(1, int(pages)+1):
            tmp_URL = URL + str(i) + '0'
            tmp_res = get_source(tmp_URL)
            tmp_results = parse_results(tmp_res, verbose=verbose)
            results = results + tmp_results
            time.sleep(delay)
    else:
        print("[!] Number of pages cannot be less than 1!")
        exit(1)

    return results

def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Exception caught: {e}")


def parse_results(response, verbose=False):
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".VwiC3b"

    results = response.html.find(css_identifier_result)
    output = []

    for result in results:
        try:
            item = {
                    "title": result.find(css_identifier_title, first=True).text,
                    "link": result.find(css_identifier_link, first=True).attrs['href'],
                    "text": result.find(css_identifier_text, first=True).text
                }
            if verbose:
                print(chalk.green.bold("[+] Found link: ") + chalk.red(item["link"]))
        except:
            pass
            

        output.append(item)

    return output



