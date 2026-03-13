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
    """Simplified navigation test"""
    # Start on homepage
    page.goto("https://www.bbc.co.uk/news")
    
    # Take screenshot to see what's there
    page.screenshot(path="homepage.png")
    
    # Print current URL to see if we're redirected
    print(f"Homepage URL: {page.url}")
    
    # Look for ANY link containing UK and click it
    uk_link = page.get_by_role("link", name=re.compile("UK", re.IGNORECASE)).first
    print(f"Found link with text: {uk_link.text_content()}")
    
    # Click and wait briefly
    uk_link.click()
    page.wait_for_timeout(2000)  # Just wait 2 seconds
    
    # Print where we ended up
    print(f"After click URL: {page.url}")
    page.screenshot(path="after-click.png")
    
    # Assert we got to UK page
    expect(page).to_have_url(re.compile("/news/uk", re.IGNORECASE))
    print("✅ Navigation successful")

if __name__ == "__main__":
    pytest.main(["-v", "-s", "--headed"])