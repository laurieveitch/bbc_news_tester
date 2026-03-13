import re
import pytest
import sys
from playwright.sync_api import Page, expect

def test_bbc_homepage(page: Page):
    # Navigate to homepage
    page.goto("https://www.bbc.co.uk/news")

    # Verify page title
    expect(page).to_have_title(re.compile("BBC News", re.IGNORECASE))

    print('Homepage loaded successfully √')

def test_navigation_to_uk_section(page: Page):
    # Starting on homepage
    page.goto("https://www.bbc.co.uk/news")

    page.wait_for_load_state("networkidle")
    
    # DEBUG: Take a screenshot
    page.screenshot(path="debug-homepage.png")
    print("📸 Screenshot saved")
    
    # DEBUG: Find all UK links and print their details
    uk_links = page.get_by_role("link", name=re.compile("UK", re.IGNORECASE)).all()
    print(f"Found {len(uk_links)} links containing 'UK'")
    
    for i, link in enumerate(uk_links):
        print(f"  Link {i+1}:")
        print(f"    Text: '{link.text_content()}'")
        print(f"    URL: '{link.get_attribute('href')}'")
        print(f"    Visible: {link.is_visible()}")
    
    # Try clicking the first visible UK link
    for link in uk_links:
        if link.is_visible():
            print(f"Clicking visible link: '{link.text_content()}'")
            link.click()
            break
    else:
        print("No visible UK links found!")
        # If we get here, take another screenshot
        page.screenshot(path="debug-no-visible-links.png")
        assert False, "No visible UK links found"

    page.wait_for_load_state("networkidle")

    # Checking we're on the correct page via url
    expect(page).to_have_url(re.compile("/news/uk", re.IGNORECASE))
    
    # Checking for 'UK' heading to verify correct page
    expect(page.get_by_role("heading", name="UK", exact=False).first).to_be_visible()

    print('Navigated to UK Section successfully √')



if __name__ == "__main__":
    pytest.main(["-v", "-s", "--headed"])