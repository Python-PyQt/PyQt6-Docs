.. sip:class-description::
    :status: todo
    :brief: Off-screen image representation that can be used as a paint device
    :digest: 5802e35d21d3486a28e6749265cd82d6

The :sip:ref:`~PyQt6.QtGui.QPixmap` class is an off-screen image representation that can be used as a paint device.

Qt provides four classes for handling image data: :sip:ref:`~PyQt6.QtGui.QImage`, :sip:ref:`~PyQt6.QtGui.QPixmap`, :sip:ref:`~PyQt6.QtGui.QBitmap` and :sip:ref:`~PyQt6.QtGui.QPicture`. :sip:ref:`~PyQt6.QtGui.QImage` is designed and optimized for I/O, and for direct pixel access and manipulation, while :sip:ref:`~PyQt6.QtGui.QPixmap` is designed and optimized for showing images on screen. :sip:ref:`~PyQt6.QtGui.QBitmap` is only a convenience class that inherits :sip:ref:`~PyQt6.QtGui.QPixmap`, ensuring a depth of 1. The :sip:ref:`~PyQt6.QtGui.QPixmap.isQBitmap` function returns ``true`` if a :sip:ref:`~PyQt6.QtGui.QPixmap` object is really a bitmap, otherwise returns ``false``. Finally, the :sip:ref:`~PyQt6.QtGui.QPicture` class is a paint device that records and replays :sip:ref:`~PyQt6.QtGui.QPainter` commands.

A :sip:ref:`~PyQt6.QtGui.QPixmap` can easily be displayed on the screen using :sip:ref:`~PyQt6.QtWidgets.QLabel` or one of :sip:ref:`~PyQt6.QtWidgets.QAbstractButton`'s subclasses (such as :sip:ref:`~PyQt6.QtWidgets.QPushButton` and :sip:ref:`~PyQt6.QtWidgets.QToolButton`). :sip:ref:`~PyQt6.QtWidgets.QLabel` has a pixmap property, whereas :sip:ref:`~PyQt6.QtWidgets.QAbstractButton` has an icon property.

:sip:ref:`~PyQt6.QtGui.QPixmap` objects can be passed around by value since the :sip:ref:`~PyQt6.QtGui.QPixmap` class uses implicit data sharing. For more information, see the `Implicit Data Sharing <https://doc.qt.io/qt-6/implicit-sharing.html>`_ documentation. :sip:ref:`~PyQt6.QtGui.QPixmap` objects can also be streamed.

Note that the pixel data in a pixmap is internal and is managed by the underlying window system. Because :sip:ref:`~PyQt6.QtGui.QPixmap` is a :sip:ref:`~PyQt6.QtGui.QPaintDevice` subclass, :sip:ref:`~PyQt6.QtGui.QPainter` can be used to draw directly onto pixmaps. Pixels can only be accessed through :sip:ref:`~PyQt6.QtGui.QPainter` functions or by converting the :sip:ref:`~PyQt6.QtGui.QPixmap` to a :sip:ref:`~PyQt6.QtGui.QImage`. However, the :sip:ref:`~PyQt6.QtGui.QPixmap.fill` function is available for initializing the entire pixmap with a given color.

There are functions to convert between :sip:ref:`~PyQt6.QtGui.QImage` and :sip:ref:`~PyQt6.QtGui.QPixmap`. Typically, the :sip:ref:`~PyQt6.QtGui.QImage` class is used to load an image file, optionally manipulating the image data, before the :sip:ref:`~PyQt6.QtGui.QImage` object is converted into a :sip:ref:`~PyQt6.QtGui.QPixmap` to be shown on screen. Alternatively, if no manipulation is desired, the image file can be loaded directly into a :sip:ref:`~PyQt6.QtGui.QPixmap`.

:sip:ref:`~PyQt6.QtGui.QPixmap` provides a collection of functions that can be used to obtain a variety of information about the pixmap. In addition, there are several functions that enables transformation of the pixmap.

.. _qpixmap-reading-and-writing-image-files:

Reading and Writing Image Files
-------------------------------

:sip:ref:`~PyQt6.QtGui.QPixmap` provides several ways of reading an image file: The file can be loaded when constructing the :sip:ref:`~PyQt6.QtGui.QPixmap` object, or by using the :sip:ref:`~PyQt6.QtGui.QPixmap.load` or :sip:ref:`~PyQt6.QtGui.QPixmap.loadFromData` functions later on. When loading an image, the file name can either refer to an actual file on disk or to one of the application's embedded resources. See `The Qt Resource System <https://doc.qt.io/qt-6/resources.html>`_ overview for details on how to embed images and other resource files in the application's executable.

