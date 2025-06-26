from playwright.sync_api import sync_playwright
import time

_browser = None
_playwright = None
_page = None

def init_browser():
    global _browser, _playwright, _page
    if _browser is None:
        _playwright = sync_playwright().start()
        _browser = _playwright.chromium.launch(headless=False, args=["--start-maximized"])
        context = _browser.new_context(no_viewport=True)
        _page = context.new_page()
        _page.goto("https://www.apollopharmacy.in/")
    return _page

def add_medicine(page, med):    
    search_button = page.locator("text='Search Medicines'")
    search_button.click()
    time.sleep(2)
    
    search_input = page.locator("input[placeholder='Search medicines, brands and more']")
    search_input.fill(med)
    search_input.press('Enter')
    time.sleep(2)
    yield f"{med} found"

    yield from add_to_cart(page)

def add_to_cart(page):
    add_buttons = page.locator("text='Add'")
    if add_buttons.count() == 0:
        yield "No 'Add' button found (product may be unavailable)."
    else:
        add_buttons.first.click()
        yield "Added to cart."
    time.sleep(2)

def open_cart(page):
    cart_btn = page.locator("text='View Cart'")
    cart_btn.click()
    yield "Cart opened."
    
def run(medicines):
    page = init_browser()
    for med in medicines:
        yield from add_medicine(page, med)
    yield from open_cart(page)
    yield "Close the browser using the button below."

def close_browser():
    global _browser, _playwright, _page
    try:
        if _browser:
            _browser.close()
            _browser = None
        if _playwright:
            _playwright.stop()
            _playwright = None
        _page = None
        return "Browser closed."
    except Exception as e:
        return f"Error closing browser: {e}"
