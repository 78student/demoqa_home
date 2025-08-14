from pages.swag_labs import SwagLabs
import time

def test_check_icon(browser):
    demo_qa_page = SwagLabs(browser)
    demo_qa_page.visit()
    time.sleep(3)
    assert demo_qa_page.equal_url()
    assert demo_qa_page.exist_icon()

def test_check_username(browser):
    demo_qa_page = SwagLabs(browser)
    demo_qa_page.visit()
    time.sleep(3)
    assert demo_qa_page.equal_url()
    assert demo_qa_page.exist_username()

def test_check_password(browser):
    demo_qa_page = SwagLabs(browser)
    demo_qa_page.visit()
    time.sleep(3)
    assert demo_qa_page.equal_url()
    assert demo_qa_page.exist_password()