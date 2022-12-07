Computer Graphics
=================

Graphics Concepts
-----------------

Modern computer displays, otherwise known as monitors, are raster based which means
that discrete pixels in a rectangular grid are used to display colors that together
form the image which is displayed.

Each of this pixels (think picture elements) has a color value assigned to it.
Each color value is made up of three color components, each with separate values, one
each for red, green, and blue.  If the red, green, and blue components all have the
highest value, the pixel will be the brightest white. If they all have the lowest
(zero) value then the pixel will be black. If the components have different values,
then other colors can be created, such as high values for red and blue with a zero
green value to make a purple color.

There are other ways to represent colors with numeric values, but RGB values with
8 bits of data for each are the most common. This is also known as 24-bit RGB.
Because two raised to the exponent of eight is 256, that is how many possible values
you can have for an 8-bit value, also known as a byte. These values range from
0 to 255.

If we have red=0, green=255, blue=128 we would have a blueish green color for example.

When images are stored in files or in offscreen memory, their data is also usually
represented as RGB. Sometimes there is also an alpha transparency component. Alpha means a component
value besides the color for reach pixel which is used to indicate how transparent or opaque
a pixel is so that when two images are composited together it can be done smoothly and
accurately.  For example if you wanted to draw an image of an object on a background,
if they object's edges had an alpha transparency stored then it could have the edges smoothly
blended when drawn on top of the background.

When image data is copied from one memory buffer to another this is called "blitting".
This often means copying an image onto the display's memory.

