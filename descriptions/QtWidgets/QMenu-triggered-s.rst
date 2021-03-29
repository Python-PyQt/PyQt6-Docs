.. sip:signal-description::
    :status: todo
    :pysig: f8ca99b6c748ea427923a2f5f071f05b
    :realsig: (QAction*)
    :digest: 47e9bd6ea91209b48e94c93b2f79a67c

This signal is emitted when an action in this menu is triggered.

*action* is the action that caused the signal to be emitted.

Normally, you connect each menu action's :sip:ref:`~PyQt6.QtGui.QAction.triggered` signal to its own custom slot, but sometimes you will want to connect several actions to a single slot, for example, when you have a group of closely related actions, such as "left justify", "center", "right justify".

**Note:** This signal is emitted for the main parent menu in a hierarchy. Hence, only the parent menu needs to be connected to a slot; sub-menus need not be connected.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMenu.hovered`, :sip:ref:`~PyQt6.QtGui.QAction.triggered`.
