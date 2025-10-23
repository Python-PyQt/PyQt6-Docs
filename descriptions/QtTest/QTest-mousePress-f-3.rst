.. sip:method-description::
    :status: todo
    :pysig: 346e0591a377b8b241d99bc168d233b8
    :realsig: (QWindow*,Qt::MouseButton,Qt::KeyboardModifiers,QPoint,int)
    :digest: 0081d18ce9d993b6db40e6245d0c47b0

Simulates pressing a mouse *button* with an optional *stateKey* modifier on a *window*. The position is defined by *pos*; the default position is the center of the window. If *delay* is specified, the test will wait for the specified amount of milliseconds before the press.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.mouseRelease`, :sip:ref:`~PyQt6.QtTest.QTest.mouseClick`.
