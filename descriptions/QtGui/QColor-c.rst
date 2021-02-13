.. sip:class-description::
    :status: todo
    :brief: Colors based on RGB, HSV or CMYK values
    :digest: c5562db29086118f598f77890c93fd93

The :sip:ref:`~PyQt6.QtGui.QColor` class provides colors based on RGB, HSV or CMYK values.

A color is normally specified in terms of RGB (red, green, and blue) components, but it is also possible to specify it in terms of HSV (hue, saturation, and value) and CMYK (cyan, magenta, yellow and black) components. In addition a color can be specified using a color name. The color name can be any of the SVG 1.0 color names.

+------------------------+------------------------+-------------------------+
| RGB                    | HSV                    | CMYK                    |
+========================+========================+=========================+
| |image-qcolor-rgb-png| | |image-qcolor-hsv-png| | |image-qcolor-cmyk-png| |
+------------------------+------------------------+-------------------------+

The :sip:ref:`~PyQt6.QtGui.QColor` constructor creates the color based on RGB values. To create a :sip:ref:`~PyQt6.QtGui.QColor` based on either HSV or CMYK values, use the :sip:ref:`~PyQt6.QtGui.QColor.toHsv` and :sip:ref:`~PyQt6.QtGui.QColor.toCmyk` functions respectively. These functions return a copy of the color using the desired format. In addition the static :sip:ref:`~PyQt6.QtGui.QColor.fromRgb`, :sip:ref:`~PyQt6.QtGui.QColor.fromHsv` and :sip:ref:`~PyQt6.QtGui.QColor.fromCmyk` functions create colors from the specified values. Alternatively, a color can be converted to any of the three formats using the :sip:ref:`~PyQt6.QtGui.QColor.convertTo` function (returning a copy of the color in the desired format), or any of the :sip:ref:`~PyQt6.QtGui.QColor.setRgb`, :sip:ref:`~PyQt6.QtGui.QColor.setHsv` and :sip:ref:`~PyQt6.QtGui.QColor.setCmyk` functions altering *this* color's format. The :sip:ref:`~PyQt6.QtGui.QColor.spec` function tells how the color was specified.

A color can be set by passing an RGB string (such as "#112233"), or an ARGB string (such as "#ff112233") or a color name (such as "blue"), to the :sip:ref:`~PyQt6.QtGui.QColor.setNamedColor` function. The color names are taken from the SVG 1.0 color names. The :sip:ref:`~PyQt6.QtGui.QColor.name` function returns the name of the color in the format "#RRGGBB". Colors can also be set using :sip:ref:`~PyQt6.QtGui.QColor.setRgb`, :sip:ref:`~PyQt6.QtGui.QColor.setHsv` and :sip:ref:`~PyQt6.QtGui.QColor.setCmyk`. To get a lighter or darker color use the :sip:ref:`~PyQt6.QtGui.QColor.lighter` and :sip:ref:`~PyQt6.QtGui.QColor.darker` functions respectively.

The :sip:ref:`~PyQt6.QtGui.QColor.isValid` function indicates whether a :sip:ref:`~PyQt6.QtGui.QColor` is legal at all. For example, a RGB color with RGB values out of range is illegal. For performance reasons, :sip:ref:`~PyQt6.QtGui.QColor` mostly disregards illegal colors, and for that reason, the result of using an invalid color is undefined.

The color components can be retrieved individually, e.g with :sip:ref:`~PyQt6.QtGui.QColor.red`, :sip:ref:`~PyQt6.QtGui.QColor.hue` and :sip:ref:`~PyQt6.QtGui.QColor.cyan`. The values of the color components can also be retrieved in one go using the :sip:ref:`~PyQt6.QtGui.QColor.getRgb`, :sip:ref:`~PyQt6.QtGui.QColor.getHsv` and :sip:ref:`~PyQt6.QtGui.QColor.getCmyk` functions. Using the RGB color model, the color components can in addition be accessed with :sip:ref:`~PyQt6.QtGui.QColor.rgb`.

