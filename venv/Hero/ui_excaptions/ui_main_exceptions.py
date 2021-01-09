from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Hero.hero_browser_config.chrome_config import driver, delay


class UiMainExcaptions:
    """
    This class will have all hero main excetions.
    """

    def wait_for_page_exception(self):
        try:
            myElem = WebDriverWait(driver, delay).until(ec.presence_of_element_located((By.ID, 'ElementId')))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")