.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: ffe7d5ab661a2717341bc7f3da00d403

Returns true if this object contains a valid native IPC key type. Invalid types are usually the result of a failure to parse a string representation using :sip:ref:`~PyQt6.QtCore.QNativeIpcKey.fromString`.

This function performs no check on the whether the key string is actually supported or valid for the current operating system.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QNativeIpcKey.type`, :sip:ref:`~PyQt6.QtCore.QNativeIpcKey.fromString`.
