.. sip:method-description::
    :status: todo
    :pysig: 3dafc730677e90fc185f333fdafb6acb
    :realsig: (WId)
    :digest: 883b25717fbfd52ab3371c37a26dfa6a

Creates a local representation of a window created by another process or by using native libraries below Qt.

Given the handle *id* to a native window, this method creates a :sip:ref:`~PyQt6.QtGui.QWindow` object which can be used to represent the window when invoking methods like :sip:ref:`~PyQt6.QtGui.QWindow.setParent` and :sip:ref:`~PyQt6.QtGui.QWindow.setTransientParent`.

This can be used, on platforms which support it, to embed a :sip:ref:`~PyQt6.QtGui.QWindow` inside a native window, or to embed a native window inside a :sip:ref:`~PyQt6.QtGui.QWindow`.

If foreign windows are not supported or embedding the native window failed in the platform plugin, this function returns ``nullptr``.

**Note:** The resulting :sip:ref:`~PyQt6.QtGui.QWindow` should not be used to manipulate the underlying native window (besides re-parenting), or to observe state changes of the native window. Any support for these kind of operations is incidental, highly platform dependent and untested.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.setParent`.
