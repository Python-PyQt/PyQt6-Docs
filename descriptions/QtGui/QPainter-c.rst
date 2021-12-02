.. sip:class-description::
    :status: todo
    :brief: Performs low-level painting on widgets and other paint devices
    :digest: df849302ee49323f70149d34d65629e2

The :sip:ref:`~PyQt6.QtGui.QPainter` class performs low-level painting on widgets and other paint devices.

:sip:ref:`~PyQt6.QtGui.QPainter` provides highly optimized functions to do most of the drawing GUI programs require. It can draw everything from simple lines to complex shapes like pies and chords. It can also draw aligned text and pixmaps. Normally, it draws in a "natural" coordinate system, but it can also do view and world transformation. :sip:ref:`~PyQt6.QtGui.QPainter` can operate on any object that inherits the :sip:ref:`~PyQt6.QtGui.QPaintDevice` class.

The common use of :sip:ref:`~PyQt6.QtGui.QPainter` is inside a widget's paint event: Construct and customize (e.g. set the pen or the brush) the painter. Then draw. Remember to destroy the :sip:ref:`~PyQt6.QtGui.QPainter` object after drawing. For example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainter.py
    :lines: 74-80

The core functionality of :sip:ref:`~PyQt6.QtGui.QPainter` is drawing, but the class also provide several functions that allows you to customize :sip:ref:`~PyQt6.QtGui.QPainter`'s settings and its rendering quality, and others that enable clipping. In addition you can control how different shapes are merged together by specifying the painter's composition mode.

The :sip:ref:`~PyQt6.QtGui.QPainter.isActive` function indicates whether the painter is active. A painter is activated by the :sip:ref:`~PyQt6.QtGui.QPainter.begin` function and the constructor that takes a :sip:ref:`~PyQt6.QtGui.QPaintDevice` argument. The :sip:ref:`~PyQt6.QtGui.QPainter.end` function, and the destructor, deactivates it.

Together with the :sip:ref:`~PyQt6.QtGui.QPaintDevice` and :sip:ref:`~PyQt6.QtGui.QPaintEngine` classes, :sip:ref:`~PyQt6.QtGui.QPainter` form the basis for Qt's paint system. :sip:ref:`~PyQt6.QtGui.QPainter` is the class used to perform drawing operations. :sip:ref:`~PyQt6.QtGui.QPaintDevice` represents a device that can be painted on using a :sip:ref:`~PyQt6.QtGui.QPainter`. :sip:ref:`~PyQt6.QtGui.QPaintEngine` provides the interface that the painter uses to draw onto different types of devices. If the painter is active, :sip:ref:`~PyQt6.QtGui.QPainter.device` returns the paint device on which the painter paints, and :sip:ref:`~PyQt6.QtGui.QPainter.paintEngine` returns the paint engine that the painter is currently operating on. For more information, see the `Paint System <https://doc.qt.io/qt-6/paintsystem.html>`_.

Sometimes it is desirable to make someone else paint on an unusual :sip:ref:`~PyQt6.QtGui.QPaintDevice`. :sip:ref:`~PyQt6.QtGui.QPainter` supports a static function to do this, setRedirected().

**Warning:** When the paintdevice is a widget, :sip:ref:`~PyQt6.QtGui.QPainter` can only be used inside a paintEvent() function or in a function called by paintEvent().

.. _qpainter-settings:

Settings
--------

There are several settings that you can customize to make :sip:ref:`~PyQt6.QtGui.QPainter` draw according to your preferences:

* :sip:ref:`~PyQt6.QtGui.QPainter.font` is the font used for drawing text. If the painter :sip:ref:`~PyQt6.QtGui.QPainter.isActive`, you can retrieve information about the currently set font, and its metrics, using the :sip:ref:`~PyQt6.QtGui.QPainter.fontInfo` and :sip:ref:`~PyQt6.QtGui.QPainter.fontMetrics` functions respectively.

* :sip:ref:`~PyQt6.QtGui.QPainter.brush` defines the color or pattern that is used for filling shapes.

* :sip:ref:`~PyQt6.QtGui.QPainter.pen` defines the color or stipple that is used for drawing lines or boundaries.

