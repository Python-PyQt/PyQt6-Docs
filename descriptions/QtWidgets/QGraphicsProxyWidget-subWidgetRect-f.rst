.. sip:method-description::
    :status: todo
    :pysig: e7721ea98fac1a56122812ed5a9b470e
    :realsig: (const QWidget*) const
    :digest: 9d6116c5d6489677522d60d2eb3f2c67

Returns the rectangle for *widget*, which must be a descendant of :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget.widget`, or :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget.widget` itself, in this proxy item's local coordinates.

If no widget is embedded, *widget* is ``nullptr``, or *widget* is not a descendant of the embedded widget, this function returns an empty :sip:ref:`~PyQt6.QtCore.QRectF`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget.widget`.
