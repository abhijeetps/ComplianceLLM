from bs4 import BeautifulSoup
import requests

def scrap_compliance_website(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        compliance_policy = soup.select('article#content').pop().get_text(separator='\n', strip=True)
        return compliance_policy
    except Exception as e:
        print(f"Exception occured while trying to fetch compliance policy: #{e}")

def scrap_test_website(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        to_test = soup.select('body').pop().get_text(separator='\n', strip=True)
        return to_test
    except Exception as e:
        print(f"Exception occured while trying to fetch test website : #{e}")


def scrap(url, type="to_test_website"):
    if type == "compliance_website":
        return scrap_compliance_website(url)
    elif type == "to_test_website":
        return scrap_test_website(url)
