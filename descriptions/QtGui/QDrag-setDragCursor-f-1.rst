.. sip:method-description::
    :status: todo
    :pysig: 9316464be7e2fb9c8d19e0ff6c3b8d95
    :realsig: (const QPixmap&,Qt::DropAction)
    :digest: 8c54df4729cc122dc87df21275fb3b23

Sets the drag *cursor* for the *action*. This allows you to override the default native cursors. To revert to using the native cursor for *action* pass in a null :sip:ref:`~PyQt6.QtGui.QPixmap` as *cursor*.

Note: setting the drag cursor for IgnoreAction may not work on all platforms. X11 and macOS has been tested to work. Windows does not support it.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QDrag.dragCursor`.
