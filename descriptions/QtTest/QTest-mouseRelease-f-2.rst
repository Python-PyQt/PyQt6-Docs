.. sip:method-description::
    :status: todo
    :pysig: de69e2b274e3113bf790023a1c86d9cd
    :realsig: (QWidget*,Qt::MouseButton,Qt::KeyboardModifiers,QPoint,int)
    :digest: 1b20bf6f2be16476a5a84231e14df85a

Simulates releasing a mouse *button* with an optional *modifier* on a *widget*. The position of the release is defined by *pos*; the default position is the center of the widget. If *delay* is specified, the test will wait for the specified amount of milliseconds before releasing the button.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.mousePress`, :sip:ref:`~PyQt6.QtTest.QTest.mouseClick`.
