### Graph Calculator

A simple but useful design made with numpy, matplotlib, and [ttkbootstrap](https://github.com/ddaneil/turbo-spoon).  
Used to visualize 2 dimensional functions or 3 dimensional functions.

---

## Features

- 2D Function plotting, random colored lines with a maximum of *30* 2D functions.
- 3D Function plotting, which has 3 types:
  - Surface Plotting (*default*).
  - Wireframe Plotting.
  - Triangulation.
---

## How To Use
- 2D
  - **Show Graph** : Creates a figure, with functions listed.
  - **+ Button** : Adds another function slot.
  - **Range** : Specifies the range of which the x / y value spans.
  - **Toggle Legend** : Shows the legend, useful if working with more than 1 function.
  - **f(y)** : If the user wants to use a y-function instead of an x-function.
  - **Function Entry** : Functions are placed here, one slot can only fit one function, sets f(x) as the default function.
  - *Up to 30 Functions*

- 3D
  - **Show Graph** : Creates a figure, with a 3D representation of the function.
  - **Range** : Specifies the range of which the x *and* value spans.
  - **Triangulate** : Toggles the triangulated graph setting. Only one toggle may be toggled at once.
  - **Wireframe** : Toggles the wireframe graph setting, which disregards theme. E-Color must not be set to 'none', otherwise the graph will have nothing in it.
  - **Function Entry** : Functions are placed here, only one function can exist.
  - **Function Formats** : changes how the functions are structured.
  - **Theme** : Defines the colormap of the 3D surface. Select from a broad amount of colormaps made by matplotlib.
  - **E-Color** : Edge color, defines the color of the lines/edges of the 3D function. Type in colors only supported by matplotlib (ex. CSS colors).
  - **Opacity** : Defines transparency.
  - **Fineness** : Defines how many squares/triangles make up for the function's side.

# Screenshots

![Screenshot](./images/sineAndCosineWave.png)
![Screenshot](./images/triangulated3DFunction.png)
