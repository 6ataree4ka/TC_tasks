import unittest
from base_test_case import BaseTestCase
from pages.main_page import MainPage
from pages.review_page import ReviewPage
from pages.car_page import CarPage
from pages.overview_page import OverviewPage
from pages.compare_page import ComparePage
from car import Car


class CarsTest(BaseTestCase):

    def test_cars_site_comparing_cars(self):
        cars = []

        while len(cars) < 2:
            main_page = MainPage()
            main_page.open_menu()
            main_page.select_menu_item()

            review_page = ReviewPage()
            brand, model, year = review_page.select_random_car()
            review_page.view_car()

            car_page = CarPage(car_brand=brand, car_model=model, car_year=year)
            car_page.switch_to_tab()

            overview_page = OverviewPage(
                car_brand=brand, car_model=model, car_year=year)
            engines, transmissions = overview_page.get_engines_and_transmissions()

            car = Car(brand, model, year, engines, transmissions)

            if overview_page.is_compare_possible() == True and overview_page.are_characteristics_present() == True:
                cars.append(car)

            if len(cars) == 2:
                overview_page.compare()

        compare_page = ComparePage()
        compare_page.select_necessary_car(
            cars[0].brand, cars[0].model, cars[0].year)
        first_car_engines, second_car_engines, first_car_transmissions, second_car_transmissions = compare_page.get_car_parameters()
        compare_page.compare_car_parameters(
            cars[0],
            cars[1],
            first_car_engines,
            second_car_engines,
            first_car_transmissions,
            second_car_transmissions)

if __name__ == "__main__":
    unittest.main()
