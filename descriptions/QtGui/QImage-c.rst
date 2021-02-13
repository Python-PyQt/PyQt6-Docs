.. sip:class-description::
    :status: todo
    :brief: Hardware-independent image representation that allows direct access to the pixel data, and can be used as a paint device
    :digest: 2f9f59988937a902b3eec131a2950541

The :sip:ref:`~PyQt6.QtGui.QImage` class provides a hardware-independent image representation that allows direct access to the pixel data, and can be used as a paint device.

Qt provides four classes for handling image data: :sip:ref:`~PyQt6.QtGui.QImage`, :sip:ref:`~PyQt6.QtGui.QPixmap`, `QBitmap <https://doc.qt.io/qt-6/gui-changes-qt6.html#qbitmap>`_ and :sip:ref:`~PyQt6.QtGui.QPicture`. :sip:ref:`~PyQt6.QtGui.QImage` is designed and optimized for I/O, and for direct pixel access and manipulation, while :sip:ref:`~PyQt6.QtGui.QPixmap` is designed and optimized for showing images on screen. `QBitmap <https://doc.qt.io/qt-6/gui-changes-qt6.html#qbitmap>`_ is only a convenience class that inherits :sip:ref:`~PyQt6.QtGui.QPixmap`, ensuring a depth of 1. Finally, the :sip:ref:`~PyQt6.QtGui.QPicture` class is a paint device that records and replays :sip:ref:`~PyQt6.QtGui.QPainter` commands.

Because :sip:ref:`~PyQt6.QtGui.QImage` is a :sip:ref:`~PyQt6.QtGui.QPaintDevice` subclass, :sip:ref:`~PyQt6.QtGui.QPainter` can be used to draw directly onto images. When using :sip:ref:`~PyQt6.QtGui.QPainter` on a :sip:ref:`~PyQt6.QtGui.QImage`, the painting can be performed in another thread than the current GUI thread.

The :sip:ref:`~PyQt6.QtGui.QImage` class supports several image formats described by the :sip:ref:`~PyQt6.QtGui.QImage.Format.Format` enum. These include monochrome, 8-bit, 32-bit and alpha-blended images which are available in all versions of Qt 4.x.

:sip:ref:`~PyQt6.QtGui.QImage` provides a collection of functions that can be used to obtain a variety of information about the image. There are also several functions that enables transformation of the image.

:sip:ref:`~PyQt6.QtGui.QImage` objects can be passed around by value since the :sip:ref:`~PyQt6.QtGui.QImage` class uses `implicit data sharing <https://doc.qt.io/qt-6/implicit-sharing.html>`_. :sip:ref:`~PyQt6.QtGui.QImage` objects can also be streamed and compared.

**Note:** If you would like to load :sip:ref:`~PyQt6.QtGui.QImage` objects in a static build of Qt, refer to the Plugin HowTo.

**Warning:** Painting on a :sip:ref:`~PyQt6.QtGui.QImage` with the format :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_Indexed8` is not supported.

.. _qimage-reading-and-writing-image-files:

Reading and Writing Image Files
-------------------------------

:sip:ref:`~PyQt6.QtGui.QImage` provides several ways of loading an image file: The file can be loaded when constructing the :sip:ref:`~PyQt6.QtGui.QImage` object, or by using the :sip:ref:`~PyQt6.QtGui.QImage.load` or :sip:ref:`~PyQt6.QtGui.QImage.loadFromData` functions later on. :sip:ref:`~PyQt6.QtGui.QImage` also provides the static :sip:ref:`~PyQt6.QtGui.QImage.fromData` function, constructing a :sip:ref:`~PyQt6.QtGui.QImage` from the given data. When loading an image, the file name can either refer to an actual file on disk or to one of the application's embedded resources. See `The Qt Resource System <https://doc.qt.io/qt-6/resources.html>`_ overview for details on how to embed images and other resource files in the application's executable.

Simply call the :sip:ref:`~PyQt6.QtGui.QImage.save` function to save a :sip:ref:`~PyQt6.QtGui.QImage` object.

The complete list of supported file formats are available through the :sip:ref:`~PyQt6.QtGui.QImageReader.supportedImageFormats` and :sip:ref:`~PyQt6.QtGui.QImageWriter.supportedImageFormats` functions. New file formats can be added as plugins. By default, Qt supports the following formats:

