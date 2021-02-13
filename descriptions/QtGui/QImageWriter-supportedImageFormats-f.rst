.. sip:method-description::
    :status: todo
    :pysig: a9de941641bfc9e1529fe64f342cdb3e
    :realsig: ()
    :digest: 1fa83f41cc6203051fad038f6a9e7508

Returns the list of image formats supported by :sip:ref:`~PyQt6.QtGui.QImageWriter`.

By default, Qt can write the following formats:

+--------+--------------------------+----------------------------------+
| Format | MIME type                | Description                      |
+========+==========================+==================================+
| BMP    | image/bmp                | Windows Bitmap                   |
+--------+--------------------------+----------------------------------+
| JPG    | image/jpeg               | Joint Photographic Experts Group |
+--------+--------------------------+----------------------------------+
| PNG    | image/png                | Portable Network Graphics        |
+--------+--------------------------+----------------------------------+
| PBM    | image/x-portable-bitmap  | Portable Bitmap                  |
+--------+--------------------------+----------------------------------+
| PGM    | image/x-portable-graymap | Portable Graymap                 |
+--------+--------------------------+----------------------------------+
| PPM    | image/x-portable-pixmap  | Portable Pixmap                  |
+--------+--------------------------+----------------------------------+
| XBM    | image/x-xbitmap          | X11 Bitmap                       |
+--------+--------------------------+----------------------------------+
| XPM    | image/x-xpixmap          | X11 Pixmap                       |
+--------+--------------------------+----------------------------------+

Reading and writing SVG files is supported through the Qt SVG module. The Qt Image Formats module provides support for additional image formats.

Note that the :sip:ref:`~PyQt6.QtWidgets.QApplication` instance must be created before this function is called.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageWriter.setFormat`, :sip:ref:`~PyQt6.QtGui.QImageReader.supportedImageFormats`, QImageIOPlugin.
