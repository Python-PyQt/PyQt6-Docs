.. sip:method-description::
    :status: todo
    :pysig: f89ac3535955a736f6c75593df2080f3
    :realsig: (Qt::WindowStates)
    :digest: 019926d78f877cf7b5ac90ce122132ed

Sets the window state to *windowState*. The window state is a OR'ed combination of :sip:ref:`~PyQt6.QtCore.Qt.WindowState`: :sip:ref:`~PyQt6.QtCore.Qt.WindowState.WindowMinimized`, :sip:ref:`~PyQt6.QtCore.Qt.WindowState.WindowMaximized`, :sip:ref:`~PyQt6.QtCore.Qt.WindowState.WindowFullScreen`, and :sip:ref:`~PyQt6.QtCore.Qt.WindowState.WindowActive`.

If the window is not visible (i.e. :sip:ref:`~PyQt6.QtWidgets.QWidget.isVisible` returns ``false``), the window state will take effect when :sip:ref:`~PyQt6.QtWidgets.QWidget.show` is called. For visible windows, the change is immediate. For example, to toggle between full-screen and normal mode, use the following code:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_kernel_qwidget.py
    :lines: 54-54

To restore and activate a minimized window (while preserving its maximized and/or full-screen state), use the following:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_kernel_qwidget.py
    :lines: 59-59

Calling this function will hide the widget. You must call :sip:ref:`~PyQt6.QtWidgets.QWidget.show` to make the widget visible again.

**Note:** On some window systems :sip:ref:`~PyQt6.QtCore.Qt.WindowState.WindowActive` is not immediate, and may be ignored in certain cases.

When the window state changes, the widget receives a :sip:ref:`~PyQt6.QtWidgets.QWidget.changeEvent` of type :sip:ref:`~PyQt6.QtCore.QEvent.Type.WindowStateChange`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.Qt.WindowState`, :sip:ref:`~PyQt6.QtWidgets.QWidget.windowState`.
