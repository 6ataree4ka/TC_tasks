from behave import *
from pages.main_page import MainPage
from pages.review_page import ReviewPage
from pages.car_page import CarPage
from pages.overview_page import OverviewPage
from pages.compare_page import ComparePage
from car import Car


@given("I have no cars to compare")
def step(context):
    context.cars = []

@when("I select two random cars with parameters present")
def step(context):
    while len(context.cars) < 2:
        main_page = MainPage()
        main_page.open_menu()
        main_page.select_menu_item()

        review_page = ReviewPage()

        context.brand, context.model, context.year = review_page.select_random_car()
        review_page.view_car()

        car_page = CarPage(car_brand=context.brand, car_model=context.model, car_year=context.year)
        car_page.switch_to_tab()

        context.overview_page = OverviewPage(
            car_brand=context.brand, car_model=context.model, car_year=context.year)

        context.engines, context.transmissions = context.overview_page.get_engines_and_transmissions()

        car = Car(context.brand, context.model, context.year, context.engines, context.transmissions)

        if context.overview_page.is_compare_possible() == True and context.overview_page.are_characteristics_present() == True:
            context.cars.append(car)

@when("I click Compare Side by Side button on second car")
def step(context):
    if len(context.cars) == 2:
        context.overview_page.compare()

@when("Compare page opens")
def step(context):
    context.compare_page = ComparePage()

@when("I enter first car data and click Compare button")
def step(context):
    context.compare_page.select_necessary_car(
            context.cars[0].brand, context.cars[0].model, context.cars[0].year)
    context.first_car_engines, context.second_car_engines, \
    context.first_car_transmissions, context.second_car_transmissions = context.compare_page.get_car_parameters()

@then("Cars parameters should be verified")
def step(context):
    context.compare_page.compare_car_parameters(
            context.cars[0],
            context.cars[1],
            context.first_car_engines,
            context.second_car_engines,
            context.first_car_transmissions,
            context.second_car_transmissions)
