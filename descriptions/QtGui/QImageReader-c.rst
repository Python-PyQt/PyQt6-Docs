.. sip:class-description::
    :status: todo
    :brief: Format independent interface for reading images from files or other devices
    :digest: 68349f6971cede199f7b43ff0924c4be

The :sip:ref:`~PyQt6.QtGui.QImageReader` class provides a format independent interface for reading images from files or other devices.

The most common way to read images is through :sip:ref:`~PyQt6.QtGui.QImage` and :sip:ref:`~PyQt6.QtGui.QPixmap`'s constructors, or by calling QImage::load() and :sip:ref:`~PyQt6.QtGui.QPixmap.load`. :sip:ref:`~PyQt6.QtGui.QImageReader` is a specialized class which gives you more control when reading images. For example, you can read an image into a specific size by calling :sip:ref:`~PyQt6.QtGui.QImageReader.setScaledSize`, and you can select a clip rect, effectively loading only parts of an image, by calling :sip:ref:`~PyQt6.QtGui.QImageReader.setClipRect`. Depending on the underlying support in the image format, this can save memory and speed up loading of images.

To read an image, you start by constructing a :sip:ref:`~PyQt6.QtGui.QImageReader` object. Pass either a file name or a device pointer, and the image format to :sip:ref:`~PyQt6.QtGui.QImageReader`'s constructor. You can then set several options, such as the clip rect (by calling :sip:ref:`~PyQt6.QtGui.QImageReader.setClipRect`) and scaled size (by calling :sip:ref:`~PyQt6.QtGui.QImageReader.setScaledSize`). :sip:ref:`~PyQt6.QtGui.QImageReader.canRead` returns the image if the :sip:ref:`~PyQt6.QtGui.QImageReader` can read the image (i.e., the image format is supported and the device is open for reading). Call :sip:ref:`~PyQt6.QtGui.QImageReader.read` to read the image.

If any error occurs when reading the image, :sip:ref:`~PyQt6.QtGui.QImageReader.read` will return a null :sip:ref:`~PyQt6.QtGui.QImage`. You can then call :sip:ref:`~PyQt6.QtGui.QImageReader.error` to find the type of error that occurred, or :sip:ref:`~PyQt6.QtGui.QImageReader.errorString` to get a human readable description of what went wrong.

**Note:** :sip:ref:`~PyQt6.QtGui.QImageReader` assumes exclusive control over the file or device that is assigned. Any attempts to modify the assigned file or device during the lifetime of the :sip:ref:`~PyQt6.QtGui.QImageReader` object will yield undefined results.

.. _qimagereader-formats:

Formats
-------

Call :sip:ref:`~PyQt6.QtGui.QImageReader.supportedImageFormats` for a list of formats that :sip:ref:`~PyQt6.QtGui.QImageReader` can read. :sip:ref:`~PyQt6.QtGui.QImageReader` supports all built-in image formats, in addition to any image format plugins that support reading. Call :sip:ref:`~PyQt6.QtGui.QImageReader.supportedMimeTypes` to obtain a list of supported MIME types, which for example can be passed to :sip:ref:`~PyQt6.QtWidgets.QFileDialog.setMimeTypeFilters`.

:sip:ref:`~PyQt6.QtGui.QImageReader` autodetects the image format by default, by looking at the provided (optional) format string, the file name suffix, and the data stream contents. You can enable or disable this feature, by calling :sip:ref:`~PyQt6.QtGui.QImageReader.setAutoDetectImageFormat`.

.. _qimagereader-high-resolution-versions-of-images:

High Resolution Versions of Images
----------------------------------

It is possible to provide high resolution versions of images should a scaling between *device pixels* and *device independent pixels* be in effect.

The high resolution version is marked by the suffix ``@2x`` on the base name. The image read will have its *device pixel ratio* set to a value of 2.

This can be disabled by setting the environment variable ``QT_HIGHDPI_DISABLE_2X_IMAGE_LOADING``.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageWriter`, :sip:ref:`~PyQt6.QtGui.QImageIOHandler`, QImageIOPlugin, :sip:ref:`~PyQt6.QtCore.QMimeDatabase`, :sip:ref:`~PyQt6.QtGui.QColorSpace`, :sip:ref:`~PyQt6.QtGui.QImage.devicePixelRatio`, :sip:ref:`~PyQt6.QtGui.QPixmap.devicePixelRatio`, :sip:ref:`~PyQt6.QtGui.QIcon`, :sip:ref:`~PyQt6.QtGui.QPainter.drawPixmap`, :sip:ref:`~PyQt6.QtGui.QPainter.drawImage`.
