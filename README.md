# Ulam-Spiral
A simple Python program that generates an **Ulam Spiral**!

The program is quite simple and easy to understand. I have tried my best to add comments and important notes everywhere!

## How it works?
The Ulam Spiral was put together by mathematician Stanslaw Ulam. It is a square spiral depicting set of prime numbers. In the spiral, we can notice sets of primes making horizontal, diagonal and vertical lines.

## The Code
The spiral is generated using an algorathim (function `change()` in `generate.py`). Refer to the function. We take a few global values. THen we run some if conditions on them. Firstly, we ask whether the number on the screen is divisible by the amount of steps. If the modulo returns 0, we change the state of the spiral or *turn the spiral*. We increment the variable `turn_counter` by 1 every time there is a turn made. Then, we check the divisibility of `turn_counter` by 2. Since it's a square matrix, every time the spiral makes two turns, we increase the number of steps it must take to make another turn.

## Line Spiral
<div align="left">
  <img src=https://github.com/haseebwt/Ulam-Spiral/blob/main/line_spiral.png>
</div>

## Number Spiral

<div align="left">
  <img src=https://github.com/haseebwt/Ulam-Spiral/blob/main/number_spiral.png>
</div>
