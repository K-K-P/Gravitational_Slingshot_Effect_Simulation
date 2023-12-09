"""Class with all methods and attributes for simulating the spacecraft's or any other object's physics"""
import pygame
import math


class Spaceship:
    def __init__(self, x, y, vel_x, vel_y, mass, window, size, color, g_factor):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.mass = mass
        self.window = window
        self.size = size
        self.color = color
        self.g_factor = g_factor

    def draw(self):
        pygame.draw.circle(self.window, self.color, (int(self.x), int(self.y)), self.size)

    def move(self, planet):
        # calculating the gravity force:
        delta_x = planet.x - self.x
        delta_y = planet.y - self.y
        dist_between = math.sqrt(delta_x**2 + delta_y**2)
        force_g = self.g_factor * self.mass * planet.mass / dist_between ** 2
        alfa = math.atan2(delta_y, delta_x)
        accel = force_g / self.mass
        accel_x = math.cos(alfa) * accel
        accel_y = math.sin(alfa) * accel
        self.vel_x += accel_x
        self.vel_y += accel_y
        self.x += self.vel_x
        self.y += self.vel_y


class Planet:
    def __init__(self, x, y, mass, window, planet, planet_size):
        self.x = x
        self.y = y
        self.mass = mass
        self.window = window
        self.planet = planet
        self.planet_size = planet_size

    def draw(self):
        self.window.blit(self.planet, (self.x - self.planet_size, self.y - self.planet_size))

