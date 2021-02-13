.. sip:method-description::
    :status: todo
    :pysig: 7cce74340329521a145f04963f5c9bd7
    :realsig: (QStyle*)
    :digest: 567d20bcd626244e2120d634c38b0c24

Sets or replaces the style of the scene to *style*, and reparents the style to this scene. Any previously assigned style is deleted. The scene's style defaults to :sip:ref:`~PyQt6.QtWidgets.QApplication.style`, and serves as the default for all `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_ items in the scene.

Changing the style, either directly by calling this function, or indirectly by calling :sip:ref:`~PyQt6.QtWidgets.QApplication.setStyle`, will automatically update the style for all widgets in the scene that do not have a style explicitly assigned to them.

If *style* is ``nullptr``, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` will revert to :sip:ref:`~PyQt6.QtWidgets.QApplication.style`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.style`.
