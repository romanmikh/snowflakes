import turtle
import random

# window parameters
WIN_SIZE    = 1200
PAD         = 30
FLAKE_SIZE  = WIN_SIZE // 6
NUM_FLAKES  = WIN_SIZE // FLAKE_SIZE
STEP        = FLAKE_SIZE + PAD

# snowflake parameters
ORDER       = 3
MIN_LEN     = 4
BRANCH_NUM  = (1, 3)        # how many side-branches per fork
ANGLE_RANGE = (25, 65)      # degrees either side of the trunk
SPLIT_RANGE = (0.15, .5)   # where along the trunk the first fork appears


# turtle setup
screen = turtle.Screen()
screen.setup(WIN_SIZE, WIN_SIZE)
pen = turtle.Turtle(visible=False)
pen.pensize(2)
screen.tracer(0, 0)  # turn off animation


def branch(length: float, depth: int, rng: random.Random) -> None:
    """Recursive, randomly-varying snow-branch."""
    if depth == 0 or length < MIN_LEN:
        pen.forward(length)
        pen.backward(length)
        return

    # first fork location
    first_seg = length * rng.uniform(*SPLIT_RANGE)
    rest      = length - first_seg
    pen.forward(first_seg)            # walk to the fork point

    if rng.random() < 0.5:            # trunk *terminates* into two arms
        angle = rng.uniform(*ANGLE_RANGE)
        for turn in (angle, -angle):  # left then right (symmetry)
            pen.left(turn)
            branch(rest, depth - 1, rng)
            pen.right(turn)
    else:                             # keep trunk & sprout side-branches
        n = rng.randint(*BRANCH_NUM)
        angle = rng.uniform(*ANGLE_RANGE)
        side_len = rest * 0.6         # side branches shorter

        for _ in range(n):
            pen.left(angle)
            branch(side_len * rng.uniform(0.5, 0.9), depth - 1, rng)
            pen.right(2 * angle)
            branch(side_len * rng.uniform(0.5, 0.9), depth - 1, rng)
            pen.left(angle)

        # continue main trunk after the side forks
        branch(rest, depth - 1, rng)

    pen.backward(first_seg)           # return to start of this segment


def snowflake(cx: float, cy: float, size: float, depth: int = ORDER) -> None:
    """
    Draws a 6-armed snowflake whose *arms stay identical*
    by re-using the same PRNG seed for every arm.
    """
    base_seed = random.getrandbits(32)

    for k in range(6):
        rng = random.Random(base_seed)        # identical pattern each arm
        pen.penup()
        pen.goto(cx, cy)
        pen.pendown()
        pen.setheading(k * 60)
        branch(size, depth, rng)


random.seed()
for x in range(-WIN_SIZE//2+STEP//2, WIN_SIZE//2, STEP):
    for y in range(-WIN_SIZE//2+STEP//2, WIN_SIZE//2, STEP):
        snowflake(x, y, FLAKE_SIZE//2)

screen.exitonclick()
