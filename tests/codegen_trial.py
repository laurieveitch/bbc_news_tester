import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.bbc.co.uk/news")
    page.get_by_test_id("navigation").get_by_role("link", name="UK").click()
    page.get_by_test_id("navigation").get_by_role("link", name="Home").click()
    page.get_by_role("link", name="Search BBC").click()
    page.get_by_role("combobox", name="Input your search term").click()
    page.get_by_role("combobox", name="Input your search term").fill("technology")
    page.get_by_role("button", name="Search").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