* :sip:ref:`~PyQt6.QtGui.QPainter.backgroundMode` defines whether there is a :sip:ref:`~PyQt6.QtGui.QPainter.background` or not, i.e it is either :sip:ref:`~PyQt6.QtCore.Qt.BGMode.OpaqueMode` or :sip:ref:`~PyQt6.QtCore.Qt.BGMode.TransparentMode`.

* :sip:ref:`~PyQt6.QtGui.QPainter.background` only applies when :sip:ref:`~PyQt6.QtGui.QPainter.backgroundMode` is :sip:ref:`~PyQt6.QtCore.Qt.BGMode.OpaqueMode` and :sip:ref:`~PyQt6.QtGui.QPainter.pen` is a stipple. In that case, it describes the color of the background pixels in the stipple.

* :sip:ref:`~PyQt6.QtGui.QPainter.brushOrigin` defines the origin of the tiled brushes, normally the origin of widget's background.

* :sip:ref:`~PyQt6.QtGui.QPainter.viewport`, :sip:ref:`~PyQt6.QtGui.QPainter.window`, :sip:ref:`~PyQt6.QtGui.QPainter.worldTransform` make up the painter's coordinate transformation system. For more information, see the :ref:`qpainter-coordinate-transformations` section and the `Coordinate System <https://doc.qt.io/qt-6/coordsys.html>`_ documentation.

* :sip:ref:`~PyQt6.QtGui.QPainter.hasClipping` tells whether the painter clips at all. (The paint device clips, too.) If the painter clips, it clips to :sip:ref:`~PyQt6.QtGui.QPainter.clipRegion`.

* :sip:ref:`~PyQt6.QtGui.QPainter.layoutDirection` defines the layout direction used by the painter when drawing text.

* :sip:ref:`~PyQt6.QtGui.QPainter.worldMatrixEnabled` tells whether world transformation is enabled.

* :sip:ref:`~PyQt6.QtGui.QPainter.viewTransformEnabled` tells whether view transformation is enabled.

Note that some of these settings mirror settings in some paint devices, e.g. :sip:ref:`~PyQt6.QtWidgets.QWidget.font`. The :sip:ref:`~PyQt6.QtGui.QPainter.begin` function (or equivalently the :sip:ref:`~PyQt6.QtGui.QPainter` constructor) copies these attributes from the paint device.

You can at any time save the :sip:ref:`~PyQt6.QtGui.QPainter`'s state by calling the :sip:ref:`~PyQt6.QtGui.QPainter.save` function which saves all the available settings on an internal stack. The :sip:ref:`~PyQt6.QtGui.QPainter.restore` function pops them back.

.. _qpainter-drawing:

Drawing
-------

:sip:ref:`~PyQt6.QtGui.QPainter` provides functions to draw most primitives: :sip:ref:`~PyQt6.QtGui.QPainter.drawPoint`, :sip:ref:`~PyQt6.QtGui.QPainter.drawPoints`, :sip:ref:`~PyQt6.QtGui.QPainter.drawLine`, :sip:ref:`~PyQt6.QtGui.QPainter.drawRect`, :sip:ref:`~PyQt6.QtGui.QPainter.drawRoundedRect`, :sip:ref:`~PyQt6.QtGui.QPainter.drawEllipse`, :sip:ref:`~PyQt6.QtGui.QPainter.drawArc`, :sip:ref:`~PyQt6.QtGui.QPainter.drawPie`, :sip:ref:`~PyQt6.QtGui.QPainter.drawChord`, :sip:ref:`~PyQt6.QtGui.QPainter.drawPolyline`, :sip:ref:`~PyQt6.QtGui.QPainter.drawPolygon`, :sip:ref:`~PyQt6.QtGui.QPainter.drawConvexPolygon` and drawCubicBezier(). The two convenience functions, :sip:ref:`~PyQt6.QtGui.QPainter.drawRects` and :sip:ref:`~PyQt6.QtGui.QPainter.drawLines`, draw the given number of rectangles or lines in the given array of :sip:ref:`~PyQt6.QtCore.QRect` or :sip:ref:`~PyQt6.QtCore.QLine` using the current pen and brush.