+--------+---------------------------------------+--------------+
| Format | Description                           | Qt's support |
+========+=======================================+==============+
| BMP    | Windows Bitmap                        | Read/write   |
+--------+---------------------------------------+--------------+
| GIF    | Graphic Interchange Format (optional) | Read         |
+--------+---------------------------------------+--------------+
| JPG    | Joint Photographic Experts Group      | Read/write   |
+--------+---------------------------------------+--------------+
| JPEG   | Joint Photographic Experts Group      | Read/write   |
+--------+---------------------------------------+--------------+
| PNG    | Portable Network Graphics             | Read/write   |
+--------+---------------------------------------+--------------+
| PBM    | Portable Bitmap                       | Read         |
+--------+---------------------------------------+--------------+
| PGM    | Portable Graymap                      | Read         |
+--------+---------------------------------------+--------------+
| PPM    | Portable Pixmap                       | Read/write   |
+--------+---------------------------------------+--------------+
| XBM    | X11 Bitmap                            | Read/write   |
+--------+---------------------------------------+--------------+
| XPM    | X11 Pixmap                            | Read/write   |
+--------+---------------------------------------+--------------+

.. _qimage-image-information:

Image Information
-----------------

:sip:ref:`~PyQt6.QtGui.QImage` provides a collection of functions that can be used to obtain a variety of information about the image:

+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                       | Available Functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+=======================+==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| Geometry              | The :sip:ref:`~PyQt6.QtGui.QImage.size`, :sip:ref:`~PyQt6.QtGui.QImage.width`, :sip:ref:`~PyQt6.QtGui.QImage.height`, :sip:ref:`~PyQt6.QtGui.QImage.dotsPerMeterX`, and :sip:ref:`~PyQt6.QtGui.QImage.dotsPerMeterY` functions provide information about the image size and aspect ratio.                                                                                                                                                                                                                                                                                                                                                                                |
|                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                       | The :sip:ref:`~PyQt6.QtGui.QImage.rect` function returns the image's enclosing rectangle. The :sip:ref:`~PyQt6.QtGui.QImage.valid` function tells if a given pair of coordinates is within this rectangle. The :sip:ref:`~PyQt6.QtGui.QImage.offset` function returns the number of pixels by which the image is intended to be offset by when positioned relative to other images, which also can be manipulated using the :sip:ref:`~PyQt6.QtGui.QImage.setOffset` function.                                                                                                                                                                                           |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Colors                | The color of a pixel can be retrieved by passing its coordinates to the :sip:ref:`~PyQt6.QtGui.QImage.pixel` function. The :sip:ref:`~PyQt6.QtGui.QImage.pixel` function returns the color as a QRgb value indepedent of the image's format.                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                       | In case of monochrome and 8-bit images, the :sip:ref:`~PyQt6.QtGui.QImage.colorCount` and :sip:ref:`~PyQt6.QtGui.QImage.colorTable` functions provide information about the color components used to store the image data: The :sip:ref:`~PyQt6.QtGui.QImage.colorTable` function returns the image's entire color table. To obtain a single entry, use the :sip:ref:`~PyQt6.QtGui.QImage.pixelIndex` function to retrieve the pixel index for a given pair of coordinates, then use the :sip:ref:`~PyQt6.QtGui.QImage.color` function to retrieve the color. Note that if you create an 8-bit image manually, you have to set a valid color table on the image as well. |
|                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                       | The :sip:ref:`~PyQt6.QtGui.QImage.hasAlphaChannel` function tells if the image's format respects the alpha channel, or not. The :sip:ref:`~PyQt6.QtGui.QImage.allGray` and :sip:ref:`~PyQt6.QtGui.QImage.isGrayscale` functions tell whether an image's colors are all shades of gray.                                                                                                                                                                                                                                                                                                                                                                                   |
|                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                       | See also the Pixel Manipulation and Image Transformations sections.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Text                  | The :sip:ref:`~PyQt6.QtGui.QImage.text` function returns the image text associated with the given text key. An image's text keys can be retrieved using the :sip:ref:`~PyQt6.QtGui.QImage.textKeys` function. Use the :sip:ref:`~PyQt6.QtGui.QImage.setText` function to alter an image's text.                                                                                                                                                                                                                                                                                                                                                                          |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Low-level information | The :sip:ref:`~PyQt6.QtGui.QImage.depth` function returns the depth of the image. The supported depths are 1 (monochrome), 8, 16, 24 and 32 bits. The :sip:ref:`~PyQt6.QtGui.QImage.bitPlaneCount` function tells how many of those bits that are used. For more information see the Image Formats section.                                                                                                                                                                                                                                                                                                                                                              |
|                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                       | The :sip:ref:`~PyQt6.QtGui.QImage.format`, :sip:ref:`~PyQt6.QtGui.QImage.bytesPerLine`, and :sip:ref:`~PyQt6.QtGui.QImage.sizeInBytes` functions provide low-level information about the data stored in the image.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                       | The :sip:ref:`~PyQt6.QtGui.QImage.cacheKey` function returns a number that uniquely identifies the contents of this :sip:ref:`~PyQt6.QtGui.QImage` object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _qimage-pixel-manipulation:

