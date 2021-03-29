.. sip:method-description::
    :status: todo
    :pysig: b6901042a6dbba0cde68990f5f1642e0
    :realsig: (QWidget*,Qt::MouseButton,Qt::KeyboardModifiers,QPoint,int)
    :digest: 1b20bf6f2be16476a5a84231e14df85a

Simulates releasing a mouse *button* with an optional *modifier* on a *widget*. The position of the release is defined by *pos*; the default position is the center of the widget. If *delay* is specified, the test will wait for the specified amount of milliseconds before releasing the button.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.mousePress`, :sip:ref:`~PyQt6.QtTest.QTest.mouseClick`.