The :sip:ref:`~PyQt6.QtGui.QPainter` class also provides the :sip:ref:`~PyQt6.QtGui.QPainter.fillRect` function which fills the given :sip:ref:`~PyQt6.QtCore.QRect`, with the given :sip:ref:`~PyQt6.QtGui.QBrush`, and the :sip:ref:`~PyQt6.QtGui.QPainter.eraseRect` function that erases the area inside the given rectangle.

All of these functions have both integer and floating point versions.

+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image-qpainter-basicdrawing-png| | **Basic Drawing Example**                                                                                                                                                                                                  |
|                                   |                                                                                                                                                                                                                            |
|                                   | The `Basic Drawing <https://doc.qt.io/qt-6/qtwidgets-painting-basicdrawing-example.html>`_ example shows how to display basic graphics primitives in a variety of styles using the :sip:ref:`~PyQt6.QtGui.QPainter` class. |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

If you need to draw a complex shape, especially if you need to do so repeatedly, consider creating a :sip:ref:`~PyQt6.QtGui.QPainterPath` and drawing it using :sip:ref:`~PyQt6.QtGui.QPainter.drawPath`.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| **Painter Paths example**                                                                                                                                                     | |image-qpainter-painterpaths-png| |
|                                                                                                                                                                               |                                   |
| The :sip:ref:`~PyQt6.QtGui.QPainterPath` class provides a container for painting operations, enabling graphical shapes to be constructed and reused.                          |                                   |
|                                                                                                                                                                               |                                   |
| The `Painter Paths <https://doc.qt.io/qt-6/qtwidgets-painting-painterpaths-example.html>`_ example shows how painter paths can be used to build complex shapes for rendering. |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

:sip:ref:`~PyQt6.QtGui.QPainter` also provides the :sip:ref:`~PyQt6.QtGui.QPainter.fillPath` function which fills the given :sip:ref:`~PyQt6.QtGui.QPainterPath` with the given :sip:ref:`~PyQt6.QtGui.QBrush`, and the :sip:ref:`~PyQt6.QtGui.QPainter.strokePath` function that draws the outline of the given path (i.e. strokes the path).

See also the `Vector Deformation <https://doc.qt.io/qt-6/qtwidgets-painting-deform-example.html>`_ example which shows how to use advanced vector techniques to draw text using a :sip:ref:`~PyQt6.QtGui.QPainterPath`, the `Gradients <https://doc.qt.io/qt-6/qtwidgets-painting-gradients-example.html>`_ example which shows the different types of gradients that are available in Qt, and the `Path Stroking <https://doc.qt.io/qt-6/qtwidgets-painting-pathstroke-example.html>`_ example which shows Qt's built-in dash patterns and shows how custom patterns can be used to extend the range of available patterns.

+---------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| `Vector Deformation <https://doc.qt.io/qt-6/qtwidgets-painting-deform-example.html>`_ | `Gradients <https://doc.qt.io/qt-6/qtwidgets-painting-gradients-example.html>`_ | `Path Stroking <https://doc.qt.io/qt-6/qtwidgets-painting-pathstroke-example.html>`_ |
+=======================================================================================+=================================================================================+======================================================================================+
| |image-qpainter-vectordeformation-png|                                                | |image-qpainter-gradients-png|                                                  | |image-qpainter-pathstroking-png|                                                    |
+---------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+

Text drawing is done using :sip:ref:`~PyQt6.QtGui.QPainter.drawText`. When you need fine-grained positioning, :sip:ref:`~PyQt6.QtGui.QPainter.boundingRect` tells you where a given :sip:ref:`~PyQt6.QtGui.QPainter.drawText` command will draw.

.. _qpainter-drawing-pixmaps-and-images:

Drawing Pixmaps and Images
--------------------------

