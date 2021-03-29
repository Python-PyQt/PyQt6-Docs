.. sip:method-description::
    :status: todo
    :pysig: 94b022f35b9734660a4c95771a8e7784
    :realsig: (const QPixmap&,int,int)
    :digest: bcacc1f30de30b1758af65a63435cef3

Constructs a custom pixmap cursor.

*pixmap* is the image. It is usual to give it a mask (set using :sip:ref:`~PyQt6.QtGui.QPixmap.setMask`). *hotX* and *hotY* define the cursor's hot spot.

If *hotX* is negative, it is set to the ``pixmap().width()/2``. If *hotY* is negative, it is set to the ``pixmap().height()/2``.

Valid cursor sizes depend on the display hardware (or the underlying window system). We recommend using 32 x 32 cursors, because this size is supported on all platforms. Some platforms also support 16 x 16, 48 x 48, and 64 x 64 cursors.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixmap.__init__`, :sip:ref:`~PyQt6.QtGui.QPixmap.setMask`.
