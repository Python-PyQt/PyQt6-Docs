.. sip:method-description::
    :status: todo
    :pysig: 773223d7a97bc727764204f49d6f1d58
    :realsig: (const QRect&)
    :digest: 1bdf499bffc2a60e0ad238c652f2ce3f

Schedules a redraw of the area covered by *rect* in this item. You can call this function whenever your item needs to be redrawn, such as if it changes appearance or size.

This function does not cause an immediate paint; instead it schedules a paint request that is processed by the QML Scene Graph when the next frame is rendered. The item will only be redrawn if it is visible.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickPaintedItem.paint`.
