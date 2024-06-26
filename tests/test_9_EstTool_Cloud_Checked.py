import re
from playwright.sync_api import Page, expect

# This test is to check that the page loads, labels, scroll bars, dropdowns are all visible and set at the default when page loads
# Cloud Checked
# Calcs match spreadsheet


def test_example(page: Page) -> None:
    # page.goto("http://localhost:57056/")
    page.goto("http://localhost:4200/")
    
    page.set_viewport_size({"width": 1920, "height": 1200})
    expect(page.get_by_role("heading", name="Carbon Estimator")).to_be_visible()
    
    #Organisation
    expect(page.get_by_label("How many employees are in the")).to_have_value("100");
    expect(page.get_by_text("What percentage of those")).to_be_visible()
    expect(page.get_by_text("Desktops 50%")).to_be_visible()
    expect(page.get_by_text("Laptops 50%")).to_be_visible()
    
    # On Prem Servers
    expect(page.get_by_role("heading", name="On-Premise Servers")).to_be_visible()
    expect(page.get_by_text("We'll use the number of")).to_be_visible()
    expect(page.get_by_text("How many on-premise servers")).to_be_visible()
    expect(page.locator("label").filter(has_text="I don't know")).to_be_visible()
    # Check "I don't know"
    page.get_by_label("I don't know").check()
    expect(page.get_by_text("We'll make an assumption")).to_be_visible()
    expect(page.get_by_text("Number of Servers:")).to_be_visible()
    expect(page.get_by_label("Number of Servers:")).to_be_disabled()
    page.get_by_label("Where are they primarily").select_option("GBR")
    page.get_by_label("Where are they primarily").select_option("WORLD")
    
    # Cloud
    expect(page.get_by_role("heading", name="Cloud Services")).to_be_visible()
    expect(page.get_by_text("Tell us about your cloud")).to_be_visible()
    expect(page.get_by_text("We don't use cloud services")).to_be_visible()
    # Check "We don't use cloud services"
    expect(page.get_by_label("We don't use cloud services")).not_to_be_checked()
    page.get_by_label("We don't use cloud services").check()
    expect(page.get_by_label("We don't use cloud services")).to_be_checked()
    expect(page.get_by_text("What percentage of your servers are cloud services vs on-premise?")).not_to_be_visible()
    
    # Users
    expect(page.get_by_role("heading", name="End-Users")).to_be_visible()
    expect(page.get_by_text("Tell us about your end-users -")).to_be_visible()
    expect(page.get_by_text("Where are your end-users")).to_be_visible()
    page.get_by_label("Where are your end-users primarily located?", exact=True).select_option("Globally")
    expect(page.get_by_text("How many monthly active users")).to_be_visible()
    expect(page.get_by_label("How many monthly active users")).to_have_value("100");
    expect(page.get_by_text("What percentage of your end-users")).to_be_visible()
    expect(page.get_by_text("Mobile 50%")).to_be_visible()
    expect(page.get_by_text("Computer 50%")).to_be_visible()
    expect(page.get_by_text("What's the primary purpose of")).to_be_visible()
    page.get_by_label("What's the primary purpose of").select_option("socialMedia")
    page.get_by_label("What's the primary purpose of").select_option("average")
   
    
    # Calculate
    # Calculate outcome and make sure it matches spreadsheet
    page.get_by_role("button", name="Calculate").click()
    expect(page.locator("foreignobject")).to_contain_text("Upstream Emissions - 26%")
    expect(page.locator("foreignobject")).to_contain_text("Direct Emissions - 74%")
    expect(page.locator("foreignobject")).to_contain_text("Downstream Emissions - <1%")
    

    
    ##############################################################################

