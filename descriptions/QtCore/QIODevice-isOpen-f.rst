.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: d8fe948f1014c79de8ab48b435fee879

Returns ``true`` if the device is open; otherwise returns ``false``. A device is open if it can be read from and/or written to. By default, this function returns ``false`` if :sip:ref:`~PyQt6.QtCore.QIODevice.openMode` returns ``NotOpen``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.openMode`, QIODeviceBase::OpenMode.
