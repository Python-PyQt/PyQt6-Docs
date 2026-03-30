.. sip:method-description::
    :status: todo
    :pysig: 607949925283b263ed00ac5fb0dd5f9d
    :realsig: (const QString&)
    :digest: 038b733bf3d9c85666ac6962c567c67c

Returns *pathName* using '/' as file separator. On Windows, for instance, fromNativeSeparators("``c:\\winnt\\system32``") returns "c:/winnt/system32".

The returned string may be the same as the argument on some operating systems, for example on Unix.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.toNativeSeparators`, :sip:ref:`~PyQt6.QtCore.QDir.separator`.
