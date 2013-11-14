# -*- encoding: utf-8 -*-

from functional_tests import FunctionalTest

class TestHomePage(FunctionalTest):
    def test_can_vieew_home_page(self):
        self.browser.get('http://localhost:8000/shot/')
        
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('bla-bla-bla', body.text)
        
    def test_has_right_title(self):
        title = self.browser.find_element_by_tag_name('title')
        self.assertEqual('Shot', title.text)
        
class TestPrivacyPage(FunctionalTest):

    def setUp(self):
        self.url = 'http://localhost:8000/shot/default/privacy'
        get_browser=self.browser.get(self.url)

    def test_can_view_privacy_page(self):
        response_code = self.get_response_code(self.url)
        self.assertEqual(response_code, 200)

    def test_has_right_title(self):
        title = self.browser.find_element_by_tag_name('title')
        self.assertEqual('Shot Privacy Policy', title.text)

    def test_has_right_heading(self):        
        heading = self.browser.find_element_by_tag_name('h1')
        self.assertIn('Shot Privacy Policy', heading.text)
        
        
class TestAboutPage(FunctionalTest):

    def setUp(self):
        self.url = 'http://localhost:8000/shot/default/about'
        get_browser=self.browser.get(self.url)

    def test_can_view_about_page(self):
        response_code = self.get_response_code(self.url)
        self.assertEqual(response_code, 200)

    def test_has_right_title(self):
        title = self.browser.find_element_by_tag_name('title')
        self.assertEqual('About', title.text)

    def test_has_right_heading(self):        
        heading = self.browser.find_element_by_tag_name('h1')
        self.assertIn('About', heading.text)
