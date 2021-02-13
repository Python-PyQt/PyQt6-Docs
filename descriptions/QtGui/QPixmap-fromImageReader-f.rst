.. sip:method-description::
    :status: todo
    :pysig: 54a07912058a58a02909f4551eae9a95
    :realsig: (QImageReader*,Qt::ImageConversionFlags)
    :digest: 1d60b1769e172276c20601c8e9ec7786

Create a :sip:ref:`~PyQt6.QtGui.QPixmap` from an image read directly from an *imageReader*. The *flags* argument is a bitwise-OR of the Qt::ImageConversionFlags. Passing 0 for *flags* sets all the default options.

On some systems, reading an image directly to :sip:ref:`~PyQt6.QtGui.QPixmap` can use less memory than reading a :sip:ref:`~PyQt6.QtGui.QImage` to convert it to :sip:ref:`~PyQt6.QtGui.QPixmap`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixmap.fromImage`, :sip:ref:`~PyQt6.QtGui.QPixmap.toImage`, Pixmap Conversion.
