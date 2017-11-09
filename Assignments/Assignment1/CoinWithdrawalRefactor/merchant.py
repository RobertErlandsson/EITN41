import random as r
import math as m
import format_converter as fc
import numpy

from bank import Bank
from alice import Alice
import common

class Merchant:

    def __init__(self, n, e):
        self.n = n
        self.e = e

    def generate_z(self):
        self.z = [r.randint(0,1) for i in range(self.k)]


    def send_z_to_alice(self, alice):
        alice.receive_z(self.z)

    def receive_serial(self, s, k):
        self.serial = s
        self.k = k

    def receive_z_answer(self, z_answer):
        self.z_answer = z_answer

    def verify(self):
        xi = []
        yi = []
        for i in range(len(self.z)):
            if self.z[i] == 0:
                xi.append(self.z_answer[i][0])
                yi.append(common.h(self.z_answer[i][1], self.z_answer[i][2]))
            else:
                xi.append(common.h(self.z_answer[i][1], self.z_answer[i][2]))
                yi.append(self.z_answer[i][0])

        f_prod = numpy.prod(list(map(lambda v:common.f(v[0], v[1]), zip(xi, yi))))
        print("h(x) signed:\t{}".format((f_prod % self.n) % self.n))
        print("decrypt:\t{}".format( (self.serial ** self.e) % self.n))
        return (f_prod % self.n) % self.n == (self.serial ** self.e) % self.n
