.. sip:class-description::
    :status: todo
    :brief: Format independent interface for writing images to files or other devices
    :digest: 63010cfeadffc5a141eda6adfbea55b2

The :sip:ref:`~PyQt6.QtGui.QImageWriter` class provides a format independent interface for writing images to files or other devices.

:sip:ref:`~PyQt6.QtGui.QImageWriter` supports setting format specific options, such as compression level and quality, prior to storing the image. If you do not need such options, you can use :sip:ref:`~PyQt6.QtGui.QImage.save` or :sip:ref:`~PyQt6.QtGui.QPixmap.save` instead.

To store an image, you start by constructing a :sip:ref:`~PyQt6.QtGui.QImageWriter` object. Pass either a file name or a device pointer, and the image format to :sip:ref:`~PyQt6.QtGui.QImageWriter`'s constructor. You can then set several options, such as quality (by calling :sip:ref:`~PyQt6.QtGui.QImageWriter.setQuality`). :sip:ref:`~PyQt6.QtGui.QImageWriter.canWrite` returns ``true`` if :sip:ref:`~PyQt6.QtGui.QImageWriter` can write the image (i.e., the image format is supported and the device is open for writing). Call :sip:ref:`~PyQt6.QtGui.QImageWriter.write` to write the image to the device.

If any error occurs when writing the image, :sip:ref:`~PyQt6.QtGui.QImageWriter.write` will return false. You can then call :sip:ref:`~PyQt6.QtGui.QImageWriter.error` to find the type of error that occurred, or :sip:ref:`~PyQt6.QtGui.QImageWriter.errorString` to get a human readable description of what went wrong.

Call :sip:ref:`~PyQt6.QtGui.QImageWriter.supportedImageFormats` for a list of formats that :sip:ref:`~PyQt6.QtGui.QImageWriter` can write. :sip:ref:`~PyQt6.QtGui.QImageWriter` supports all built-in image formats, in addition to any image format plugins that support writing.

**Note:** :sip:ref:`~PyQt6.QtGui.QImageWriter` assumes exclusive control over the file or device that is assigned. Any attempts to modify the assigned file or device during the lifetime of the :sip:ref:`~PyQt6.QtGui.QImageWriter` object will yield undefined results. If immediate access to a resource is desired, the use of a scope is the recommended method.

For example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-qimagewriter-main.py
    :lines: 56-65

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageReader`, :sip:ref:`~PyQt6.QtGui.QImageIOHandler`, QImageIOPlugin, :sip:ref:`~PyQt6.QtGui.QColorSpace`.
