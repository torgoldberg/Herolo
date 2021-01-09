
class HeroMainPageElements:
    """
    This class will have all hero main page elements.
    """

    @staticmethod
    def get_main_site_page_element():
        """
        This method return herolo site page element.
        """
        HeroMainPage = 'https://automation.herolo.co.il/'
        return driver.get(HeroMainPage)

    @staticmethod
    def get_close_browser_element():
        """
        This method close the browser.
        """
        return driver.quit()

    @staticmethod
    def get_whatsapp_fotter_button_element():
        """
        This method return whatsapp footer image element in hero main site page.
        """
        return driver.find_element_by_xpath("//*[@id='section-contact']/section/div[2]/div/div[2]/div/a[2]")

    @staticmethod
    def get_linkdin_fotter_button_element():
        """
        This method return linkdin footer image element in hero main site page.
        """
        return driver.find_element_by_xpath("//*[@id='section-contact']/section/div[2]/div/div[2]/div/a[1]")

    @staticmethod
    def get_facebook_fotter_button_element():
        """
        This method return facebook footer image element in hero main site page.
        """
        return driver.find_element_by_xpath("//*[@id='section-contact']/section/div[2]/div/div[2]/div/a[3]")

    @staticmethod
    def get_name_text_box_element():
        """
        This method return the name text box element in hero main site page.
        """
        return driver.find_element_by_id("name")

    @staticmethod
    def get_company_text_box_element():
        """
        This method return the company text box element in hero main site page.
        """
        return driver.find_element_by_id("company")

    @staticmethod
    def get_email_text_box_element():
        """
        This method return the email text box element in hero main site page.
        """
        return driver.find_element_by_id("email")

    @staticmethod
    def get_telephone_text_box_element():
        """
        This method return the telephone text box element in hero main site page.
        """
        return driver.find_element_by_id("telephone")

    @staticmethod
    def get_close_pop_up_text_box_element():
        """
        This method return close button of the pop up text box element in hero main site page.
        """
        return driver.find_element_by_xpath("/html/body/div[3]/div/div/div/span")