There are functions to draw pixmaps/images, namely :sip:ref:`~PyQt6.QtGui.QPainter.drawPixmap`, :sip:ref:`~PyQt6.QtGui.QPainter.drawImage` and :sip:ref:`~PyQt6.QtGui.QPainter.drawTiledPixmap`. Both :sip:ref:`~PyQt6.QtGui.QPainter.drawPixmap` and :sip:ref:`~PyQt6.QtGui.QPainter.drawImage` produce the same result, except that :sip:ref:`~PyQt6.QtGui.QPainter.drawPixmap` is faster on-screen while :sip:ref:`~PyQt6.QtGui.QPainter.drawImage` may be faster on a :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` or other devices.

There is a :sip:ref:`~PyQt6.QtGui.QPainter.drawPicture` function that draws the contents of an entire :sip:ref:`~PyQt6.QtGui.QPicture`. The :sip:ref:`~PyQt6.QtGui.QPainter.drawPicture` function is the only function that disregards all the painter's settings as :sip:ref:`~PyQt6.QtGui.QPicture` has its own settings.

.. _qpainter-drawing-high-resolution-versions-of-pixmaps-and-images:

Drawing High Resolution Versions of Pixmaps and Images
......................................................

High resolution versions of pixmaps have a *device pixel ratio* value larger than 1 (see :sip:ref:`~PyQt6.QtGui.QImageReader`, :sip:ref:`~PyQt6.QtGui.QPixmap.devicePixelRatio`). Should it match the value of the underlying :sip:ref:`~PyQt6.QtGui.QPaintDevice`, it is drawn directly onto the device with no additional transformation applied.

This is for example the case when drawing a :sip:ref:`~PyQt6.QtGui.QPixmap` of 64x64 pixels size with a device pixel ratio of 2 onto a high DPI screen which also has a device pixel ratio of 2. Note that the pixmap is then effectively 32x32 pixels in *user space*. Code paths in Qt that calculate layout geometry based on the pixmap size will use this size. The net effect of this is that the pixmap is displayed as high DPI pixmap rather than a large pixmap.

.. _qpainter-rendering-quality:

Rendering Quality
-----------------

To get the optimal rendering result using :sip:ref:`~PyQt6.QtGui.QPainter`, you should use the platform independent :sip:ref:`~PyQt6.QtGui.QImage` as paint device; i.e. using :sip:ref:`~PyQt6.QtGui.QImage` will ensure that the result has an identical pixel representation on any platform.

The :sip:ref:`~PyQt6.QtGui.QPainter` class also provides a means of controlling the rendering quality through its :sip:ref:`~PyQt6.QtGui.QPainter.RenderHint.RenderHint` enum and the support for floating point precision: All the functions for drawing primitives has a floating point version. These are often used in combination with the :sip:ref:`~PyQt6.QtGui.QPainter.RenderHint.RenderHint` render hint.

+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image-qpainter-concentriccircles-png| | **Concentric Circles Example**                                                                                                                                                                                                                       |
|                                        |                                                                                                                                                                                                                                                      |
|                                        | The `Concentric Circles <https://doc.qt.io/qt-6/qtwidgets-painting-concentriccircles-example.html>`_ example shows the improved rendering quality that can be obtained using floating point precision and anti-aliasing when drawing custom widgets. |
|                                        |                                                                                                                                                                                                                                                      |
|                                        | The application's main window displays several widgets which are drawn using the various combinations of precision and anti-aliasing.                                                                                                                |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The :sip:ref:`~PyQt6.QtGui.QPainter.RenderHint.RenderHint` enum specifies flags to :sip:ref:`~PyQt6.QtGui.QPainter` that may or may not be respected by any given engine. :sip:ref:`~PyQt6.QtGui.QPainter.RenderHint.RenderHint` indicates that the engine should antialias edges of primitives if possible, :sip:ref:`~PyQt6.QtGui.QPainter.RenderHint.RenderHint` indicates that the engine should antialias text if possible, and the :sip:ref:`~PyQt6.QtGui.QPainter.RenderHint.RenderHint` indicates that the engine should use a smooth pixmap transformation algorithm.

The :sip:ref:`~PyQt6.QtGui.QPainter.renderHints` function returns a flag that specifies the rendering hints that are set for this painter. Use the :sip:ref:`~PyQt6.QtGui.QPainter.setRenderHint` function to set or clear the currently set RenderHints.

.. _qpainter-coordinate-transformations:

Coordinate Transformations
--------------------------

