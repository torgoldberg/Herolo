from selenium.common.exceptions import NoSuchElementException
from Hero.hero_elemets.hero_main_page_elements import HeroMainPageElements


class UiMainValidations:
    """
    This class will have all hero main validations.
    """

    def verify_element_exist(self):
        """
        This method verify if the UI element exist.
        """
        elements_list = [HeroMainPageElements.get_name_text_box_element(),
                         HeroMainPageElements.get_telephone_text_box_element(),
                         HeroMainPageElements.get_email_text_box_element(),
                         HeroMainPageElements.get_company_text_box_element(),
                         HeroMainPageElements.get_facebook_fotter_button_element(),
                         HeroMainPageElements.get_whatsapp_fotter_button_element(),
                         HeroMainPageElements.get_linkdin_fotter_button_element()]
        for element in elements_list:
            if not element:
                print("no such element")
                try:
                    self.HeroMainPageMethods.close_herolo_pop_up()
                except NoSuchElementException:
                    break
            else:
                print(element, "element found")

