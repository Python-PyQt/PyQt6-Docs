.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: da06699311de425d90873ae0ec62f8fc

Returns ``true`` if data can be written to the device; otherwise returns false.

This is a convenience function which checks if the OpenMode of the device contains the :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenMode.WriteOnly` flag.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.openMode`, OpenMode.
