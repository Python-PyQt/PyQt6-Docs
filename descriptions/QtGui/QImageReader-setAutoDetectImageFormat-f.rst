.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: a7a2c56933b5f17a9ef9bf7d4f13dda0

If *enabled* is true, image format autodetection is enabled; otherwise, it is disabled. By default, autodetection is enabled.

:sip:ref:`~PyQt6.QtGui.QImageReader` uses an extensive approach to detecting the image format; firstly, if you pass a file name to :sip:ref:`~PyQt6.QtGui.QImageReader`, it will attempt to detect the file extension if the given file name does not point to an existing file, by appending supported default extensions to the given file name, one at a time. It then uses the following approach to detect the image format:

* Image plugins are queried first, based on either the optional format string, or the file name suffix (if the source device is a file). No content detection is done at this stage. :sip:ref:`~PyQt6.QtGui.QImageReader` will choose the first plugin that supports reading for this format.

* If no plugin supports the image format, Qt's built-in handlers are checked based on either the optional format string, or the file name suffix.

* If no capable plugins or built-in handlers are found, each plugin is tested by inspecting the content of the data stream.

* If no plugins could detect the image format based on data contents, each built-in image handler is tested by inspecting the contents.

* Finally, if all above approaches fail, :sip:ref:`~PyQt6.QtGui.QImageReader` will report failure when trying to read the image.

By disabling image format autodetection, :sip:ref:`~PyQt6.QtGui.QImageReader` will only query the plugins and built-in handlers based on the format string (i.e., no file name extensions are tested).

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageReader.autoDetectImageFormat`, :sip:ref:`~PyQt6.QtGui.QImageIOHandler.canRead`, QImageIOPlugin::capabilities().
