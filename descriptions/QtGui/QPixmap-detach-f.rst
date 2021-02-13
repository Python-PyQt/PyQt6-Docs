.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 0d334beed754e4f8acee73bac7ab7a8d

Detaches the pixmap from shared pixmap data.

A pixmap is automatically detached by Qt whenever its contents are about to change. This is done in almost all :sip:ref:`~PyQt6.QtGui.QPixmap` member functions that modify the pixmap (\ :sip:ref:`~PyQt6.QtGui.QPixmap.fill`, :sip:ref:`~PyQt6.QtGui.QPixmap.fromImage`, :sip:ref:`~PyQt6.QtGui.QPixmap.load`, etc.), and in :sip:ref:`~PyQt6.QtGui.QPainter.begin` on a pixmap.

There are two exceptions in which  must be called explicitly, that is when calling the  or the x11PictureHandle() function (only available on X11). Otherwise, any modifications done using system calls, will be performed on the shared data.

The  function returns immediately if there is just a single reference or if the pixmap has not been initialized yet.
