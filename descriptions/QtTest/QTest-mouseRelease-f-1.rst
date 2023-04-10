.. sip:method-description::
    :status: todo
    :pysig: f65b1d626fe994f478ad21f60ca7eba5
    :realsig: (QWindow*,Qt::MouseButton,Qt::KeyboardModifiers,QPoint,int)
    :digest: 56336fda0c00162043e9097f030585f5

This is an overloaded function.

Simulates releasing a mouse *button* with an optional *stateKey* modifier on a *window*. The position of the release is defined by *pos*; the default position is the center of the window. If *delay* is specified, the test will wait for the specified amount of milliseconds before releasing the button; otherwise, it will wait for a default amount of time (1 ms), which can be overridden via `command-line arguments <https://doc.qt.io/qt-6/qtest-overview.html#testing-options>`_.

**Note:** If you wish to test a double-click by sending events individually, specify a short delay, greater than the default, on both mouse release events. The total of the delays for the press, release, press and release must be less than :sip:ref:`~PyQt6.QtGui.QStyleHints.mouseDoubleClickInterval`. But if you don't need to check state between events, it's better to use :sip:ref:`~PyQt6.QtTest.QTest.mouseDClick`.

.. literalinclude:: ../../../snippets/qtbase-src-testlib-doc-snippets-code-src_qtestlib_qtestcase_snippet.py

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.mousePress`, :sip:ref:`~PyQt6.QtTest.QTest.mouseClick`.