Normally, the :sip:ref:`~PyQt6.QtGui.QPainter` operates on the device's own coordinate system (usually pixels), but :sip:ref:`~PyQt6.QtGui.QPainter` has good support for coordinate transformations.

+----------------------------+-----------------------------------------+----------------------------------------+--------------------------------------------+
| nop                        | :sip:ref:`~PyQt6.QtGui.QPainter.rotate` | :sip:ref:`~PyQt6.QtGui.QPainter.scale` | :sip:ref:`~PyQt6.QtGui.QPainter.translate` |
+============================+=========================================+========================================+============================================+
| |image-qpainter-clock-png| | |image-qpainter-rotation-png|           | |image-qpainter-scale-png|             | |image-qpainter-translation-png|           |
+----------------------------+-----------------------------------------+----------------------------------------+--------------------------------------------+

The most commonly used transformations are scaling, rotation, translation and shearing. Use the :sip:ref:`~PyQt6.QtGui.QPainter.scale` function to scale the coordinate system by a given offset, the :sip:ref:`~PyQt6.QtGui.QPainter.rotate` function to rotate it clockwise and :sip:ref:`~PyQt6.QtGui.QPainter.translate` to translate it (i.e. adding a given offset to the points). You can also twist the coordinate system around the origin using the :sip:ref:`~PyQt6.QtGui.QPainter.shear` function. See the `Affine Transformations <https://doc.qt.io/qt-6/qtwidgets-painting-affine-example.html>`_ example for a visualization of a sheared coordinate system.

See also the `Transformations <https://doc.qt.io/qt-6/qtwidgets-painting-transformations-example.html>`_ example which shows how transformations influence the way that :sip:ref:`~PyQt6.QtGui.QPainter` renders graphics primitives. In particular it shows how the order of transformations affects the result.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------+
| **Affine Transformations Example**                                                                                                                                                                                                                                                                 | |image-qpainter-affinetransformations-png| |
|                                                                                                                                                                                                                                                                                                    |                                            |
| The `Affine Transformations <https://doc.qt.io/qt-6/qtwidgets-painting-affine-example.html>`_ example shows Qt's ability to perform affine transformations on painting operations. The demo also allows the user to experiment with the transformation operations and see the results immediately. |                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------+

All the transformation operations operate on the transformation :sip:ref:`~PyQt6.QtGui.QPainter.worldTransform`. A matrix transforms a point in the plane to another point. For more information about the transformation matrix, see the `Coordinate System <https://doc.qt.io/qt-6/coordsys.html>`_ and :sip:ref:`~PyQt6.QtGui.QTransform` documentation.

The :sip:ref:`~PyQt6.QtGui.QPainter.setWorldTransform` function can replace or add to the currently set :sip:ref:`~PyQt6.QtGui.QPainter.worldTransform`. The :sip:ref:`~PyQt6.QtGui.QPainter.resetTransform` function resets any transformations that were made using :sip:ref:`~PyQt6.QtGui.QPainter.translate`, :sip:ref:`~PyQt6.QtGui.QPainter.scale`, :sip:ref:`~PyQt6.QtGui.QPainter.shear`, :sip:ref:`~PyQt6.QtGui.QPainter.rotate`, :sip:ref:`~PyQt6.QtGui.QPainter.setWorldTransform`, :sip:ref:`~PyQt6.QtGui.QPainter.setViewport` and :sip:ref:`~PyQt6.QtGui.QPainter.setWindow` functions. The :sip:ref:`~PyQt6.QtGui.QPainter.deviceTransform` returns the matrix that transforms from logical coordinates to device coordinates of the platform dependent paint device. The latter function is only needed when using platform painting commands on the platform dependent handle, and the platform does not do transformations nativly.

When drawing with :sip:ref:`~PyQt6.QtGui.QPainter`, we specify points using logical coordinates which then are converted into the physical coordinates of the paint device. The mapping of the logical coordinates to the physical coordinates are handled by :sip:ref:`~PyQt6.QtGui.QPainter`'s :sip:ref:`~PyQt6.QtGui.QPainter.combinedTransform`, a combination of :sip:ref:`~PyQt6.QtGui.QPainter.viewport` and :sip:ref:`~PyQt6.QtGui.QPainter.window` and :sip:ref:`~PyQt6.QtGui.QPainter.worldTransform`. The :sip:ref:`~PyQt6.QtGui.QPainter.viewport` represents the physical coordinates specifying an arbitrary rectangle, the :sip:ref:`~PyQt6.QtGui.QPainter.window` describes the same rectangle in logical coordinates, and the :sip:ref:`~PyQt6.QtGui.QPainter.worldTransform` is identical with the transformation matrix.