Pixel Manipulation
------------------

The functions used to manipulate an image's pixels depend on the image format. The reason is that monochrome and 8-bit images are index-based and use a color lookup table, while 32-bit images store ARGB values directly. For more information on image formats, see the :ref:`qimage-image-formats` section.

In case of a 32-bit image, the :sip:ref:`~PyQt6.QtGui.QImage.setPixel` function can be used to alter the color of the pixel at the given coordinates to any other color specified as an ARGB quadruplet. To make a suitable QRgb value, use the :sip:ref:`~PyQt6.QtGui.qRgb` (adding a default alpha component to the given RGB values, i.e. creating an opaque color) or :sip:ref:`~PyQt6.QtGui.qRgba` function. For example:

+---------------------------------+------------------------------------------------------------------------------------------------+
| 32-bit                          |                                                                                                |
+=================================+================================================================================================+
| |image-qimage-32bit_scaled-png| | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_image_qimage.py |
|                                 |     :lines: 58-69                                                                              |
+---------------------------------+------------------------------------------------------------------------------------------------+

In case of a 8-bit and monchrome images, the pixel value is only an index from the image's color table. So the :sip:ref:`~PyQt6.QtGui.QImage.setPixel` function can only be used to alter the color of the pixel at the given coordinates to a predefined color from the image's color table, i.e. it can only change the pixel's index value. To alter or add a color to an image's color table, use the :sip:ref:`~PyQt6.QtGui.QImage.setColor` function.

An entry in the color table is an ARGB quadruplet encoded as an QRgb value. Use the :sip:ref:`~PyQt6.QtGui.qRgb` and :sip:ref:`~PyQt6.QtGui.qRgba` functions to make a suitable QRgb value for use with the :sip:ref:`~PyQt6.QtGui.QImage.setColor` function. For example:

+--------------------------------+------------------------------------------------------------------------------------------------+
| 8-bit                          |                                                                                                |
+================================+================================================================================================+
| |image-qimage-8bit_scaled-png| | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_image_qimage.py |
|                                |     :lines: 77-92                                                                              |
+--------------------------------+------------------------------------------------------------------------------------------------+

For images with more than 8-bit per color-channel. The methods :sip:ref:`~PyQt6.QtGui.QImage.setPixelColor` and :sip:ref:`~PyQt6.QtGui.QImage.pixelColor` can be used to set and get with :sip:ref:`~PyQt6.QtGui.QColor` values.

:sip:ref:`~PyQt6.QtGui.QImage` also provide the :sip:ref:`~PyQt6.QtGui.QImage.scanLine` function which returns a pointer to the pixel data at the scanline with the given index, and the :sip:ref:`~PyQt6.QtGui.QImage.bits` function which returns a pointer to the first pixel data (this is equivalent to ``scanLine(0)``).

.. _qimage-image-formats:

Image Formats
-------------

Each pixel stored in a :sip:ref:`~PyQt6.QtGui.QImage` is represented by an integer. The size of the integer varies depending on the format. :sip:ref:`~PyQt6.QtGui.QImage` supports several image formats described by the :sip:ref:`~PyQt6.QtGui.QImage.Format.Format` enum.

Monochrome images are stored using 1-bit indexes into a color table with at most two colors. There are two different types of monochrome images: big endian (MSB first) or little endian (LSB first) bit order.

8-bit images are stored using 8-bit indexes into a color table, i.e. they have a single byte per pixel. The color table is a QList<QRgb>, and the QRgb typedef is equivalent to an unsigned int containing an ARGB quadruplet on the format 0xAARRGGBB.

