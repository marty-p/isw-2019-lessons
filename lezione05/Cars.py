# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 09:36:09 2019

@author: Studente
"""

class Cars(object):
    def __init__(self, car, offer):
        self.car = car
        self.offer = offer
        self.__min_price = 12500
        self.__available_cars = ['fiat500', 'audia3', 'ferrarif8']
    def __sold(self):
        print('the {} car has been sold.'.format(self.car))
    def __not_sold(self):
        print('the selected car {} has not been sold, the offer is too low'.format(self.offer))
    def _set_min_price(self, new_price):
        self.__min_price = new_price
    def _set_available_cars(self, new_cars):
        self.__available_cars = new_cars
    def car_dealership(self):
        if self.car in self.__available_cars:
            if self.car == 'fiat500':
                if self.offer == self.__min_price:
                    self.__sold()
                else:
                    self.__not_sold()
            elif self.car == 'audia3':
                if self.offer == 3*self.__min_price:
                    self.__sold()
                else:
                    self.__not_sold()
            else:
                if self.offer == 21*self.__min_price:
                    self.__sold()
                else:
                    self.__not_sold()
                    
if __name__ == '__main__':
    cars_instance = Cars('ferrarif8', 300000)
    print(cars_instance.offer)
    print(cars_instance.car_dealership())
    cars_instance._set_available_cars(['fiat500','audia3'])
    print(cars_instance.__dict__)
