.. sip:class-description::
    :status: todo
    :brief: Formatting information for images in a QTextDocument
    :digest: 9fd71d302f32a3abbdb37575fa884807

The :sip:ref:`~PyQt6.QtGui.QTextImageFormat` class provides formatting information for images in a :sip:ref:`~PyQt6.QtGui.QTextDocument`.

Inline images are represented by a Unicode value U+FFFC (OBJECT REPLACEMENT CHARACTER) which has an associated :sip:ref:`~PyQt6.QtGui.QTextImageFormat`. The image format specifies a name with :sip:ref:`~PyQt6.QtGui.QTextImageFormat.setName` that is used to locate the image. The size of the rectangle that the image will occupy is specified in pixels using :sip:ref:`~PyQt6.QtGui.QTextImageFormat.setWidth` and :sip:ref:`~PyQt6.QtGui.QTextImageFormat.setHeight`. The desired image quality may be set with :sip:ref:`~PyQt6.QtGui.QTextImageFormat.setQuality`.

Images can be supplied in any format for which Qt has an image reader, so SVG drawings can be included alongside PNG, TIFF and other bitmap formats.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage`, :sip:ref:`~PyQt6.QtGui.QImageReader`.