32-bit images have no color table; instead, each pixel contains an QRgb value. There are three different types of 32-bit images storing RGB (i.e. 0xffRRGGBB), ARGB and premultiplied ARGB values respectively. In the premultiplied format the red, green, and blue channels are multiplied by the alpha component divided by 255.

An image's format can be retrieved using the :sip:ref:`~PyQt6.QtGui.QImage.format` function. Use the :sip:ref:`~PyQt6.QtGui.QImage.convertToFormat` functions to convert an image into another format. The :sip:ref:`~PyQt6.QtGui.QImage.allGray` and :sip:ref:`~PyQt6.QtGui.QImage.isGrayscale` functions tell whether a color image can safely be converted to a grayscale image.

.. _qimage-image-transformations:

Image Transformations
---------------------

:sip:ref:`~PyQt6.QtGui.QImage` supports a number of functions for creating a new image that is a transformed version of the original: The :sip:ref:`~PyQt6.QtGui.QImage.createAlphaMask` function builds and returns a 1-bpp mask from the alpha buffer in this image, and the :sip:ref:`~PyQt6.QtGui.QImage.createHeuristicMask` function creates and returns a 1-bpp heuristic mask for this image. The latter function works by selecting a color from one of the corners, then chipping away pixels of that color starting at all the edges.

The :sip:ref:`~PyQt6.QtGui.QImage.mirrored` function returns a mirror of the image in the desired direction, the :sip:ref:`~PyQt6.QtGui.QImage.scaled` returns a copy of the image scaled to a rectangle of the desired measures, and the :sip:ref:`~PyQt6.QtGui.QImage.rgbSwapped` function constructs a BGR image from a RGB image.

The :sip:ref:`~PyQt6.QtGui.QImage.scaledToWidth` and :sip:ref:`~PyQt6.QtGui.QImage.scaledToHeight` functions return scaled copies of the image.

The :sip:ref:`~PyQt6.QtGui.QImage.transformed` function returns a copy of the image that is transformed with the given transformation matrix and transformation mode: Internally, the transformation matrix is adjusted to compensate for unwanted translation, i.e. :sip:ref:`~PyQt6.QtGui.QImage.transformed` returns the smallest image containing all transformed points of the original image. The static :sip:ref:`~PyQt6.QtGui.QImage.trueMatrix` function returns the actual matrix used for transforming the image.

There are also functions for changing attributes of an image in-place:

+-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Function                                        | Description                                                                                                       |
+=================================================+===================================================================================================================+
| :sip:ref:`~PyQt6.QtGui.QImage.setDotsPerMeterX` | Defines the aspect ratio by setting the number of pixels that fit horizontally in a physical meter.               |
+-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtGui.QImage.setDotsPerMeterY` | Defines the aspect ratio by setting the number of pixels that fit vertically in a physical meter.                 |
+-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtGui.QImage.fill`             | Fills the entire image with the given pixel value.                                                                |
+-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtGui.QImage.invertPixels`     | Inverts all pixel values in the image using the given :sip:ref:`~PyQt6.QtGui.QImage.InvertMode.InvertMode` value. |
+-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtGui.QImage.setColorTable`    | Sets the color table used to translate color indexes. Only monochrome and 8-bit formats.                          |
+-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtGui.QImage.setColorCount`    | Resizes the color table. Only monochrome and 8-bit formats.                                                       |
+-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageReader`, :sip:ref:`~PyQt6.QtGui.QImageWriter`, :sip:ref:`~PyQt6.QtGui.QPixmap`, `Image Composition Example <https://doc.qt.io/qt-6/qtwidgets-painting-imagecomposition-example.html>`_, `Image Viewer Example <https://doc.qt.io/qt-6/qtwidgets-widgets-imageviewer-example.html>`_, `Scribble Example <https://doc.qt.io/qt-6/qtwidgets-widgets-scribble-example.html>`_, `Pixelator Example <https://doc.qt.io/qt-6/qtwidgets-itemviews-pixelator-example.html>`_.

.. |image-qimage-32bit_scaled-png| image:: ../../../images/qimage-32bit_scaled.png
.. |image-qimage-8bit_scaled-png| image:: ../../../images/qimage-8bit_scaled.png
