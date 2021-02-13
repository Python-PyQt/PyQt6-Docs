.. sip:method-description::
    :status: todo
    :pysig: 37b2e3c5a43d9aa3a55105ac473e4713
    :realsig: (const QBitmap&,const QBitmap&,int,int)
    :digest: 768770c6f81191eb0c576a2d2c6ddc49

Constructs a custom bitmap cursor.

*bitmap* and *mask* make up the bitmap. *hotX* and *hotY* define the cursor's hot spot.

If *hotX* is negative, it is set to the ``bitmap().width()/2``. If *hotY* is negative, it is set to the ``bitmap().height()/2``.

The cursor *bitmap* (B) and *mask* (M) bits are combined like this:

* B=1 and M=1 gives black.

* B=0 and M=1 gives white.

* B=0 and M=0 gives transparent.

* B=1 and M=0 gives an XOR'd result under Windows, undefined results on all other platforms.

Use the global Qt color :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.color0` to draw 0-pixels and :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.color1` to draw 1-pixels in the bitmaps.

Valid cursor sizes depend on the display hardware (or the underlying window system). We recommend using 32 x 32 cursors, because this size is supported on all platforms. Some platforms also support 16 x 16, 48 x 48, and 64 x 64 cursors.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QBitmap.__init__`, QBitmap::setMask().
