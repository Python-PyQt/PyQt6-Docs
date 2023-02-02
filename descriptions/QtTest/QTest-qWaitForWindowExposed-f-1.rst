.. sip:method-description::
    :status: todo
    :pysig: 720d553c04b75d1e761b2ee2969113a6
    :realsig: (QWidget*,int)
    :digest: 5e405842eb3fbf75dd8527fbf01e02bc

Returns ``true`` if *widget* is exposed within *timeout* milliseconds. Otherwise returns ``false``.

The method is useful in tests that call :sip:ref:`~PyQt6.QtWidgets.QWidget.show` and rely on the widget actually being being visible before proceeding.

**Note:** A window mapped to screen may still not be considered exposed, if the window client area is not visible, e.g. because it is completely covered by other windows. In such cases, the method will time out and return ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.qWaitForWindowActive`, :sip:ref:`~PyQt6.QtWidgets.QWidget.isVisible`, :sip:ref:`~PyQt6.QtGui.QWindow.isExposed`.
