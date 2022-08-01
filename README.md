# glasses
A PaintBrush-like desktop application for building objects in
2D using Tkinter API.

## What's to install?

Although Tkinter is Python's standard GUI lib,
it has to be installed apart from the language.
To obtain Tkinter, you must use

`sudo apt-get install python3-tk`

After the installation, you may execute the code
from the `main` module.

## How to use it?

![App in execution](images/app.png)

There are 3 major components in 'glasses', acessible by the
`Operations` menu:
    
    * Prompt;
    * Created structures; and
    * Canvas.

For instance, every time a component is desired to be added,
the user must tell which are its coordinates inside
the application `Prompt`.
With a single coordinate, a point will be shown;
with 2, a line, and, with even more, a polygon.

In order to add a component, one must use

> `add (x1,y1) ... (xn,yn)`
> 
> e.g. `add (0,0)` or `add (200,200) (-999,90)`

As a disclaimer, it is worth mentioning that
there must be no blank spaces space between x and y.

With the coordinates written, just press the `Enter`
button the interface's text field and the given coordinates
will be properly painted over the `Canvas` and
listed at the `Created structures` menu.

## What else can the app do?

The application has 5 available operations.

    1. `add`;
    2. `rm` (remove);
    3. `tl` (translate):
    4. `sc` (scale); and
    5. `rt` (rotate).

Every operation follow the same template of
`<operation_name> (xi,yi) ... (xk,yk)`.
For the translation, scaling and rotation operations,
the last coordinate is interpreted as the desired
value to be used according to the operation,
e.g. `sc (100,100) (50,40) (30,30) (2,2)` will be interpreted as
`increase the object's size twofold`.

In order to use translation, scaling or rotation, the
desired object needs to be existent already.
For using it, one needs to write all of its
coordinates.

## .obj files

If wanted, one can add `.obj` files and
its coordinates to the canvas by using the upper
side menu `File` and clicking at `Open`. This projects
has a small collection of `.obj` files that can be
used, which are inside the `/resources` folder.