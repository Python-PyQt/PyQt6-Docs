.. sip:method-description::
    :status: todo
    :pysig: de69e2b274e3113bf790023a1c86d9cd
    :realsig: (QWidget*,Qt::MouseButton,Qt::KeyboardModifiers,QPoint,int)
    :digest: 995216b8fe714e3247e5ee152e60cb06

Simulates double clicking a mouse *button* with an optional *modifier* on a *widget*. The position of the click is defined by *pos*; the default position is the center of the widget. If *delay* is specified, the test will wait for the specified amount of milliseconds before each press and release.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.mouseClick`.