There are several related non-members: QRgb is a typdef for an unsigned int representing the RGB value triplet (r, g, b). Note that it also can hold a value for the alpha-channel (for more information, see the Alpha-Blended Drawing section). The :sip:ref:`~PyQt6.QtGui.qRed`, :sip:ref:`~PyQt6.QtGui.qBlue` and :sip:ref:`~PyQt6.QtGui.qGreen` functions return the respective component of the given QRgb value, while the :sip:ref:`~PyQt6.QtGui.qRgb` and :sip:ref:`~PyQt6.QtGui.qRgba` functions create and return the QRgb triplet based on the given component values. Finally, the :sip:ref:`~PyQt6.QtGui.qAlpha` function returns the alpha component of the provided QRgb, and the :sip:ref:`~PyQt6.QtGui.qGray` function calculates and return a gray value based on the given value.

:sip:ref:`~PyQt6.QtGui.QColor` is platform and device independent. The QColormap class maps the color to the hardware.

For more information about painting in general, see the `Paint System <https://doc.qt.io/qt-6/paintsystem.html>`_ documentation.

.. _qcolor-integer-vs-floating-point-precision:

Integer vs. Floating Point Precision
------------------------------------

:sip:ref:`~PyQt6.QtGui.QColor` supports floating point precision and provides floating point versions of all the color components functions, e.g. :sip:ref:`~PyQt6.QtGui.QColor.getRgbF`, :sip:ref:`~PyQt6.QtGui.QColor.hueF` and :sip:ref:`~PyQt6.QtGui.QColor.fromCmykF`. Note that since the components are stored using 16-bit integers, there might be minor deviations between the values set using, for example, :sip:ref:`~PyQt6.QtGui.QColor.setRgbF` and the values returned by the :sip:ref:`~PyQt6.QtGui.QColor.getRgbF` function due to rounding.

While the integer based functions take values in the range 0-255 (except :sip:ref:`~PyQt6.QtGui.QColor.hue` which must have values within the range 0-359), the floating point functions accept values in the range 0.0 - 1.0.

.. _qcolor-alpha-blended-drawing:

Alpha-Blended Drawing
---------------------

:sip:ref:`~PyQt6.QtGui.QColor` also support alpha-blended outlining and filling. The alpha channel of a color specifies the transparency effect, 0 represents a fully transparent color, while 255 represents a fully opaque color. For example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qcolor.py
    :lines: 62-68

The code above produces the following output:

.. image:: ../../../images/alphafill.png

The alpha channel of a color can be retrieved and set using the :sip:ref:`~PyQt6.QtGui.QColor.alpha` and :sip:ref:`~PyQt6.QtGui.QColor.setAlpha` functions if its value is an integer, and :sip:ref:`~PyQt6.QtGui.QColor.alphaF` and :sip:ref:`~PyQt6.QtGui.QColor.setAlphaF` if its value is float. By default, the alpha-channel is set to 255 (opaque). To retrieve and set *all* the RGB color components (including the alpha-channel) in one go, use the :sip:ref:`~PyQt6.QtGui.QColor.rgba` and :sip:ref:`~PyQt6.QtGui.QColor.setRgba` functions.

.. _qcolor-predefined-colors:

Predefined Colors
-----------------

There are 20 predefined :sip:ref:`~PyQt6.QtGui.QColor` objects in the ``QColorConstants`` namespace, including black, white, primary and secondary colors, darker versions of these colors, and three shades of gray. Furthermore, the ``QColorConstants::Svg`` namespace defines :sip:ref:`~PyQt6.QtGui.QColor` objects for the standard `SVG color keyword names <https://www.w3.org/TR/SVG11/types.html#ColorKeywords>`_.

.. image:: ../../../images/qt-colors.png

The ``QColorConstants::Color0``, ``QColorConstants::Color1`` and ``QColorConstants::Transparent`` colors are used for special purposes.

``QColorConstants::Color0`` (zero pixel value) and ``QColorConstants::Color1`` (non-zero pixel value) are special colors for drawing in QBitmaps. Painting with ``QColorConstants::Color0`` sets the bitmap bits to 0 (transparent; i.e., background), and painting with c{QColorConstants::Color1} sets the bits to 1 (opaque; i.e., foreground).

``QColorConstants::Transparent`` is used to indicate a transparent pixel. When painting with this value, a pixel value will be used that is appropriate for the underlying pixel format in use.

