from selenium import webdriver
import unittest

class CVVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_cv(self):  
        # I want to go and update my cv page. I go
        # to check out my homepage
        self.browser.get('http://127.0.0.1:8000/cv')

        # I notice the title of the website is Georgina Cottrell
        self.assertIn('Georgina Cottrell', self.browser.title)  

        #I am able to see my contact information at the top of the page
        photo=self.browser.find_element_by_tag_name('img')
        self.assertIn('Profile_Picture_.jpg', photo.get_attribute('src'))
        email = self.browser.find_element_by_class_name('email').text
        self.assertEqual(email, 'GMC851@student.bham.ac.uk')
        mobile = self.browser.find_element_by_class_name('mobile').text
        self.assertEqual(mobile, '07496879858')
        #I notice the title of the CV is Georgina Cottrell
        header_text=self.browser.find_element_by_class_name('cv_name').text
        self.assertIn(header_text ,'Georgina Cottrell')

        # I want to now edit my contact information
        self.browser.get('http://127.0.0.1:8000/admin/blog/cv/1/change')
        self.login()
        edit_website =self.browser.find_element_by_class_name('email')
        edit_website.clear()
        edit_website.send_keys("georgina.cottrell@yahoo.co.uk")


        self.fail('Finish the test!')  

    def login(self, username="georginac",password="Poppyandruby1"):
        username_el=self.browser.find_element_by_id("id_username")
        username_el.send_keys(username)
        password_el=self.browser.find_element_by_id("id_password")
        password_el.send_keys(password)

        password_el.submit()

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  
