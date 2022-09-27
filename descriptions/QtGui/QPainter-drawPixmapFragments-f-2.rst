.. sip:method-description::
    :status: todo
    :pysig: f5d7690cafa674cfa427f93ae1dfd739
    :realsig: (const QPainter::PixmapFragment*,int,const QPixmap&,QPainter::PixmapFragmentHints)
    :digest: 6e3c8b4af2302ac2266d9d4e8c796b55

This function is used to draw *pixmap*, or a sub-rectangle of *pixmap*, at multiple positions with different scale, rotation and opacity. *fragments* is an array of *fragmentCount* elements specifying the parameters used to draw each pixmap fragment. The *hints* parameter can be used to pass in drawing hints.

This function is potentially faster than multiple calls to :sip:ref:`~PyQt6.QtGui.QPainter.drawPixmap`, since the backend can optimize state changes.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.PixmapFragment`, :sip:ref:`~PyQt6.QtGui.QPainter.PixmapFragmentHint`.
