from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from bs4 import BeautifulSoup
from win11toast import toast


def main():

    url = "https://www.eventim.pl/event/rammstein-europe-stadium-tour-2023-stadion-slaski-15801757"
    notification_message = "Rammstein dostępny!!!"
    ticket_type = 4  # Eventim category - 1
    chromedriver_path = "chromedriver.exe"

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, features="html.parser")
    ticket_category = soup.find_all(class_="event-list-item-wrapper theme-element-border clearfix")
    if len((ticket_category[ticket_type].find_all(class_="ticket-type-unavailable-sec theme-text-color"))) != 1:
        toast(notification_message, 'Click to open url',
              on_click=url)
    else:  # Test lines
        toast("Skrypt działa.")


if __name__ == "__main__":
    main()
