.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 2691e033c1e9c50bbff4068c29aeab85

Sets the shortcut's "What's This?" help *text*.

The text will be shown when a widget application is in "What's This?" mode and the user types the shortcut :sip:ref:`~PyQt6.QtGui.QShortcut.key` sequence.

To set "What's This?" help on a menu item (with or without a shortcut key), set the help on the item's action.

By default, the help text is an empty string.

This function has no effect in applications that don't use widgets.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QShortcut.whatsThis`, :sip:ref:`~PyQt6.QtWidgets.QWhatsThis.inWhatsThisMode`, :sip:ref:`~PyQt6.QtGui.QAction.setWhatsThis`.
