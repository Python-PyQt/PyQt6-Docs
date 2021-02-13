.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 647b6a2a1c33669d555bd13f96f86820

Removes the shortcut with the given *id* from Qt's shortcut system. The widget will no longer receive :sip:ref:`~PyQt6.QtCore.QEvent.Type.Shortcut` events for the shortcut's key sequence (unless it has other shortcuts with the same key sequence).

**Warning:** You should not normally need to use this function since Qt's shortcut system removes shortcuts automatically when their parent widget is destroyed. It is best to use :sip:ref:`~PyQt6.QtGui.QAction` or :sip:ref:`~PyQt6.QtGui.QShortcut` to handle shortcuts, since they are easier to use than this low-level function. Note also that this is an expensive operation.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.grabShortcut`, :sip:ref:`~PyQt6.QtWidgets.QWidget.setShortcutEnabled`.
