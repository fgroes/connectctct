#! /usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier. All rights reserved.
# Distributed under the terms of the new BSD License.
# -----------------------------------------------------------------------------
from shaders import basic_vertex_code as vertex_code
from shaders import basic_fragment_code as fragment_code
from graphics import Graphics, Geometry, Rectangle


if __name__ == "__main__":
    cs = [
        [1, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 0, 1, 1]]
    vs = [
        [-1, -1, 0],
        [-1, 1, 0],
        [1, -1, 0]]
    triangle1 = Geometry(vs, cs)
    cs = [
        [0, 1, 0, 1],
        [1, 0, 0, 1],
        [0, 0, 1, 1]]
    vs = [
        [1, -1, 0],
        [-1, 1, 0],
        [1, 1, 0]]
    triangle2 = Geometry(vs, cs)
    cs = [
        [0, 1, 0, 1],
        [1, 0, 0, 1],
        [0, 0, 1, 1],
        [1, 1, 0, 1]]
    vs = [
        [-1, -1, 0],
        [1, -1, 0],
        [-1, 1, 0],
        [1, 1, 0]]
    rectangle = Rectangle(vs, cs)
    rectangle.translate([0.5, 0.5, 0.0])
    geos = [triangle1, triangle2, rectangle]
    g = Graphics(geos, vertex_code, fragment_code)
    g.start()