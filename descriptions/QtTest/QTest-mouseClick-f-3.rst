.. sip:method-description::
    :status: todo
    :pysig: 346e0591a377b8b241d99bc168d233b8
    :realsig: (QWindow*,Qt::MouseButton,Qt::KeyboardModifiers,QPoint,int)
    :digest: 10c9702ef999f2c5d5b4aa65173e4a52

Simulates clicking a mouse *button* with an optional *stateKey* modifier on a *window*. The position of the click is defined by *pos*; the default position is the center of the window. If *delay* is specified, the test will wait for the specified amount of milliseconds before pressing and before releasing the button.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.mousePress`, :sip:ref:`~PyQt6.QtTest.QTest.mouseRelease`.
