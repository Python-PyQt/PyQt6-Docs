.. sip:method-description::
    :status: todo
    :pysig: 346e0591a377b8b241d99bc168d233b8
    :realsig: (QWindow*,Qt::MouseButton,Qt::KeyboardModifiers,QPoint,int)
    :digest: a0a823154c2c3eab4c45b70c0b802606

Simulates double clicking a mouse *button* with an optional *stateKey* modifier on a *window*. The position of the click is defined by *pos*; the default position is the center of the window. If *delay* is specified, the test will wait for the specified amount of milliseconds before each press and release.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.mouseClick`.
