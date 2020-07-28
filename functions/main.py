## Name: Joshua Santillan
## Date: 3/1/20
## Email: santillanj125821@student.vvc.edu
## Class: cis83 spr-2020
## Description: Defining functions and calling them with paramaters

import math

def sphere_volume(r):
    sphere_volume = (4 / 3) * math.pi * pow(r,3)
    print("Sphere volume: ",sphere_volume)

def sphere_surface(r):
    sphere_surface = 4 * math.pi * pow(r,2)
    print("Sphere surface area: ",sphere_surface)

def cylinder_volume(r,h):
    cylinder_volume = math.pi * pow(r,2) * h
    print("Cylinder Volume: ",cylinder_volume)

def cylinder_surface(r,h):
    cylinder_surface = 2 * math.pi * r * (r + h) 
    print("Cylinder surface area: ",cylinder_surface)

def cone_volume(r,h):
    cone_volume = math.pi * pow(r,2) * (h/3) 
    print("Cone volume: ",cone_volume)

def cone_surface(r,h):
    cone_surface = math.pi * r * (r + math.sqrt( pow(h,2) + pow(r,2) ))
    print("Cone surface: ",cone_surface)

radius = int(input('Enter a radius to find the volume of a sphere: '))
sphere_volume(radius)

radius = int(input('Enter a radius to find the surface area of a sphere: '))
sphere_surface(radius)

radius = int(input('Enter a radius to find the volume and surface area of a sphere: '))
height = int(input('Enter a height to find the volume and surface area of a sphere: '))
cylinder_volume(radius,height)
cylinder_surface(radius,height)

radius = int(input('Enter a radius to find the volume and surface area of a cone: '))
height = int(input('Enter a height to find the volume and surface area of a sphere: '))
cone_volume(radius,height)
cone_surface(radius,height)