.. sip:enum-description::
    :status: todo
    :digest: 41b5732bf4cd334257b4123873e94718

This enum describes the state changes that are notified by :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange`. The notifications are sent as the state changes, and in some cases, adjustments can be made (see the documentation for each change for details).

Note: Be careful with calling functions on the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` itself inside :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange`, as certain function calls can lead to unwanted recursion. For example, you cannot call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setPos` in :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange` on an  notification, as the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setPos` function will again call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange`\ (). Instead, you can return the new, adjusted position from :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange`.
