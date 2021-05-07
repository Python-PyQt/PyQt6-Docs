.. sip:method-description::
    :status: todo
    :pysig: de69e2b274e3113bf790023a1c86d9cd
    :realsig: (QWidget*,Qt::MouseButton,Qt::KeyboardModifiers,QPoint,int)
    :digest: 3a537c34428cacc2ec7737e92cdb0c85

Simulates pressing a mouse *button* with an optional *modifier* on a *widget*. The position is defined by *pos*; the default position is the center of the widget. If *delay* is specified, the test will wait for the specified amount of milliseconds before the press.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.mouseRelease`, :sip:ref:`~PyQt6.QtTest.QTest.mouseClick`.
