.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: e79ce8705a4b8692012579f04b505aaa

This slot *advances* the scene by one step, by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.advance` for all items on the scene. This is done in two phases: in the first phase, all items are notified that the scene is about to change, and in the second phase all items are notified that they can move. In the first phase, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.advance` is called passing a value of 0 as an argument, and 1 is passed in the second phase.

Note that you can also use the `Animation Framework <https://doc.qt.io/qt-6/animation-overview.html>`_ for animations.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.advance`, :sip:ref:`~PyQt6.QtCore.QTimeLine`.
