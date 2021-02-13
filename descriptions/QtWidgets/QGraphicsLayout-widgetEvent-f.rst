.. sip:method-description::
    :status: todo
    :pysig: e7d4b6e3f87ba9fe2928216c4f159b5b
    :realsig: (QEvent*)
    :digest: 990741192783b1eea9b42af6edb8c130

This virtual event handler receives all events for the managed widget. `QGraphicsLayout <https://doc.qt.io/qt-6/graphicsview.html#qgraphicslayout>`_ uses this event handler to listen for layout related events such as geometry changes, layout changes or layout direction changes.

*e* is a pointer to the event.

You can reimplement this event handler to track similar events for your own custom layout.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.event`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.sceneEvent`.
