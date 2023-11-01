.. sip:method-description::
    :status: todo
    :pysig: 5ae4df144bb6014c3175a8eeb873f7f7
    :realsig: (const QString&)
    :digest: ca24b4cabb8c7bb792bda2596d8b6da1

Returns *pathName* with the '/' separators converted to separators that are appropriate for the underlying operating system.

On Windows, toNativeSeparators("c:/winnt/system32") returns "c:\\winnt\\system32".

The returned string may be the same as the argument on some operating systems, for example on Unix.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.fromNativeSeparators`, :sip:ref:`~PyQt6.QtCore.QDir.separator`.
