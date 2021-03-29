.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: (qreal)
    :digest: 158f50aea205c55a3bffa950625f4de4

Sets the bounding region granularity to *granularity*; a value between and including 0 and 1. The default value is 0 (i.e., the lowest granularity, where the bounding region corresponds to the item's bounding rectangle).

The granularity is used by :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.boundingRegion` to calculate how fine the bounding region of the item should be. The highest achievable granularity is 1, where :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.boundingRegion` will return the finest outline possible for the respective device (e.g., for a :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` viewport, this gives you a pixel-perfect bounding region). The lowest possible granularity is 0. The value of *granularity* describes the ratio between device resolution and the resolution of the bounding region (e.g., a value of 0.25 will provide a region where each chunk corresponds to 4x4 device units / pixels).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.boundingRegionGranularity`.
