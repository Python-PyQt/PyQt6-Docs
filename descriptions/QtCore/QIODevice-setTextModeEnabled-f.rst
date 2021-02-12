.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 80a095c04fe6c84d5ada6711a207f192

If *enabled* is true, this function sets the :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenMode.Text` flag on the device; otherwise the :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenMode.Text` flag is removed. This feature is useful for classes that provide custom end-of-line handling on a :sip:ref:`~PyQt6.QtCore.QIODevice`.

The IO device should be opened before calling this function.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.isTextModeEnabled`, :sip:ref:`~PyQt6.QtCore.QIODevice.open`, :sip:ref:`~PyQt6.QtCore.QIODevice.setOpenMode`.
