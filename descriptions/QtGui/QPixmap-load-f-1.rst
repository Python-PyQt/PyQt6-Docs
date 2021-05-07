.. sip:method-description::
    :status: todo
    :pysig: 5117857841e31ffb349a4a44b36efc27
    :realsig: (const QString&,const char*,Qt::ImageConversionFlags)
    :digest: 077536c1d52b3e8e00ec4224b2d4ea7b

Loads a pixmap from the file with the given *fileName*. Returns true if the pixmap was successfully loaded; otherwise invalidates the pixmap and returns ``false``.

The loader attempts to read the pixmap using the specified *format*. If the *format* is not specified (which is the default), the loader probes the file for a header to guess the file format.

The file name can either refer to an actual file on disk or to one of the application's embedded resources. See the `Resource System <https://doc.qt.io/qt-6/resources.html>`_ overview for details on how to embed pixmaps and other resource files in the application's executable.

If the data needs to be modified to fit in a lower-resolution result (e.g. converting from 32-bit to 8-bit), use the *flags* to control the conversion.

Note that QPixmaps are automatically added to the :sip:ref:`~PyQt6.QtGui.QPixmapCache` when loaded from a file in main thread; the key used is internal and cannot be acquired.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixmap.loadFromData`, Reading and Writing Image Files.
