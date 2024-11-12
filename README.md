# 🐢 flowers

## Table of Contents 
- [Features](#features)
- [Installation](#installation)
- [How It Works](#how-it-works)

## Features✨
- draws colorful flowers at random coordinates

## Installation💻
- to run this project, you need Python installed on your machine

## How it works🔍
- the `choose_color()` function is a generator that iterates through a list of colors, yielding each one to provide a new color each time it's called
- the `draw_petal()` function uses the lengths and angles lists to create one petal
- the `draw_flower()` function uses `choose_color()` to pick a new color for each petal, creating a 12-petal flower in a circular shape
- the `draw_flowers()` function creates five flowers by moving the turtle to random spots

