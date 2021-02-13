.. sip:class-description::
    :status: todo
    :brief: List of points using floating point precision
    :digest: 8b962e21342c71a136fc541282e987ff

The :sip:ref:`~PyQt6.QtGui.QPolygonF` class provides a list of points using floating point precision.

A :sip:ref:`~PyQt6.QtGui.QPolygonF` is a QList<\ :sip:ref:`~PyQt6.QtCore.QPointF`>. The easiest way to add points to a :sip:ref:`~PyQt6.QtGui.QPolygonF` is to use its streaming operator, as illustrated below:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-polygon-polygon.py
    :lines: 67-68

In addition to the functions provided by QList, :sip:ref:`~PyQt6.QtGui.QPolygonF` provides the :sip:ref:`~PyQt6.QtGui.QPolygonF.boundingRect` and :sip:ref:`~PyQt6.QtGui.QPolygonF.translate` functions for geometry operations. Use the :sip:ref:`~PyQt6.QtGui.QTransform.map` function for more general transformations of QPolygonFs.

:sip:ref:`~PyQt6.QtGui.QPolygonF` also provides the :sip:ref:`~PyQt6.QtGui.QPolygonF.isClosed` function to determine whether a polygon's start and end points are the same, and the :sip:ref:`~PyQt6.QtGui.QPolygonF.toPolygon` function returning an integer precision copy of this polygon.

The :sip:ref:`~PyQt6.QtGui.QPolygonF` class is `implicitly shared <https://doc.qt.io/qt-6/implicit-sharing.html>`_.

.. seealso:: QList, :sip:ref:`~PyQt6.QtGui.QPolygon`, :sip:ref:`~PyQt6.QtCore.QLineF`.
