.. sip:method-description::
    :status: todo
    :pysig: f7dba2c0411c0ef6af4394e6fc1d3906
    :realsig: (const QBitmap&)
    :digest: bc52b9d177d9133bb74bf5ab829b0c4a

Sets a mask bitmap.

This function merges the *mask* with the pixmap's alpha channel. A pixel value of 1 on the mask means the pixmap's pixel is unchanged; a value of 0 means the pixel is transparent. The mask must have the same size as this pixmap.

Setting a null mask resets the mask, leaving the previously transparent pixels black. The effect of this function is undefined when the pixmap is being painted on.

**Warning:** This is potentially an expensive operation.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixmap.mask`, Pixmap Transformations, `QBitmap <https://doc.qt.io/qt-6/gui-changes-qt6.html#qbitmap>`_.
