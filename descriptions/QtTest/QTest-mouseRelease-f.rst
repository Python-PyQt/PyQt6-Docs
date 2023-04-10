.. sip:method-description::
    :status: todo
    :pysig: b6901042a6dbba0cde68990f5f1642e0
    :realsig: (QWidget*,Qt::MouseButton,Qt::KeyboardModifiers,QPoint,int)
    :digest: 492c8b106f2e930649a5c6cc762b60c3

Simulates releasing a mouse *button* with an optional *modifier* on a *widget*. The position of the release is defined by *pos*; the default position is the center of the widget. If *delay* is specified, the test will wait for the specified amount of milliseconds before releasing the button; otherwise, it will wait for a default amount of time (1 ms), which can be overridden via `command-line arguments <https://doc.qt.io/qt-6/qtest-overview.html#testing-options>`_.

**Note:** If you wish to test a double-click by sending events individually, specify a short delay, greater than the default, on both mouse release events. The total of the delays for the press, release, press and release must be less than :sip:ref:`~PyQt6.QtGui.QStyleHints.mouseDoubleClickInterval`. But if you don't need to check state between events, it's better to use :sip:ref:`~PyQt6.QtTest.QTest.mouseDClick`.

.. literalinclude:: ../../../snippets/qtbase-src-testlib-doc-snippets-code-src_qtestlib_qtestcase_snippet.py

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.mousePress`, :sip:ref:`~PyQt6.QtTest.QTest.mouseClick`.
