from pages.swag_labs import SwagLabs
import time

def test_check_icon(browser):
    demo_qa_page = SwagLabs(browser)
    demo_qa_page.visit()
    time.sleep(3)
#    demo_qa_page.click_on_the_icon()
    time.sleep(3)
    assert demo_qa_page.equal_url()
    assert demo_qa_page.exist_icon()
    assert demo_qa_page.exist_username()
    assert demo_qa_page.exist_password()