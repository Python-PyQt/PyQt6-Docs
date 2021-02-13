.. sip:method-description::
    :status: todo
    :pysig: fbf8e5c29e1757a3ecfc032c2ea4a1af
    :realsig: (const QCursor&)
    :digest: eb7bc92a4cda1eaab5d9b02d29a20a22

Sets the application override cursor to *cursor*.

Application override cursors are intended for showing the user that the application is in a special state, for example during an operation that might take some time.

This cursor will be displayed in all the application's widgets until :sip:ref:`~PyQt6.QtGui.QGuiApplication.restoreOverrideCursor` or another  is called.

Application cursors are stored on an internal stack.  pushes the cursor onto the stack, and :sip:ref:`~PyQt6.QtGui.QGuiApplication.restoreOverrideCursor` pops the active cursor off the stack. :sip:ref:`~PyQt6.QtGui.QGuiApplication.changeOverrideCursor` changes the curently active application override cursor.

Every  must eventually be followed by a corresponding :sip:ref:`~PyQt6.QtGui.QGuiApplication.restoreOverrideCursor`, otherwise the stack will never be emptied.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_kernel_qguiapplication_x11.py
    :lines: 62-64

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication.overrideCursor`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.restoreOverrideCursor`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.changeOverrideCursor`.
