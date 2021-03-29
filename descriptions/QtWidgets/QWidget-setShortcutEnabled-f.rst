.. sip:method-description::
    :status: todo
    :pysig: 57f99c5c422bda7ca5d50ce4272ef5ef
    :realsig: (int,bool)
    :digest: d19e3bcc244606dc5d13ed602d580fe8

If *enable* is true, the shortcut with the given *id* is enabled; otherwise the shortcut is disabled.

**Warning:** You should not normally need to use this function since Qt's shortcut system enables/disables shortcuts automatically as widgets become hidden/visible and gain or lose focus. It is best to use :sip:ref:`~PyQt6.QtGui.QAction` or :sip:ref:`~PyQt6.QtGui.QShortcut` to handle shortcuts, since they are easier to use than this low-level function.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.grabShortcut`, :sip:ref:`~PyQt6.QtWidgets.QWidget.releaseShortcut`.
