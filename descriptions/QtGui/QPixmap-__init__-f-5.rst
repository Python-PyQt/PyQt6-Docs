.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int,int)
    :digest: 1df4cb486fee479b1d38fc42e3747330

Constructs a pixmap with the given *width* and *height*. If either *width* or *height* is zero, a null pixmap is constructed.

**Warning:** This will create a :sip:ref:`~PyQt6.QtGui.QPixmap` with uninitialized data. Call :sip:ref:`~PyQt6.QtGui.QPixmap.fill` to fill the pixmap with an appropriate color before drawing onto it with :sip:ref:`~PyQt6.QtGui.QPainter`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixmap.isNull`.
