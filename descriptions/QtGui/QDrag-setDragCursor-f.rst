.. sip:method-description::
    :status: todo
    :pysig: d96b2982cce8a99482f76b2634be044d
    :realsig: (const QPixmap&,Qt::DropAction)
    :digest: 8c54df4729cc122dc87df21275fb3b23

Sets the drag *cursor* for the *action*. This allows you to override the default native cursors. To revert to using the native cursor for *action* pass in a null :sip:ref:`~PyQt6.QtGui.QPixmap` as *cursor*.

Note: setting the drag cursor for IgnoreAction may not work on all platforms. X11 and macOS has been tested to work. Windows does not support it.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QDrag.dragCursor`.