See also `Coordinate System <https://doc.qt.io/qt-6/coordsys.html>`_

.. _qpainter-clipping:

Clipping
--------

:sip:ref:`~PyQt6.QtGui.QPainter` can clip any drawing operation to a rectangle, a region, or a vector path. The current clip is available using the functions :sip:ref:`~PyQt6.QtGui.QPainter.clipRegion` and :sip:ref:`~PyQt6.QtGui.QPainter.clipPath`. Whether paths or regions are preferred (faster) depends on the underlying :sip:ref:`~PyQt6.QtGui.QPainter.paintEngine`. For example, the :sip:ref:`~PyQt6.QtGui.QImage` paint engine prefers paths while the X11 paint engine prefers regions. Setting a clip is done in the painters logical coordinates.

After :sip:ref:`~PyQt6.QtGui.QPainter`'s clipping, the paint device may also clip. For example, most widgets clip away the pixels used by child widgets, and most printers clip away an area near the edges of the paper. This additional clipping is not reflected by the return value of :sip:ref:`~PyQt6.QtGui.QPainter.clipRegion` or :sip:ref:`~PyQt6.QtGui.QPainter.hasClipping`.

Composition Modes
-----------------

.. _qpainter-composition-modes:

:sip:ref:`~PyQt6.QtGui.QPainter` provides the :sip:ref:`~PyQt6.QtGui.QPainter.CompositionMode.CompositionMode` enum which defines the Porter-Duff rules for digital image compositing; it describes a model for combining the pixels in one image, the source, with the pixels in another image, the destination.

The two most common forms of composition are :sip:ref:`~PyQt6.QtGui.QPainter.CompositionMode` and :sip:ref:`~PyQt6.QtGui.QPainter.CompositionMode`. :sip:ref:`~PyQt6.QtGui.QPainter.CompositionMode` is used to draw opaque objects onto a paint device. In this mode, each pixel in the source replaces the corresponding pixel in the destination. In :sip:ref:`~PyQt6.QtGui.QPainter.CompositionMode` composition mode, the source object is transparent and is drawn on top of the destination.

Note that composition transformation operates pixelwise. For that reason, there is a difference between using the graphic primitive itself and its bounding rectangle: The bounding rect contains pixels with alpha == 0 (i.e the pixels surrounding the primitive). These pixels will overwrite the other image's pixels, effectively clearing those, while the primitive only overwrites its own area.

+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image-qpainter-compositiondemo-png| | **Composition Modes Example**                                                                                                                                                                                                             |
|                                      |                                                                                                                                                                                                                                           |
|                                      | The `Composition Modes <https://doc.qt.io/qt-6/qtwidgets-painting-composition-example.html>`_ example, available in Qt's examples directory, allows you to experiment with the various composition modes and see the results immediately. |
+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Limitations
-----------

.. _qpainter-limitations:

If you are using coordinates with Qt's raster-based paint engine, it is important to note that, while coordinates greater than +/- 2\ :sup:`15` can be used, any painting performed with coordinates outside this range is not guaranteed to be shown; the drawing may be clipped. This is due to the use of ``short int`` in the implementation.

The outlines generated by Qt's stroker are only an approximation when dealing with curved shapes. It is in most cases impossible to represent the outline of a bezier curve segment using another bezier curve segment, and so Qt approximates the curve outlines by using several smaller curves. For performance reasons there is a limit to how many curves Qt uses for these outlines, and thus when using large pen widths or scales the outline error increases. To generate outlines with smaller errors it is possible to use the :sip:ref:`~PyQt6.QtGui.QPainterPathStroker` class, which has the setCurveThreshold member function which let's the user specify the error tolerance. Another workaround is to convert the paths to polygons first and then draw the polygons instead.

.. _qpainter-performance:

