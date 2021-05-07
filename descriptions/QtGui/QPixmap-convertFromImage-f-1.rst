.. sip:method-description::
    :status: todo
    :pysig: c453a7144df52d234bc30136ad695844
    :realsig: (const QImage&,Qt::ImageConversionFlags)
    :digest: 065b811ec0f6fd4405bf9faa4412bf35

Replaces this pixmap's data with the given *image* using the specified *flags* to control the conversion. The *flags* argument is a bitwise-OR of the Qt::ImageConversionFlags. Passing 0 for *flags* sets all the default options. Returns ``true`` if the result is that this pixmap is not null.

Note: this function was part of Qt 3 support in Qt 4.6 and earlier. It has been promoted to official API status in 4.7 to support updating the pixmap's image without creating a new :sip:ref:`~PyQt6.QtGui.QPixmap` as :sip:ref:`~PyQt6.QtGui.QPixmap.fromImage` would.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixmap.fromImage`.
