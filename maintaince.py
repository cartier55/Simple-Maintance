from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import itertools


class testing(unittest.TestCase):
    # list of Transparency page post xpath values
    posts = []
    # list of the exit button xpath values for the post popup
    exits = []
    # list of correct headings for each post
    intext = []
    # list of the xpath values for the headings of each post to compare to intext list
    compare = []
    errormsgs = []
    @classmethod
    def setUpClass(cls):
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        cls.driver = webdriver.Chrome(PATH)
        cls.driver.maximize_window()
        cls.driver.get('https://www.blackhempfamily.com')
        cls.home = cls.driver.find_element_by_id("idh09fqo0label")
        cls.shop = cls.driver.find_element_by_id("idh09fqo1label")
        cls.why = cls.driver.find_element_by_id("idh09fqo2label")
        cls.tran = cls.driver.find_element_by_xpath('//*[@id="idh09fqo3label"]')
        cls.services = cls.driver.find_element_by_id("idh09fqo5label")
        cls.contact = cls.driver.find_element_by_id("idh09fqo7label")
        cls.facts = cls.driver.find_element_by_id("idh09fqo4label")
        cls.about = cls.driver.find_element_by_id("idh09fqo6label")
    def test_a_nav_menu(self):
        assert "Home" in self.home.text, "Home Button Error"
        assert "Shop" in self.shop.text, "Shop Button Error"
        assert "Why Black Hemp?" in self.why.text, "Why Button Error"
        assert "Transparency" in self.tran.text, "Transparency Button Error"
        assert "Hemp Facts Topics" in self.facts.text, "Facts Button Error"
        assert "Our Services" in self.services.text, "Services Button Error"
        assert "About" in self.about.text, "About Button Error"
        assert "Contact" in self.contact.text, "Contact Button Error"

        hover = ActionChains(self.driver).move_to_element(self.facts)
        hover.perform()
        time.sleep(1.5)
        
        legal = self.driver.find_element_by_id("idh09fqomoreContainer0label")
        vs = self.driver.find_element_by_id("idh09fqomoreContainer1label")
        effects = self.driver.find_element_by_id("idh09fqomoreContainer2label")
        what = self.driver.find_element_by_id("idh09fqomoreContainer3label")
        assert "Legal History" in legal.text, "Legal History Button Error"
        assert "Hemp vs Weed The confusion" in vs.text, "vs Button Error"
        assert "What are the effects of CBD?" in effects.text, "Effects Button Error"
        assert "What is Hemp & CBD" in what.text, "What Button Error"

        hover2 = ActionChains(self.driver).move_to_element(self.about)
        hover2.perform()
        time.sleep(1.5)

        sources = self.driver.find_element_by_id("idh09fqomoreContainer0label")
        assert "Sources" in sources.text, "Source Button Effect"

    def test_b_home_page(self):
        assert "Black Hemp Family" in self.driver.title, "Home Button Link Failed"
        self.driver.find_element_by_xpath('//*[@id="comp-jfmz52xz"]/h2/span/a').click()
        #assert "Essential Oil Facts" in 

    def test_c_shop_page(self):
        self.shop.click()
        time.sleep(3)
        assert "Shop Black Hemp" in self.driver.title, "Shop Button Link Failed"

    def test_d_why_page(self):
        self.why.click()
        time.sleep(3)
        natural_mosisture = self.driver.find_element_by_xpath("//div[@id='comp-jfmyk0fr']").click()
        time.sleep(3)
        title = self.driver.find_element_by_xpath('//*[@id="comp-jvdefy9e"]/h2[1]/span/span/span/span')
        assert "the benefits of natural butters & oils" in title.text, "Natural Moisture Link Failed"
        self.driver.find_element_by_xpath('//*[@id="comp-jvfpdcbwsvgcontent"]').click()

        self.driver.find_element_by_tag_name('body').send_keys(Keys.HOME)
        time.sleep(3)




    def test_e_transparency_page(self):
        self.posts = ['//*[@id="pgi86feccece3844ba09f80aa6696eb037f_0"]',
        '//*[@id="pgibb0246bf32f6468189670ff4c02f48d6_1"]', '//*[@id="pgi561b043aafbf428aa532ca1212803c15_2"]']
        self.compare = ["//span[contains(text(),'what you should know about your CBD oil')]", "//span[contains(text(),'Essential Oil Facts')]",
                                "//span[contains(text(),'the benefits of natural butters & oils')]"]
        self.intext = ["what you should know about your CBD oil", "Essential Oil Facts",
        "the benefits of natural butters & oils", "Hemp Facts Topics"]
        self.exits = ["//*[@id='comp-jvfpiv1wsvgcontent']",
        "//*[@id='comp-jvfii91usvgcontent']", "//*[@id='comp-jvfpdcbwsvgcontent']"]
        self.errormsgs = ["Our Farms Error","Essiental Oil Benifits","Butters and Oils"]
        self.tran.click()
        time.sleep(3)
        assert "Transparency | Black Hemp Family" in self.driver.title, "Transparency Button Link Error"
        time.sleep(5)
        arrow_help = self.driver.find_element_by_xpath('//*[@id="pgibb0246bf32f6468189670ff4c02f48d6_1"]')
        hover3 = ActionChains(self.driver).move_to_element(arrow_help)
        hover3.perform()
        time.sleep(3)
        n_arrow = self.driver.find_element_by_css_selector('div.noop.visual-focus-on:nth-child(5) div.SITE_ROOT:nth-child(4) div.mesh-layout main.pc1:nth-child(3) div.pc1centeredContent div.pc1inlineContent div.style-jvfruku4 div.style-jvfruku4inlineContent div.style-jtkg324h div.comp-jdkrll66 div.pro-gallery:nth-child(3) div:nth-child(1) div.pro-gallery-parent-container.gallery-slider.streched:nth-child(2) div.pro-gallery.inline-styles.one-row.hide-scrollbars.slider.ltr > button.nav-arrows-container.next')
        for (post, c, text, exit_button, error) in zip(self.posts, self.compare, self.intext, self.exits, self.errormsgs):
            self.driver.find_element_by_xpath(post).click()
            time.sleep(3)
            title = self.driver.find_element_by_xpath(c)
            time.sleep(1)
            assert text in title.text, error
            self.driver.find_element_by_xpath(exit_button).click()
            time.sleep(3)
            n_arrow.click()

        cbd_info = self.driver.find_element_by_xpath("//div[@id='pgi6faab6bad5984f57a41cfd82c3623871_3']").click()
        time.sleep(3)
        assert self.intext[3] in self.driver.title, "CBD Info Link Error"

    def test_f_hemp_facts_topics_page(self):
        self.facts.click()
        self.posts = ["//span[@id='comp-jveoeg3x__item-j9pujymdlabel']", "//span[@id='comp-jveoeg3x__item2label']", "//span[@id='comp-jveoeg3x__item-j9pujxu7label']", "//span[@id='comp-jveoeg3x__item1label']"]
        self.intext = ["Legal History", "Hemp vs Weed", "What is Hemp &amp; CBD?", "What are the effects of CBD?"]
        time.sleep(3)
        self.errormsgs = ["Legal History Link Error", "Hemp v Weed Link Error", "Effects of CBD Link Error", "What is Hemp & CBD Link Error"]
        assert "Hemp Facts Topics | Black Hemp Family" in self.driver.title, "Facts Button Link Error"
        for (post, text, error) in zip(self.posts, self.intext, self.errormsgs):
            self.driver.find_element_by_xpath(post).click()
            time.sleep(3)
            assert text in self.driver.page_source, error
            self.driver.back()
            time.sleep(3)
    
    def test_g_services_page():
        self.services.click()
        time.sleep(3)
        assert "Our Services" in self.driver.title, "Services Button Link Error"
        lets_go = self.driver.find_element_by_xpath("//a[@id='comp-kduff175link']")
        assert "Lets go" in lets_go.text, "Lets Go Button Error"
        assert "Business & Branding Sessions" in self.driver.find_element_by_xpath("//span[contains(text(),'Business & Branding Sessions')]").text
        assert "Agriculture & Growing Sessions" in self.driver.find_element_by_xpath("//span[contains(text(),'Agriculture & Growing Sessions')]").text
        assert "" in self.driver.find_element_by_xpath("//span[contains(text(),'Agriculture & Growing Sessions')]").text
        





    @classmethod
    def tearDownClass(cls):
        cls.driver.quit










if __name__ == "__main__":
    unittest.main()


