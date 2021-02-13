.. sip:method-description::
    :status: todo
    :pysig: a9de941641bfc9e1529fe64f342cdb3e
    :realsig: ()
    :digest: 2cf1f320c70c399c67fd6821a145e285

Returns the list of image formats supported by :sip:ref:`~PyQt6.QtGui.QImageReader`.

By default, Qt can read the following formats:

+--------+--------------------------+---------------------------------------+
| Format | MIME type                | Description                           |
+========+==========================+=======================================+
| BMP    | image/bmp                | Windows Bitmap                        |
+--------+--------------------------+---------------------------------------+
| GIF    | image/gif                | Graphic Interchange Format (optional) |
+--------+--------------------------+---------------------------------------+
| JPG    | image/jpeg               | Joint Photographic Experts Group      |
+--------+--------------------------+---------------------------------------+
| PNG    | image/png                | Portable Network Graphics             |
+--------+--------------------------+---------------------------------------+
| PBM    | image/x-portable-bitmap  | Portable Bitmap                       |
+--------+--------------------------+---------------------------------------+
| PGM    | image/x-portable-graymap | Portable Graymap                      |
+--------+--------------------------+---------------------------------------+
| PPM    | image/x-portable-pixmap  | Portable Pixmap                       |
+--------+--------------------------+---------------------------------------+
| XBM    | image/x-xbitmap          | X11 Bitmap                            |
+--------+--------------------------+---------------------------------------+
| XPM    | image/x-xpixmap          | X11 Pixmap                            |
+--------+--------------------------+---------------------------------------+
| SVG    | image/svg+xml            | Scalable Vector Graphics              |
+--------+--------------------------+---------------------------------------+

Reading and writing SVG files is supported through the Qt SVG module. The Qt Image Formats module provides support for additional image formats.

Note that the QApplication instance must be created before this function is called.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageReader.setFormat`, :sip:ref:`~PyQt6.QtGui.QImageWriter.supportedImageFormats`, QImageIOPlugin.