Performance
-----------

:sip:ref:`~PyQt6.QtGui.QPainter` is a rich framework that allows developers to do a great variety of graphical operations, such as gradients, composition modes and vector graphics. And :sip:ref:`~PyQt6.QtGui.QPainter` can do this across a variety of different hardware and software stacks. Naturally the underlying combination of hardware and software has some implications for performance, and ensuring that every single operation is fast in combination with all the various combinations of composition modes, brushes, clipping, transformation, etc, is close to an impossible task because of the number of permutations. As a compromise we have selected a subset of the :sip:ref:`~PyQt6.QtGui.QPainter` API and backends, where performance is guaranteed to be as good as we can sensibly get it for the given combination of hardware and software.

The backends we focus on as high-performance engines are:

* Raster - This backend implements all rendering in pure software and is always used to render into QImages. For optimal performance only use the format types :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_ARGB32_Premultiplied`, :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_RGB32` or :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_RGB16`. Any other format, including :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_ARGB32`, has significantly worse performance. This engine is used by default for :sip:ref:`~PyQt6.QtWidgets.QWidget` and :sip:ref:`~PyQt6.QtGui.QPixmap`.

* OpenGL 2.0 (ES) - This backend is the primary backend for hardware accelerated graphics. It can be run on desktop machines and embedded devices supporting the OpenGL 2.0 or OpenGL/ES 2.0 specification. This includes most graphics chips produced in the last couple of years. The engine can be enabled by using :sip:ref:`~PyQt6.QtGui.QPainter` onto a :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget`.

These operations are:

* Simple transformations, meaning translation and scaling, pluss 0, 90, 180, 270 degree rotations.

* ``drawPixmap()`` in combination with simple transformations and opacity with non-smooth transformation mode (``QPainter::SmoothPixmapTransform`` not enabled as a render hint).

* Rectangle fills with solid color, two-color linear gradients and simple transforms.

* Rectangular clipping with simple transformations and intersect clip.

* Composition Modes ``QPainter::CompositionMode_Source`` and :sip:ref:`~PyQt6.QtGui.QPainter.CompositionMode.CompositionMode_SourceOver`.

* Rounded rectangle filling using solid color and two-color linear gradients fills.

* 3x3 patched pixmaps, via .

This list gives an indication of which features to safely use in an application where performance is critical. For certain setups, other operations may be fast too, but before making extensive use of them, it is recommended to benchmark and verify them on the system where the software will run in the end. There are also cases where expensive operations are ok to use, for instance when the result is cached in a :sip:ref:`~PyQt6.QtGui.QPixmap`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPaintDevice`, :sip:ref:`~PyQt6.QtGui.QPaintEngine`, `Qt SVG <https://doc.qt.io/qt-6/qtsvg-index.html>`_, `Basic Drawing Example <https://doc.qt.io/qt-6/qtwidgets-painting-basicdrawing-example.html>`_, `Drawing Utility Functions <https://doc.qt.io/qt-6/qdrawutil-h.html>`_.

.. |image-qpainter-basicdrawing-png| image:: ../../../images/qpainter-basicdrawing.png
.. |image-qpainter-painterpaths-png| image:: ../../../images/qpainter-painterpaths.png
.. |image-qpainter-vectordeformation-png| image:: ../../../images/qpainter-vectordeformation.png
.. |image-qpainter-gradients-png| image:: ../../../images/qpainter-gradients.png
.. |image-qpainter-pathstroking-png| image:: ../../../images/qpainter-pathstroking.png
.. |image-qpainter-concentriccircles-png| image:: ../../../images/qpainter-concentriccircles.png
.. |image-qpainter-clock-png| image:: ../../../images/qpainter-clock.png
.. |image-qpainter-rotation-png| image:: ../../../images/qpainter-rotation.png
.. |image-qpainter-scale-png| image:: ../../../images/qpainter-scale.png
.. |image-qpainter-translation-png| image:: ../../../images/qpainter-translation.png
.. |image-qpainter-affinetransformations-png| image:: ../../../images/qpainter-affinetransformations.png
.. |image-qpainter-compositiondemo-png| image:: ../../../images/qpainter-compositiondemo.png
