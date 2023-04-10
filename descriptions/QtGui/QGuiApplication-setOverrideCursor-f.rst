.. sip:method-description::
    :status: todo
    :pysig: fbf8e5c29e1757a3ecfc032c2ea4a1af
    :realsig: (const QCursor&)
    :digest: c2b76035d56479ead9849f825bc00ada

Sets the application override cursor to *cursor*.

Application override cursors are intended for showing the user that the application is in a special state, for example during an operation that might take some time.

This cursor will be displayed in all the application's widgets until :sip:ref:`~PyQt6.QtGui.QGuiApplication.restoreOverrideCursor` or another setOverrideCursor() is called.

Application cursors are stored on an internal stack. setOverrideCursor() pushes the cursor onto the stack, and :sip:ref:`~PyQt6.QtGui.QGuiApplication.restoreOverrideCursor` pops the active cursor off the stack. changeOverrideCursor() changes the currently active application override cursor.

Every setOverrideCursor() must eventually be followed by a corresponding :sip:ref:`~PyQt6.QtGui.QGuiApplication.restoreOverrideCursor`, otherwise the stack will never be emptied.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_kernel_qguiapplication_x11.py
    :lines: 62-64

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication.overrideCursor`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.restoreOverrideCursor`, :sip:ref:`~PyQt6.QtWidgets.QWidget.setCursor`.
