from Hero.hero_main_page.hero_main_page_methods import HeroMainPageMethods
from Hero.hero_validations.ui_main_validations import UiMainValidations


class HeroMainPageTest:

    def test_sanity(self):
        USER_1_INFO = ['tor1', 'hero1', 'test1@gmail.com', '0543384731']
        HeroMainPageMethods.open_main_site_page(self)
        HeroMainPageMethods.fill_text_box(name=USER_1_INFO[0], company=USER_1_INFO[1], email=USER_1_INFO[2],
                                          telephone=USER_1_INFO[3])
        UiMainValidations.verify_element_exist(self)
        HeroMainPageMethods.click_whatsapp_button(self)
        HeroMainPageMethods.move_to_main_tab(self)
        HeroMainPageMethods.click_linkdin_button(self)
        HeroMainPageMethods.move_to_main_tab(self)
        HeroMainPageMethods.click_facebook_button(self)
        HeroMainPageMethods.move_to_main_tab(self)
        HeroMainPageMethods.close_browser(self)


x = HeroMainPageTest()
x.test_sanity()
