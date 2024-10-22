# A sprite is a simple spider shaped thing with n legs coming out from a center point. The angle between each leg is 360 / n degrees.
# Write a program to draw a sprite where the number of legs is provided by the user.


import matplotlib
matplotlib.use('Agg')  # use the Agg backend for headless environments
import matplotlib.pyplot as plt
import numpy as np

# function to draw sprite w/ matplotlib
def draw_sprite(legs):
    angles = np.linspace(0, 2 * np.pi, legs, endpoint=False)  # angle spacing
    length = 1  # leg length

    # plot
    fig, ax = plt.subplots()
    ax.set_aspect('equal')  # aspect ratio

    # draw leg
    for angle in angles:
        x = [0, length * np.cos(angle)]
        y = [0, length * np.sin(angle)]
        ax.plot(x, y, 'k-', lw=2)  # 'k-' means a black line

    # set limits and hide axes
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.axis('off')

    # save the plot to a file instead of showing it
    plt.savefig("sprite.png")  # save as a PNG file
    plt.close()  # close plot

# number of legs from user
n = int(input("Enter the number of legs for the sprite: "))

# call function
draw_sprite(n)

print("Sprite saved as 'sprite.png'")

