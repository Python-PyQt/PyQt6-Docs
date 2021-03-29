.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: ae1121144f78abf60aaf68c57921f07e

This virtual function is called twice for all items by the :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.advance` slot. In the first phase, all items are called with *phase* == 0, indicating that items on the scene are about to advance, and then all items are called with *phase* == 1. Reimplement this function to update your item if you need simple scene-controlled animation.

The default implementation does nothing.

This function is intended for animations. An alternative is to multiple-inherit from :sip:ref:`~PyQt6.QtCore.QObject` and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` and use the `Animation Framework <https://doc.qt.io/qt-6/animation-overview.html>`_.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.advance`, :sip:ref:`~PyQt6.QtCore.QTimeLine`.
