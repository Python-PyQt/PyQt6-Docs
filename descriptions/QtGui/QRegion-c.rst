.. sip:class-description::
    :status: todo
    :brief: Specifies a clip region for a painter
    :digest: 98935fa472986a498626c1a7e06517c8

The :sip:ref:`~PyQt6.QtGui.QRegion` class specifies a clip region for a painter.

:sip:ref:`~PyQt6.QtGui.QRegion` is used with :sip:ref:`~PyQt6.QtGui.QPainter.setClipRegion` to limit the paint area to what needs to be painted. There is also a QWidget::repaint() function that takes a :sip:ref:`~PyQt6.QtGui.QRegion` parameter. :sip:ref:`~PyQt6.QtGui.QRegion` is the best tool for minimizing the amount of screen area to be updated by a repaint.

This class is not suitable for constructing shapes for rendering, especially as outlines. Use :sip:ref:`~PyQt6.QtGui.QPainterPath` to create paths and shapes for use with :sip:ref:`~PyQt6.QtGui.QPainter`.

:sip:ref:`~PyQt6.QtGui.QRegion` is an `implicitly shared <https://doc.qt.io/qt-6/implicit-sharing.html>`_ class.

.. _qregion-creating-and-using-regions:

Creating and Using Regions
--------------------------

A region can be created from a rectangle, an ellipse, a polygon or a bitmap. Complex regions may be created by combining simple regions using :sip:ref:`~PyQt6.QtGui.QRegion.united`, :sip:ref:`~PyQt6.QtGui.QRegion.intersected`, :sip:ref:`~PyQt6.QtGui.QRegion.subtracted`, or :sip:ref:`~PyQt6.QtGui.QRegion.xored` (exclusive or). You can move a region using :sip:ref:`~PyQt6.QtGui.QRegion.translate`.

You can test whether a region :sip:ref:`~PyQt6.QtGui.QRegion.isEmpty` or if it :sip:ref:`~PyQt6.QtGui.QRegion.contains` a :sip:ref:`~PyQt6.QtCore.QPoint` or :sip:ref:`~PyQt6.QtCore.QRect`. The bounding rectangle can be found with :sip:ref:`~PyQt6.QtGui.QRegion.boundingRect`.

Iteration over the region (with begin(), end(), or C++11 ranged-for loops) gives a decomposition of the region into rectangles.

Example of using complex regions:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qregion.py
    :lines: 62-72

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.setClipRegion`, :sip:ref:`~PyQt6.QtGui.QPainter.setClipRect`, :sip:ref:`~PyQt6.QtGui.QPainterPath`.
