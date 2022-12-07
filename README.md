## Instructions for Users

## Team Members

Vedant Apte, Natalie Mogul, Annika Holliday

## Downloading Python

If you do not have Python downloaded on your computer, you will need to do that first.

1. Go to this link [https://www.python.org/downloads/]
2. Hover over the downloads tab and click on your operating system: macOS for MacBooks, Windows for others.
3. Click on the option beginning with "Latest Release for..." and follow the instructions.
4. Download the appropriate version for your device.
5. Follow the on screen instructions to complete the installation.

## Downloading Visual Studio Code

If you do not have Visual Studio Code on your computer, you will need to download that as well. To do so,

1. Go to this link [https://code.visualstudio.com/download] and download the appropriate version.
2. Follow the on screen instructions to complete the installation.

## Downloading Anaconda

If you do not have Anaconda downloaded on your computer, you will need to download that as well. To do so,

1. Go to this link [https://www.anaconda.com/products/distribution] and download the appropriate version.
2. Follow the on screen instructions to complete the installation.

## Instructions for Learners

1. Navigate to the Code tab in the top left of this Github repository.
2. Click on the green button labeled <> Code.
3. Click Download ZIP.
4. Go to your Downloads folder and open up the zip file. You should see another folder titled "stlHeatmap-main" get created. Within this stlHeatmap folder, create two new folders called "random" and "heatmaps".
5. Now, open up Visual Studio Code.
6. Click "File" in the top left corner, then click "Open Folder", and open up the stlHeatmap-main folder that you just downloaded.
7. Open the file titled "heatmap.py".
8. Take a look at lines 110-120. In line 110, the default parameters should be length = 116, width = 74, numPoints = 200. Feel free to change the numPoints parameter to a number that you desire. This is the number of random points our code will generate in order to create a heatmap. Do not change the length and width parameters.
9. In lines 114-116, modify the parameters you wish to modify. Do not modify the length, width, or resultFileName parameters. The showPoints parameter should be set to "True" if you want to see all the coordinate points plotted on your heatmap, and "False" otherwise. The showLines parameter should be set to "True" if you want to see all the lines from the field plotted on your heatmap, and "False" otherwise. The colorScheme parameter should be set to the color scheme that you want to use. The options include "viridis", "magma", "plasma", "inferno", and "cividis".
10. In the top navigation bar, click on "View". In the dropdown menu that appears, click "Terminal" (the option under Debug Console). This should open up a terminal window at the bottom of VS Code.
11. Type the following commands in order, ONE AT A TIME (hit enter after typing each one), in the Terminal window. "conda install numpy", "conda install matplotlib", "conda install seaborn". These three commands will import the necessary packages, numpy, matplotlib, and seaborn, to make the heatmap generation code functional. If the commands do not work, you can Google "how to install package name> (replace package name with the name of the package you are having trouble installing). You should only have to do this step the first time you are running the program.
12. In the same terminal window, type in the command "python3 heatmap.py". After a couple of seconds, you should see the heatmap open up on your computer. It will also be saved inside the "heatmaps" folder with the title "random_date_time" for future access.

## Instructions for Athletes

We are assuming you already have a .txt file with position data.

** For the purposes of this project, we have some pregenerated files already placed in the pregenerated folder. If you are a member of the teaching team who is grading this project, please use any of the pregenerated files in the pregenerated folder. **

1. Navigate to the Code tab in the top left of this Github repository.
2. Click on the green button labeled <> Code.
3. Click Download ZIP.
4. Go to your Downloads folder and open up the zip file. You should see another folder titled "stlHeatmap-main" get created. Within this stlHeatmap folder, create two new folders called "random" and "heatmaps".
5. Now, open up Visual Studio Code.
6. Click "File" in the top left corner, then click "Open Folder", and open up the stlHeatmap-main folder that you just downloaded.
7. Add your .txt file with coordinates in x,y format already to the pregenerated folder. For the teaching team, once again, this has already been done for you; use the pregenerated files already in the pregenerated folder.
8. Open the file titled "heatmap.py".
9. Take a look at the code, and then set the randomPoints variable to "False" in line 136.
10. In lines 126-134, modify the parameters you wish to modify. The showPoints parameter should be set to "True" if you want to see all the coordinate points plotted on your heatmap, and "False" otherwise. The showLines parameter should be set to "True" if you want to see all the lines from the field plotted on your heatmap, and "False" otherwise. The colorScheme parameter should be set to the color scheme that you want to use. The options include "viridis", "magma", "plasma", "inferno", and "cividis". The length should be the length of the field in yards (set this to 116 if you are on the teaching team). The width should be the width of the field in yards (set this to 74 if you are on the teaching team). Do not change the resultFileName. In the file parameter, replace "demo.txt" with the name of the file that contains your position data (teaching team can use any file from the pregenerated folder).
11. In the top navigation bar, click on "View". In the dropdown menu that appears, click "Terminal" (the option under Debug Console). This should open up a terminal window at the bottom of VS Code.
12. Type the following commands in order, ONE AT A TIME (hit enter after typing each one), in the Terminal window. "conda install numpy", "conda install matplotlib", "conda install seaborn". These three commands will import the necessary packages, numpy, matplotlib, and seaborn, to make the heatmap generation code functional. If the commands do not work, you can Google "how to install package name> (replace package name with the name of the package you are having trouble installing). You should only have to do this step the first time you are running the program.
13. In the same terminal window, type in the command "python3 heatmap.py". After a couple of seconds, you should see the heatmap open up on your computer. It will also be saved inside the "heatmaps" folder with the title "random_date_time" for future access.
