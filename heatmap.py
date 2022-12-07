import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import os

# Function to generate a list of random coordinate points
# and store them in a file titled "coordinates.txt"
def generateCoordinatePointsFile(length, width, numPoints):
    # Define the dimensions of our field
    xMin = -length // 2
    xMax = length // 2
    yMin = -width // 2
    yMax = width // 2
    
    # Create a file titled coordinates.txt
    with open("./random/coordinates.txt", "w") as c:

        # Add corners of our field as coordinate points
        c.write("{x},{y}\n".format(x = str(xMin), y = str(yMin)))
        c.write("{x},{y}\n".format(x = str(xMin), y = str(yMax)))
        c.write("{x},{y}\n".format(x = str(xMax), y = str(yMin)))
        c.write("{x},{y}\n".format(x = str(xMax), y = str(yMax)))

        i = 0
        
        # Randomly generate numPoints coordinate points,
        # and add them to the "coordinates.txt" file
        while i < numPoints:
            x = random.randint(xMin, xMax) # x coordinate
            y = random.randint(yMin, yMax) # y coordinate

            if (x,y) in [(xMin, yMin), (xMin, yMax), (xMax, yMin), (xMax, yMax)]:
                continue
            else:
                c.write("{x},{y}\n".format(x = str(x), y = str(y)))
                i += 1


# Function to generate a heat map given
# a file with x,y coordinate points
def generateHeatMap(showPoints, showLines, colorScheme, length, width, resultFileName, file="./random/coordinates.txt"):
    # Load the coordinates file
    x, y = np.loadtxt(file, delimiter=',', unpack=True)

    # Draw the lines on the soccer field if the ShowLines parameter is true
    if showLines:
        # Draw the midfield circle
        figure, axes = plt.subplots()
        midCircle = plt.Circle((0, 0), 10, fill=False, color="black")
        axes.set_aspect(1)
        axes.add_artist(midCircle)

        # Draw the midfield line
        plt.vlines(0, -width // 2, width // 2, color = "black")

        # Draw the penalty areas on both sides
        plt.hlines(22, -length // 2, (-length// 2) + 18, color = "black")
        plt.hlines(22, (length // 2) - 18, length // 2, color = "black")
        plt.hlines(-22, -length // 2, (-length// 2) + 18, color = "black")
        plt.hlines(-22, (length // 2) - 18, length // 2, color = "black")
        plt.vlines((-length// 2) + 18, 22, -22, color = "black")
        plt.vlines((length// 2) - 18, 22, -22, color = "black")

        # Draw the goal areas on both sides
        plt.hlines(6, -length // 2, (-length// 2) + 6, color = "black")
        plt.hlines(6, (length // 2) - 6, length // 2, color = "black")
        plt.hlines(-6, -length // 2, (-length// 2) + 6, color = "black")
        plt.hlines(-6, (length // 2) - 6, length // 2, color = "black")
        plt.vlines((-length// 2) + 6, 6, -6, color = "black")
        plt.vlines((length// 2) - 6, 6, -6, color = "black")

        # Draw the penalty spots
        plt.plot((-length // 2) + 12, 0, "ko")
        plt.plot((length // 2) - 12, 0, "ko")
    
    # Plot all the coordinate points if the showPoints parameter is true
    if showPoints:
        plt.plot(x, y, 'o', markersize=1, markeredgecolor="black")

    # Generate our kernel density estimation
    kde = sns.kdeplot(
        x=x, # The x coordinates from our position data
        y=y, # The y coordinates from our position data
        fill=True,
        thresh=0,
        alpha=.8, # The brightness of the heatmap
        levels = 100, # The number of contour levels
        cmap=colorScheme # The color scheme to use
    )

    # Show the heatmap to the user
    plt.xlim(-length // 2, length // 2)
    plt.ylim(-width // 2, width // 2)
    plt.show()

    # Save the heatmap in the heatmaps folder
    img = kde.get_figure()
    curDir = os.getcwd()
    newDir = curDir + "/heatmaps/" + resultFileName + ".png"
    img.savefig(newDir, transparent=True, bbox_inches='tight', pad_inches=0)

# Call the two functions above to generate our heatmap
def generate(randomPoints):
    now = datetime.now()
    time = now.strftime("%m-%d-%Y_%H:%M:%S")
    
    if randomPoints:
        generateCoordinatePointsFile(length = 116, width = 74, numPoints = 200)
        # EDIT THESE PARAMETERS IF YOU WANT TO RANDOMLY GENERATE
        # COORDINATE POINTS AND THEN A HEATMAP USING THOSE POINTS
        generateHeatMap(
            showPoints = False,
            showLines = True,
            colorScheme = "viridis",
            length = 116,
            width = 74,
            resultFileName = "random_{t}".format(t = time)
        )

        return
    
    # EDIT THESE PARAMETERS IF YOU ALREADY HAVE COORDINATE POINTS IN
    # A .txt FILE AND WANT TO GENERATE A HEATMAP USING THOSE POINTS
    generateHeatMap(
        showPoints = False,
        showLines = True,
        colorScheme = "viridis",
        length = 116,
        width = 74,
        resultFileName = "real_{t}".format(t = time),
        file = "./pregenerated/demo.txt"
    )
    
generate(randomPoints = True)

# SOURCES
# https://zbigatron.com/generating-heatmaps-from-coordinates/
# https://stackoverflow.com/questions/64055621/write-coordinates-to-txt-file-to-future-use-it-in-program
# https://cmdlinetips.com/2012/09/three-ways-to-write-text-to-a-file-in-python/#:~:text=To%20create%20and%20write%20to,a%20new%20file%20to%20write.&text=If%20you%20want%20to%20append,if%20it%20does%20not%20exist.
# https://seaborn.pydata.org/tutorial/color_palettes.html
# https://matplotlib.org/stable/tutorials/colors/colormaps.html
# Official documentations for all imported libraries and packages
