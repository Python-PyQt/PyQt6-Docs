.. sip:class-description::
    :status: todo
    :brief: Events when a tooltip is requested
    :digest: cfeeb55eccf1535fe7a71f54870a8be2

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneHelpEvent` class provides events when a tooltip is requested.

When a :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` receives a :sip:ref:`~PyQt6.QtCore.QEvent` of type :sip:ref:`~PyQt6.QtCore.QEvent.Type.ToolTip`, it creates a :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneHelpEvent`, which is forwarded to the scene. You can set a tooltip on a :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` with :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setToolTip`; by default :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` displays the tooltip of the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` with the highest z-value (i.e, the top-most item) under the mouse position.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsView` does not forward events when :sip:ref:`~PyQt6.QtWidgets.QWhatsThis` and :sip:ref:`~PyQt6.QtGui.QStatusTipEvent` help is requested. If you need this, you can reimplement :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.viewportEvent` and forward :sip:ref:`~PyQt6.QtGui.QStatusTipEvent` events and :sip:ref:`~PyQt6.QtCore.QEvent` of type :sip:ref:`~PyQt6.QtCore.QEvent.Type.WhatsThis` to the scene.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QEvent`.
