.. sip:class-description::
    :status: todo
    :brief: Used to draw the contents of SVG files onto paint devices
    :digest: 030df26e2b9d85d8e01c9f74cdb6b9e2

The :sip:ref:`~PyQt6.QtSvg.QSvgRenderer` class is used to draw the contents of SVG files onto paint devices.

Using :sip:ref:`~PyQt6.QtSvg.QSvgRenderer`, Scalable Vector Graphics (SVG) can be rendered onto any :sip:ref:`~PyQt6.QtGui.QPaintDevice` subclass, including :sip:ref:`~PyQt6.QtWidgets.QWidget`, :sip:ref:`~PyQt6.QtGui.QImage`, and QGLWidget.

:sip:ref:`~PyQt6.QtSvg.QSvgRenderer` provides an API that supports basic features of SVG rendering, such as loading and rendering of static drawings, and more interactive features like animation. Since the rendering is performed using :sip:ref:`~PyQt6.QtGui.QPainter`, SVG drawings can be rendered on any subclass of :sip:ref:`~PyQt6.QtGui.QPaintDevice`.

SVG drawings are either loaded when an :sip:ref:`~PyQt6.QtSvg.QSvgRenderer` is constructed, or loaded later using the :sip:ref:`~PyQt6.QtSvg.QSvgRenderer.load` functions. Data is either supplied directly as serialized XML, or indirectly using a file name. If a valid file has been loaded, either when the renderer is constructed or at some later time, :sip:ref:`~PyQt6.QtSvg.QSvgRenderer.isValid` returns true; otherwise it returns false. :sip:ref:`~PyQt6.QtSvg.QSvgRenderer` provides the :sip:ref:`~PyQt6.QtSvg.QSvgRenderer.render` slot to render the current document, or the current frame of an animated document, using a given painter.

The :sip:ref:`~PyQt6.QtSvg.QSvgRenderer.defaultSize` function provides information about the amount of space that is required to render the currently loaded SVG file. This is useful for paint devices, such as :sip:ref:`~PyQt6.QtWidgets.QWidget`, that often need to supply a size hint to their parent layout. The default size of a drawing may differ from its visible area, found using the :sip:ref:`~PyQt6.QtSvg.QSvgRenderer.viewBox` property.

Animated SVG drawings are supported, and can be controlled with a simple collection of functions and properties:

* The :sip:ref:`~PyQt6.QtSvg.QSvgRenderer.animated` function indicates whether a drawing contains animation information.

* The :sip:ref:`~PyQt6.QtSvg.QSvgRenderer.framesPerSecond` property contains the rate at which the animation plays.

Finally, the :sip:ref:`~PyQt6.QtSvg.QSvgRenderer` class provides the :sip:ref:`~PyQt6.QtSvg.QSvgRenderer.repaintNeeded` signal which is emitted whenever the rendering of the document needs to be updated.

.. seealso:: :sip:ref:`~PyQt6.QtSvgWidgets.QSvgWidget`, :sip:ref:`~PyQt6.Qt SVG C++ Classes`, :sip:ref:`~PyQt6.QtGui.QPicture`.
