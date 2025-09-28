# Defining global variables
step = 1
state = 0
num_step = 1
turn_counter = 1


class Generate:

    # Taking the step size and x, y cordinates
    def __init__(self, step_size, x, y):
        self.step_size = step_size
        self.x = x
        self.y = y

    # Checking for prime
    def is_prime(num):

        if num <= 1:
            return False

        import math
        # Check divisibility from 2 to the square root of n
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                return False

        # If no divisors were found, n is prime
        return True

    #  Determining what will happen to the position
    def spiral(self):

        # 1=x++, 2=y--, 3=x--, 4=y++
        if step == 0:
            return (self.x, self.y)

        if state == 0:
            self.x += self.step_size
        elif state == 1:
            self.y -= self.step_size
        elif state == 2:
            self.x -= self.step_size
        elif state == 3:
            self.y += self.step_size

        return (self.x, self.y)

    # The bread and butter of the code!
    def change():
        global step,  state, turn_counter, num_step

        # So, we are saying if the remainder of step and number of steps is 0: Change the state.
        # Here, it's basically looking for if 1/1=0 then change state. 2/2=0 change state. 3/3=0 change state
        if step % num_step == 0:
            state = (state + 1) % 4

            # If the state changed, we took a turn. How many turns? We keep track
            turn_counter += 1

            # Increase the amount of steps every 2 turns
            if turn_counter % 2 == 0:
                num_step += 1

        # Increase steps
        step += 1

    # For drawing the numbers
    def draw_num(self, font, canvas, prev_x, prev_y):

        # Setting up globals
        global position, this_position

        line_color = (252, 209, 194)
        dot_color = (212, 89, 149)

        # Regular and Prime gets different colors
        normal = font.render(str(step), True, line_color)
        prime = font.render(str(step), True, dot_color)

        if step == 1:
            canvas.blit(normal, (prev_x, prev_y))

        elif Generate.is_prime(step):
            canvas.blit(prime, position)

        else:
            canvas.blit(normal, position)

        position = self.spiral()

    def draw_line(self, pos_x, pos_y, step, check, draw, canvas, func):
        global prev_x, prev_y, position, this_position

        line_color = (36, 18, 12)
        dot_color = (155, 57, 21)

        if step == 1:
            prev_x, prev_y = pos_x, pos_y

            draw.line(canvas, line_color, (prev_x, prev_y), (pos_x, pos_y), 2)

        elif check:
            draw.line(canvas, line_color, (prev_x, prev_y), position, 2)
            draw.circle(canvas, dot_color, (position), 4)

            prev_x, prev_y = position[0], position[1]
            this_position = position

        else:
            draw.line(canvas, line_color, (prev_x, prev_y), position, 2)
            draw.circle(canvas, dot_color, (this_position), 4)

            prev_x, prev_y = position[0], position[1]

        position = self.spiral()
