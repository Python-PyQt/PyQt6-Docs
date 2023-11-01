.. sip:class-description::
    :status: todo
    :brief: Paint device that is used to create SVG drawings
    :digest: 9193377f8744822a80d66901ac9db87e

The :sip:ref:`~PyQt6.QtSvg.QSvgGenerator` class provides a paint device that is used to create SVG drawings.

This paint device represents a Scalable Vector Graphics (SVG) drawing. Like :sip:ref:`~PyQt6.QtPrintSupport.QPrinter`, it is designed as a write-only device that generates output in a specific format.

To write an SVG file, you first need to configure the output by setting the :sip:ref:`~PyQt6.QtSvg.QSvgGenerator.fileName` or :sip:ref:`~PyQt6.QtSvg.QSvgGenerator.outputDevice` properties. It is usually necessary to specify the size of the drawing by setting the :sip:ref:`~PyQt6.QtSvg.QSvgGenerator.size` property, and in some cases where the drawing will be included in another, the :sip:ref:`~PyQt6.QtSvg.QSvgGenerator.viewBox` property also needs to be set.

.. literalinclude:: ../../../snippets/qtsvg-tests-manual-examples-svggenerator-window.py

Other meta-data can be specified by setting the *title*, *description* and *resolution* properties.

As with other :sip:ref:`~PyQt6.QtGui.QPaintDevice` subclasses, a :sip:ref:`~PyQt6.QtGui.QPainter` object is used to paint onto an instance of this class:

.. literalinclude:: ../../../snippets/qtsvg-tests-manual-examples-svggenerator-window.py

.. literalinclude:: ../../../snippets/qtsvg-tests-manual-examples-svggenerator-window.py

Painting is performed in the same way as for any other paint device. However, it is necessary to use the :sip:ref:`~PyQt6.QtGui.QPainter.begin` and :sip:ref:`~PyQt6.QtGui.QPainter.end` to explicitly begin and end painting on the device.

.. seealso:: :sip:ref:`~PyQt6.QtSvg.QSvgRenderer`, :sip:ref:`~PyQt6.QtSvgWidgets.QSvgWidget`, :sip:ref:`~PyQt6.Qt SVG C++ Classes`.
