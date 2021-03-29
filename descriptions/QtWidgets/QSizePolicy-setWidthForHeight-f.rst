.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 37e5b48f53e27a3854be225b31da261b

Sets the flag determining whether the widget's width depends on its height, to *dependent*.

This is only supported for `QGraphicsLayout <https://doc.qt.io/qt-6/graphicsview.html#qgraphicslayout>`_'s subclasses. It is not possible to have a layout with both height-for-width and width-for-height constraints at the same time.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.hasWidthForHeight`, :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.setHeightForWidth`.
