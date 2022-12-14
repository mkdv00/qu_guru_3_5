import os

from selene import be, have, command
from selene.support.shared import browser


def test_fill_form(open_browser):
    browser.open("/automation-practice-form")

    browser.element("#firstName").should(be.blank).type("Maks")
    browser.element("#lastName").should(be.blank).type("Kudaev")
    browser.element("#userEmail").should(be.blank).type("maxim.cudaew@gmail.com")
    browser.element("[for=gender-radio-1]").click()
    browser.element("#userNumber").should(be.blank).type("9999999999")
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select>[value="2000"]').click()
    browser.element('.react-datepicker__month-select>[value="1"]').click()
    browser.element('.react-datepicker__day--022').click()
    browser.element("#subjectsInput").type("Computer Science").press_enter()

    ads = browser.all('[id^=google_ads_][id$=container__]')
    ads.should(have.size_less_than_or_equal(3))
    ads.perform(command.js.remove)

    checkboxes = browser.elements(".custom-checkbox label")
    for checkbox in checkboxes:
        checkbox.click()

    browser.element('#uploadPicture').set_value(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'files/photo.jpg')))
    browser.element("#currentAddress").should(be.blank).type("It's my address")
    browser.element("#react-select-3-input").type("NCR").press_enter()
    browser.element("#react-select-4-input").type("Delhi").press_enter()
    browser.element('#submit').press_enter()

    browser.all(".table-responsive td:nth-child(2)").should(have.texts(
        "Maks Kudaev",
        "maxim.cudaew@gmail.com",
        "Male",
        "9999999999",
        "22 February,2000",
        "Computer Science",
        "Sports, Reading, Music",
        "photo.jpg",
        "It's my address",
        "NCR Delhi"
    ))