For historical reasons, the 20 predefined colors are also available in the :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor` enumeration.

Finally, :sip:ref:`~PyQt6.QtGui.QColor` recognizes a variety of color names (as strings); the static :sip:ref:`~PyQt6.QtGui.QColor.colorNames` function returns a QStringList color names that :sip:ref:`~PyQt6.QtGui.QColor` knows about.

.. _qcolor-the-extended-rgb-color-model:

The Extended RGB Color Model
----------------------------

The extended RGB color model, also known as the scRGB color space, is the same the RGB color model except it allows values under 0.0, and over 1.0. This makes it possible to represent colors that would otherwise be outside the range of the RGB colorspace but still use the same values for colors inside the RGB colorspace.

.. _qcolor-the-hsv-color-model:

The HSV Color Model
-------------------

The RGB model is hardware-oriented. Its representation is close to what most monitors show. In contrast, HSV represents color in a way more suited to the human perception of color. For example, the relationships "stronger than", "darker than", and "the opposite of" are easily expressed in HSV but are much harder to express in RGB.

HSV, like RGB, has three components:

* H, for hue, is in the range 0 to 359 if the color is chromatic (not gray), or meaningless if it is gray. It represents degrees on the color wheel familiar to most people. Red is 0 (degrees), green is 120, and blue is 240.

  |image-qcolor-hue-png|

* S, for saturation, is in the range 0 to 255, and the bigger it is, the stronger the color is. Grayish colors have saturation near 0; very strong colors have saturation near 255.

  |image-qcolor-saturation-png|

* V, for value, is in the range 0 to 255 and represents lightness or brightness of the color. 0 is black; 255 is as far from black as possible.

  |image-qcolor-value-png|

Here are some examples: pure red is H=0, S=255, V=255; a dark red, moving slightly towards the magenta, could be H=350 (equivalent to -10), S=255, V=180; a grayish light red could have H about 0 (say 350-359 or 0-10), S about 50-100, and S=255.

Qt returns a hue value of -1 for achromatic colors. If you pass a hue value that is too large, Qt forces it into range. Hue 360 or 720 is treated as 0; hue 540 is treated as 180.

In addition to the standard HSV model, Qt provides an alpha-channel to feature alpha-blended drawing.

.. _qcolor-the-hsl-color-model:

The HSL Color Model
-------------------

HSL is similar to HSV, however instead of the Value parameter, HSL specifies a Lightness parameter which maps somewhat differently to the brightness of the color.

Similarly, the HSL saturation value is not in general the same as the HSV saturation value for the same color. :sip:ref:`~PyQt6.QtGui.QColor.hslSaturation` provides the color's HSL saturation value, while :sip:ref:`~PyQt6.QtGui.QColor.saturation` and :sip:ref:`~PyQt6.QtGui.QColor.hsvSaturation` provides the HSV saturation value.

The hue value is defined to be the same in HSL and HSV.

.. _qcolor-the-cmyk-color-model:

The CMYK Color Model
--------------------

While the RGB and HSV color models are used for display on computer monitors, the CMYK model is used in the four-color printing process of printing presses and some hard-copy devices.

CMYK has four components, all in the range 0-255: cyan (C), magenta (M), yellow (Y) and black (K). Cyan, magenta and yellow are called subtractive colors; the CMYK color model creates color by starting with a white surface and then subtracting color by applying the appropriate components. While combining cyan, magenta and yellow gives the color black, subtracting one or more will yield any other color. When combined in various percentages, these three colors can create the entire spectrum of colors.

Mixing 100 percent of cyan, magenta and yellow *does* produce black, but the result is unsatisfactory since it wastes ink, increases drying time, and gives a muddy colour when printing. For that reason, black is added in professional printing to provide a solid black tone; hence the term 'four color process'.

In addition to the standard CMYK model, Qt provides an alpha-channel to feature alpha-blended drawing.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPalette`, :sip:ref:`~PyQt6.QtGui.QBrush`, :sip:ref:`~PyQt6.QtGui.QColorConstants`.

.. |image-qcolor-rgb-png| image:: ../../../images/qcolor-rgb.png
.. |image-qcolor-hsv-png| image:: ../../../images/qcolor-hsv.png
.. |image-qcolor-cmyk-png| image:: ../../../images/qcolor-cmyk.png
.. |image-qcolor-hue-png| image:: ../../../images/qcolor-hue.png
.. |image-qcolor-saturation-png| image:: ../../../images/qcolor-saturation.png
.. |image-qcolor-value-png| image:: ../../../images/qcolor-value.png
