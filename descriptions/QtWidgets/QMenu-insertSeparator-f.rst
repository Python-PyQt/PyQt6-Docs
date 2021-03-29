.. sip:method-description::
    :status: todo
    :pysig: 48e0b7b7211368d7fe37ab6bd3de75d6
    :realsig: (QAction*)
    :digest: b502dd0e21643f5c150222fdccc4a818

This convenience function creates a new separator action, i.e. an action with :sip:ref:`~PyQt6.QtGui.QAction.isSeparator` returning true. The function inserts the newly created action into this menu's list of actions before action *before* and returns it.

:sip:ref:`~PyQt6.QtWidgets.QMenu` takes ownership of the returned :sip:ref:`~PyQt6.QtGui.QAction`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.insertAction`, :sip:ref:`~PyQt6.QtWidgets.QMenu.addSeparator`.
