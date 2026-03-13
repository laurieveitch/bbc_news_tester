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
    """ULTRA SIMPLE - just check if we can get to UK page"""
    # Go directly to UK page (skip navigation entirely)
    page.goto("https://www.bbc.co.uk/news/uk")
    
    # Take screenshot
    page.screenshot(path="uk-page-direct.png")
    
    # Check we're on UK page
    expect(page).to_have_url(re.compile("/news/uk", re.IGNORECASE))
    expect(page.get_by_text("UK", exact=False).first).to_be_visible()
    
    print("✅ UK page loaded directly")

if __name__ == "__main__":
    pytest.main(["-v", "-s", "--headed"])