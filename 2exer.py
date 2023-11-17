import random
from dataclasses import dataclass, field, InitVar, make_dataclass
from typing import Any
from random import randint

# import pprint
# class Thing:
#     def __init__(self, name, weight, price, dims = []):
#         self.name = name
#         self.weight = weight
#         self.price = price
#         self.dims = dims
#
#     def __repr__(self):
#         return f'{self.__dict__}'
#
# @dataclass
# class ThingData:
#     name: str
#     weight: int
#     price: float
#     dims: list = field(default_factory=list)
#
#     def __eq__(self, other):
#         return self.price == other.price
#
#
# th = Thing('revref', 15, 1500)
# # print(th)
# td = ThingData('few', 12, 2.5)
# td.dims.append(10)
# print(td)
# td2 = ThingData('nam2', 12, 2.3)
# print(td2)

# class Vector3D:
#
#     def __init__(self, x, y, z, calc_len: bool = True):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.length = (x**2 + y**2 + z**2) ** 0.5 if calc_len else 0
#
# @dataclass(frozen=True)
# class VectorData:
#     x: int
#     y: int = field(compare=False)
#     z: int = field(default=0)
#     calc_len: InitVar[bool] = True
#     length: float = field(init=False, compare=False)
#     pi: float = field(init=False)
#
#     def __post_init__(self, calc_len):
#         if calc_len:
#             self.length = (self.x**2 + self.y**2 + self.z**2) ** 0.5
#         self.pi = 3.14
#
#
#
# v = Vector3D(1, 2, 3, False)
# print(v)
# vd = VectorData(1, 4, 3)
# vd2 = VectorData(1, 2, 3)
# print(vd == vd2)
# print(vd)
# print(vd2)

# @dataclass
# class Goods:
#     current_uid = 0
#
#     uid: int = field(init=False)
#     price: Any
#     weight: Any
#
#     def __post_init__(self):
#         print('Goods')
#         Goods.current_uid += 1
#         self.uid = Goods.current_uid
#
# class GoodMeasureFactory:
#
#     @staticmethod
#     def get_init_measure():
#         return [0, 0, 0]
#
#
# @dataclass
# class Book(Goods):
#     title: str
#     author: str
#     price: int
#     weight: float
#     measure: list = field(default_factory=list)
#
#     def __post_init__(self):
#         super().__post_init__()
#         print('book')
#
#
# g = Goods(1200, 2.5)
# print(g)
# g1 = Goods(1200, 2.5)
# print(g1)
# b = Book(123, 423, 'tyjty', 'iuygb')
# for i in range(len(b.measure)):
#     b.measure[i] = randint(10, 20)
# print(b)

# class Car:
#
#     def __init__(self, model, max_speed, price):
#         self.model = model
#         self.max_speed = max_speed
#         self.price = price
#
#     def get_max_speed(self):
#         return self.max_speed
#
#     def get_price(self):
#         return self.price
#
#
# CarData = make_dataclass('CarData', [('model', str), 'max_speed', ('price', int, field(default=0))],
#                          namespace={'get_max_speed': lambda self: self.max_speed,
#                                     'get_price': lambda self: self.price})
#
# cd = CarData('Lada Granta', 120, 600000)
# print(cd.get_max_speed())
# print(cd.get_price())

# @dataclass
# class AirCastle:
#     heigh: int
#     blocks: int
#     color: str
#
#     def change_height(self, value):
#         self.heigh = value if  value >- 1 else 0
#
#     def __add__(self, other):
#         if not isinstance(other, int):
#             raise TypeError ('woiuehfowieh')
#         self.blocks = self.blocks + other
#         self.heigh=self.heigh + other // 5
#
#         return AirCastle(self.heigh, self.blocks, self.color)
#
#     def visible(self, visibli):
#         return f'видимость замка: {self.heigh//visibli*self.blocks}'
#
#     def __str__(self):
#         return f'The AirCastle at an altitude of {self.heigh} meters is {self.color} with {self.blocks} clouds'
#
#
#
# v = AirCastle(552, 522, 'Red')
# v1 = AirCastle(55, 22, 'Black')
# print(v)
# v=v+10
# print(v)
# print(v1)
# print(v1 > v)
# print(v1 < v)
# print(v1 <= v)
# print(v1 >= v)
# print(v1 == v)
# print(v1 != v)
























