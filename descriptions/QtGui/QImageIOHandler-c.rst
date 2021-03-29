.. sip:class-description::
    :status: todo
    :brief: Defines the common image I/O interface for all image formats in Qt
    :digest: 299b9153c8549d36cf0c98f768b61590

The :sip:ref:`~PyQt6.QtGui.QImageIOHandler` class defines the common image I/O interface for all image formats in Qt.

Qt uses :sip:ref:`~PyQt6.QtGui.QImageIOHandler` for reading and writing images through :sip:ref:`~PyQt6.QtGui.QImageReader` and :sip:ref:`~PyQt6.QtGui.QImageWriter`. You can also derive from this class to write your own image format handler using Qt's plugin mechanism.

Call :sip:ref:`~PyQt6.QtGui.QImageIOHandler.setDevice` to assign a device to the handler, and :sip:ref:`~PyQt6.QtGui.QImageIOHandler.setFormat` to assign a format to it. One :sip:ref:`~PyQt6.QtGui.QImageIOHandler` may support more than one image format. :sip:ref:`~PyQt6.QtGui.QImageIOHandler.canRead` returns ``true`` if an image can be read from the device, and :sip:ref:`~PyQt6.QtGui.QImageIOHandler.read` and :sip:ref:`~PyQt6.QtGui.QImageIOHandler.write` return true if reading or writing an image was completed successfully.

:sip:ref:`~PyQt6.QtGui.QImageIOHandler` also has support for animations formats, through the functions :sip:ref:`~PyQt6.QtGui.QImageIOHandler.loopCount`, :sip:ref:`~PyQt6.QtGui.QImageIOHandler.imageCount`, :sip:ref:`~PyQt6.QtGui.QImageIOHandler.nextImageDelay` and :sip:ref:`~PyQt6.QtGui.QImageIOHandler.currentImageNumber`.

In order to determine what options an image handler supports, Qt will call :sip:ref:`~PyQt6.QtGui.QImageIOHandler.supportsOption` and :sip:ref:`~PyQt6.QtGui.QImageIOHandler.setOption`. Make sure to reimplement these functions if you can provide support for any of the options in the :sip:ref:`~PyQt6.QtGui.QImageIOHandler.ImageOption.ImageOption` enum.

To write your own image handler, you must at least reimplement :sip:ref:`~PyQt6.QtGui.QImageIOHandler.canRead` and :sip:ref:`~PyQt6.QtGui.QImageIOHandler.read`. Then create a QImageIOPlugin that can create the handler. Finally, install your plugin, and :sip:ref:`~PyQt6.QtGui.QImageReader` and :sip:ref:`~PyQt6.QtGui.QImageWriter` will then automatically load the plugin, and start using it.

.. seealso:: QImageIOPlugin, :sip:ref:`~PyQt6.QtGui.QImageReader`, :sip:ref:`~PyQt6.QtGui.QImageWriter`.