Simply call the :sip:ref:`~PyQt6.QtGui.QPixmap.save` function to save a :sip:ref:`~PyQt6.QtGui.QPixmap` object.

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

.. _qpixmap-pixmap-information:

Pixmap Information
------------------

:sip:ref:`~PyQt6.QtGui.QPixmap` provides a collection of functions that can be used to obtain a variety of information about the pixmap:

+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                       | Available Functions                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+=======================+=================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| Geometry              | The :sip:ref:`~PyQt6.QtGui.QPixmap.size`, :sip:ref:`~PyQt6.QtGui.QPixmap.width` and :sip:ref:`~PyQt6.QtGui.QPixmap.height` functions provide information about the pixmap's size. The :sip:ref:`~PyQt6.QtGui.QPixmap.rect` function returns the image's enclosing rectangle.                                                                                                                                                                                                    |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Alpha component       | The hasAlphaChannel() returns ``true`` if the pixmap has a format that respects the alpha channel, otherwise returns ``false``. The hasAlpha(), :sip:ref:`~PyQt6.QtGui.QPixmap.setMask` and :sip:ref:`~PyQt6.QtGui.QPixmap.mask` functions are legacy and should not be used. They are potentially very slow.                                                                                                                                                                   |
|                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                       | The :sip:ref:`~PyQt6.QtGui.QPixmap.createHeuristicMask` function creates and returns a 1-bpp heuristic mask (i.e. a :sip:ref:`~PyQt6.QtGui.QBitmap`) for this pixmap. It works by selecting a color from one of the corners and then chipping away pixels of that color, starting at all the edges. The :sip:ref:`~PyQt6.QtGui.QPixmap.createMaskFromColor` function creates and returns a mask (i.e. a :sip:ref:`~PyQt6.QtGui.QBitmap`) for the pixmap based on a given color. |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Low-level information | The :sip:ref:`~PyQt6.QtGui.QPixmap.depth` function returns the depth of the pixmap. The defaultDepth() function returns the default depth, i.e. the depth used by the application on the given screen.                                                                                                                                                                                                                                                                          |
|                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                       | The :sip:ref:`~PyQt6.QtGui.QPixmap.cacheKey` function returns a number that uniquely identifies the contents of the :sip:ref:`~PyQt6.QtGui.QPixmap` object.                                                                                                                                                                                                                                                                                                                     |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _qpixmap-pixmap-conversion:

Pixmap Conversion
-----------------

A :sip:ref:`~PyQt6.QtGui.QPixmap` object can be converted into a :sip:ref:`~PyQt6.QtGui.QImage` using the :sip:ref:`~PyQt6.QtGui.QPixmap.toImage` function. Likewise, a :sip:ref:`~PyQt6.QtGui.QImage` can be converted into a :sip:ref:`~PyQt6.QtGui.QPixmap` using the :sip:ref:`~PyQt6.QtGui.QPixmap.fromImage`. If this is too expensive an operation, you can use :sip:ref:`~PyQt6.QtGui.QBitmap.fromImage` instead.

To convert a :sip:ref:`~PyQt6.QtGui.QPixmap` to and from HICON you can use the :sip:ref:`~PyQt6.QtGui.QImage.toHICON` and :sip:ref:`~PyQt6.QtGui.QImage.fromHICON` functions respectively (after converting the :sip:ref:`~PyQt6.QtGui.QPixmap` to a :sip:ref:`~PyQt6.QtGui.QImage`, as explained above).

.. _qpixmap-pixmap-transformations:

Pixmap Transformations
----------------------

:sip:ref:`~PyQt6.QtGui.QPixmap` supports a number of functions for creating a new pixmap that is a transformed version of the original:

The :sip:ref:`~PyQt6.QtGui.QPixmap.scaled`, :sip:ref:`~PyQt6.QtGui.QPixmap.scaledToWidth` and :sip:ref:`~PyQt6.QtGui.QPixmap.scaledToHeight` functions return scaled copies of the pixmap, while the :sip:ref:`~PyQt6.QtGui.QPixmap.copy` function creates a :sip:ref:`~PyQt6.QtGui.QPixmap` that is a plain copy of the original one.

The transformed() function returns a copy of the pixmap that is transformed with the given transformation matrix and transformation mode: Internally, the transformation matrix is adjusted to compensate for unwanted translation, i.e. transformed() returns the smallest pixmap containing all transformed points of the original pixmap. The static :sip:ref:`~PyQt6.QtGui.QPixmap.trueMatrix` function returns the actual matrix used for transforming the pixmap.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QBitmap`, :sip:ref:`~PyQt6.QtGui.QImage`, :sip:ref:`~PyQt6.QtGui.QImageReader`, :sip:ref:`~PyQt6.QtGui.QImageWriter`.
