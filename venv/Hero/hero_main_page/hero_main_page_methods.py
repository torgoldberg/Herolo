from Hero.herolo_browser_config.chrome_config import driver
from Hero.hero_elemets.hero_main_page_elements import HeroMainPageElements


class HeroMainPageMethods:

    def move_to_main_tab(self):
        """"
        this method move back to the hero tab
        """
        AllTabs = driver.window_handles
        for tab in AllTabs:
            if driver.current_url != HeroMainPageElements.get_main_site_page_element():
                driver.switch_to.window(tab)
            break

    def open_main_site_page(self):
        """"
        this method opens hero main site page
        """
        HeroMainPageElements.get_main_site_page_element()
        print("opening main ste page finish in success")

    def click_whatsapp_button(self):
        """"
        this method click the whatsapp redirect image
        """
        whatsapp = HeroMainPageElements.get_whatsapp_fotter_button_element()
        whatsapp.click()
        print("click whatsapp button element finish in success")

    def click_linkdin_button(self):
        """"
        this method click the linkdin redirect image
        """
        linkdin = HeroMainPageElements.get_linkdin_fotter_button_element()
        linkdin.click()
        print("click linkdin button element finish in success")

    def click_facebook_button(self):
        """"
        this method click the facebook redirect image
        """
        facebook = HeroMainPageElements.get_facebook_fotter_button_element()
        facebook.click()
        print("click facebook button element finish in success")

    def close_browser(self):
        """"
        this method close the browser
        """
        HeroMainPageElements.get_close_browser_element()
        print("close browser finish in success")

    def close_herolo_pop_up(self):
        """
        This method validate there are no pop up element blocking the page.
        """
        ClosePopUp = HeroMainPageElements.get_close_pop_up_text_box_element()
        ClosePopUp.click()
        print("close herolo popup finish in success")

    @staticmethod
    def fill_text_box(name=None, company=None, email=None, telephone=None):
        """
        this method responsible for the filling of the text box
        """
        HeroMainPageElements.get_name_text_box_element()
        user_name = HeroMainPageElements.get_name_text_box_element()
        user_name.send_keys(name)
        HeroMainPageElements.get_company_text_box_element()
        company_name = HeroMainPageElements.get_company_text_box_element()
        company_name.send_keys(company)
        HeroMainPageElements.get_email_text_box_element()
        email_address = HeroMainPageElements.get_email_text_box_element()
        email_address.send_keys(email)
        HeroMainPageElements.get_telephone_text_box_element()
        telephone_number = HeroMainPageElements.get_telephone_text_box_element()
        telephone_number.send_keys(telephone)
        print("fill text box finish in success")













