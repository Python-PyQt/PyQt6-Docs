.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: eac6019e4ad151011ad38bbe5834aad0

Returns ``true`` if an image can be read for the device (i.e., the image format is supported, and the device seems to contain valid data); otherwise returns ``false``.

is a lightweight function that only does a quick test to see if the image data is valid. :sip:ref:`~PyQt6.QtGui.QImageReader.read` may still return false after  returns ``true``, if the image data is corrupt.

**Note:** A :sip:ref:`~PyQt6.QtCore.QMimeDatabase` lookup is normally a better approach than this function for identifying potentially non-image files or data.

For images that support animation,  returns ``false`` when all frames have been read.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageReader.read`, :sip:ref:`~PyQt6.QtGui.QImageReader.supportedImageFormats`, :sip:ref:`~PyQt6.QtCore.QMimeDatabase`.
