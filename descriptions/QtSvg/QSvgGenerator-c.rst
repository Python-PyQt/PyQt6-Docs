.. sip:class-description::
    :status: todo
    :brief: Paint device that is used to create SVG drawings
    :digest: 569534b4ecfd4a28478e51b210e7fe14

The :sip:ref:`~PyQt6.QtSvg.QSvgGenerator` class provides a paint device that is used to create SVG drawings.

This paint device represents a Scalable Vector Graphics (SVG) drawing. Like :sip:ref:`~PyQt6.QtPrintSupport.QPrinter`, it is designed as a write-only device that generates output in a specific format.

To write an SVG file, you first need to configure the output by setting the :sip:ref:`~PyQt6.QtSvg.QSvgGenerator.fileName` or :sip:ref:`~PyQt6.QtSvg.QSvgGenerator.outputDevice` properties. It is usually necessary to specify the size of the drawing by setting the :sip:ref:`~PyQt6.QtSvg.QSvgGenerator.size` property, and in some cases where the drawing will be included in another, the :sip:ref:`~PyQt6.QtSvg.QSvgGenerator.viewBox` property also needs to be set.

::

    QSvgGenerator generator;
    generator.setFileName(path);
    generator.setSize(QSize(200, 200));
    generator.setViewBox(QRect(0, 0, 200, 200));
    generator.setTitle(tr("SVG Generator Drawing"));
    generator.setDescription(tr("An SVG drawing created by the SVG Generator"));

Other meta-data can be specified by setting the *title*, *description* and *resolution* properties.

As with other :sip:ref:`~PyQt6.QtGui.QPaintDevice` subclasses, a :sip:ref:`~PyQt6.QtGui.QPainter` object is used to paint onto an instance of this class:

::

    QPainter painter;
    painter.begin(&generator);
    ...
    painter.end();

Painting is performed in the same way as for any other paint device. However, it is necessary to use the :sip:ref:`~PyQt6.QtGui.QPainter.begin` and :sip:ref:`~PyQt6.QtGui.QPainter.end` to explicitly begin and end painting on the device.

.. seealso:: :sip:ref:`~PyQt6.QtSvg.QSvgRenderer`, :sip:ref:`~PyQt6.QtSvgWidgets.QSvgWidget`, :sip:ref:`~PyQt6.Qt SVG C++ Classes`.
