import pygame, sys, math

width, height = 360, 720
x = 0
y = 1


class Ball:
    def __init__(self):  # Initiation
        self.decel = 1
        self.pos = [width/2, height/2]
        self.velo = [0, 0]

    def get_decel_int(self):  # In case decel is needed
        return self.decel

    def get_velo(self):  # In case velo is needed
        return self.velo

    def set_velo(self, xdiff, ydiff, pwr):  # When space is pressed
        self.velo[x] = pwr * xdiff // 75
        self.velo[y] = pwr * ydiff // 75

    def set_pos(self, pos):
        self.pos = pos

    def __mod_velo(self):  # Called every frame
        if self.pos[x] > width:
            self.velo[x] = -self.velo[x]
            self.pos[x] = width
        if self.pos[x] < 0:
            self.velo[x] = -self.velo[x]
            self.pos[x] = 0
        if self.pos[y] > height:
            self.velo[y] = -self.velo[y]
            self.pos[y] = height
        if self.pos[y] < 0:
            self.velo[y] = -self.velo[y]
            self.pos[y] = 0

        if self.velo[x] > 1:
            self.velo[x] -= self.decel
        elif self.velo[x] < -1:
            self.velo[x] += self.decel
        if self.velo[y] > 1:
            self.velo[y] -= self.decel
        elif self.velo[y] < -1:
            self.velo[y] += self.decel

        if (self.velo[x] is 1 or self.velo[x] is -1) and (self.velo[y] is 1 or self.velo[y] is -1):
            self.velo[x] = 0
            self.velo[y] = 0


    def get_pos(self):
        self.__mod_velo()
        self.pos[x] += self.velo[x]
        self.pos[y] += self.velo[y]
        return self.pos