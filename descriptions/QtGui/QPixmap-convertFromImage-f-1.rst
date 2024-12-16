.. sip:method-description::
    :status: todo
    :pysig: c453a7144df52d234bc30136ad695844
    :realsig: (const QImage&,Qt::ImageConversionFlags)
    :digest: fbda86d1c9483d4cd5f0995e6ef90ffd

Replaces this pixmap's data with the given *image* using the specified *flags* to control the conversion. The *flags* argument is a bitwise-OR of the Qt::ImageConversionFlags. Passing 0 for *flags* sets all the default options. Returns ``true`` if the result is that this pixmap is not null.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixmap.fromImage`.
