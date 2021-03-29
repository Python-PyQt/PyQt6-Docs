.. sip:method-description::
    :status: todo
    :pysig: 78c2ee29b9f6bed2b9f05a748c095133
    :realsig: (QEvent*)
    :digest: b0828bd5b10d853011935c51c92e2e48

This event handler, for *event*, receives events for the window frame if this widget is a window. Its base implementation provides support for default window frame interaction such as moving, resizing, etc.

You can reimplement this handler in a subclass of `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_ to provide your own custom window frame interaction support.

Returns ``true`` if *event* has been recognized and processed; otherwise, returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.event`.
