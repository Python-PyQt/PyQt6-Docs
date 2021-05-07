.. sip:method-description::
    :status: todo
    :pysig: de69e2b274e3113bf790023a1c86d9cd
    :realsig: (QWidget*,Qt::MouseButton,Qt::KeyboardModifiers,QPoint,int)
    :digest: 9212d036233bb96a8c1dea8b0b21a269

Simulates clicking a mouse *button* with an optional *modifier* on a *widget*. The position of the click is defined by *pos*; the default position is the center of the widget. If *delay* is specified, the test will wait for the specified amount of milliseconds before pressing and before releasing the button.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.mousePress`, :sip:ref:`~PyQt6.QtTest.QTest.mouseRelease`.
