.. sip:method-description::
    :status: todo
    :pysig: c5d6e3115e754b395283dc1c09f54493
    :realsig: (const QSizeF&)
    :digest: 55400203da52172bb0993834743940bd

Sets the minimum size to *size*. This property overrides :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.sizeHint` for :sip:ref:`~PyQt6.QtCore.Qt.SizeHint.MinimumSize` and ensures that :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.effectiveSizeHint` will never return a size smaller than *size*. In order to unset the minimum size, use an invalid size.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.minimumSize`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.maximumSize`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.preferredSize`, :sip:ref:`~PyQt6.QtCore.Qt.SizeHint.MinimumSize`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.sizeHint`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.setMinimumWidth`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.setMinimumHeight`.
