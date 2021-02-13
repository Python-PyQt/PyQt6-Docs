.. sip:class-description::
    :status: todo
    :brief: List of points using integer precision
    :digest: 3a8d1708626a64ccfd161e69e4181580

The :sip:ref:`~PyQt6.QtGui.QPolygon` class provides a list of points using integer precision.

A :sip:ref:`~PyQt6.QtGui.QPolygon` object is a QList<\ :sip:ref:`~PyQt6.QtCore.QPoint`>. The easiest way to add points to a :sip:ref:`~PyQt6.QtGui.QPolygon` is to use QList's streaming operator, as illustrated below:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-polygon-polygon.py
    :lines: 59-60

In addition to the functions provided by QList, :sip:ref:`~PyQt6.QtGui.QPolygon` provides some point-specific functions.

Each point in a polygon can be retrieved by passing its index to the :sip:ref:`~PyQt6.QtGui.QPolygon.point` function. To populate the polygon, :sip:ref:`~PyQt6.QtGui.QPolygon` provides the :sip:ref:`~PyQt6.QtGui.QPolygon.setPoint` function to set the point at a given index, the :sip:ref:`~PyQt6.QtGui.QPolygon.setPoints` function to set all the points in the polygon (resizing it to the given number of points), and the :sip:ref:`~PyQt6.QtGui.QPolygon.putPoints` function which copies a number of given points into the polygon from a specified index (resizing the polygon if necessary).

:sip:ref:`~PyQt6.QtGui.QPolygon` provides the :sip:ref:`~PyQt6.QtGui.QPolygon.boundingRect` and :sip:ref:`~PyQt6.QtGui.QPolygon.translate` functions for geometry functions. Use the :sip:ref:`~PyQt6.QtGui.QTransform.map` function for more general transformations of QPolygons.

The :sip:ref:`~PyQt6.QtGui.QPolygon` class is `implicitly shared <https://doc.qt.io/qt-6/implicit-sharing.html>`_.

.. seealso:: QList, :sip:ref:`~PyQt6.QtGui.QPolygonF`, :sip:ref:`~PyQt6.QtCore.QLine`.
