.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: c0f50bcc24e4da5009217044c0750a7c

Resets any cached content. Calling this function will clear :sip:ref:`~PyQt6.QtWidgets.QGraphicsView`'s cache. If the current cache mode is :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.CacheMode.CacheNone`, this function does nothing.

This function is called automatically for you when the :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.backgroundBrush` or :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.backgroundBrush` properties change; you only need to call this function if you have reimplemented :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.drawBackground` or :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.drawBackground` to draw a custom background, and need to trigger a full redraw.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.cacheMode`.
