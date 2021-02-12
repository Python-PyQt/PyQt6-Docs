.. sip:method-description::
    :status: todo
    :pysig: bc433f34a736713d77fa06b4c6325f0a
    :realsig: (const QString&)
    :digest: 32e04b88f0309aa66918aa541671ea2c

Returns *pathName* with the '/' separators converted to separators that are appropriate for the underlying operating system.

On Windows, ("c:/winnt/system32") returns "c:\\winnt\\system32".

The returned string may be the same as the argument on some operating systems, for example on Unix.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.fromNativeSeparators`, :sip:ref:`~PyQt6.QtCore.QDir.separator`.
