.. sip:method-description::
    :status: todo
    :pysig: 50cad8623622f8634e05e32fc5f89c03
    :realsig: (const QPointF&)
    :digest: a00fa18f5fa81cf3ea7267cc88dbd697

Sets the brush origin to *position*.

The brush origin specifies the (0, 0) coordinate of the painter's brush.

Note that while the :sip:ref:`~PyQt6.QtGui.QPainter.brushOrigin` was necessary to adopt the parent's background for a widget in Qt 3, this is no longer the case since the Qt 4 painter doesn't paint the background unless you explicitly tell it to do so by setting the widget's autoFillBackground property to true.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.brushOrigin`, Settings.
