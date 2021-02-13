.. sip:method-description::
    :status: todo
    :pysig: 50cad8623622f8634e05e32fc5f89c03
    :realsig: (const QPointF&)
    :digest: 839b56761d2bfea06fa1ae9c355a10af

Sets the brush origin to *position*.

The brush origin specifies the (0, 0) coordinate of the painter's brush.

Note that while the :sip:ref:`~PyQt6.QtGui.QPainter.brushOrigin` was necessary to adopt the parent's background for a widget in Qt 3, this is no longer the case since the Qt 4 painter doesn't paint the background unless you explicitly tell it to do so by setting the widget's :sip:ref:`~PyQt6.QtWidgets.QWidget.autoFillBackground` property to true.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.brushOrigin`, Settings.
