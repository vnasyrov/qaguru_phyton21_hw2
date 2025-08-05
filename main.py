from selene import browser, be, have

def test_input_value():
    browser.open('https://ya.ru')
    browser.element('[id="text"]').type('погода спб').press_enter()
    browser.element('input[name="text"]').should(have.value('погода спб'))