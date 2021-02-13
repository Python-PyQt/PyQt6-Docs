.. sip:method-description::
    :status: todo
    :pysig: c5d6e3115e754b395283dc1c09f54493
    :realsig: (const QSizeF&)
    :digest: c185a50458b380a57128e8dadcc2d7bd

Sets the maximum size to *size*. This property overrides :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.sizeHint` for :sip:ref:`~PyQt6.QtCore.Qt.SizeHint.MaximumSize` and ensures that :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.effectiveSizeHint` will never return a size larger than *size*. In order to unset the maximum size, use an invalid size.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.maximumSize`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.minimumSize`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.preferredSize`, :sip:ref:`~PyQt6.QtCore.Qt.SizeHint.MaximumSize`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.sizeHint`.
