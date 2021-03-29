.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: ()
    :digest: 02475238adf1f570af767f1835a692b9

Returns the absolute canonical path of the system's temporary directory.

On Unix/Linux systems this is the path in the ``TMPDIR`` environment variable or ``/tmp`` if ``TMPDIR`` is not defined. On Windows this is usually the path in the ``TEMP`` or ``TMP`` environment variable. The path returned by this method doesn't end with a directory separator unless it is the root directory (of a drive).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.temp`, :sip:ref:`~PyQt6.QtCore.QDir.currentPath`, :sip:ref:`~PyQt6.QtCore.QDir.homePath`, :sip:ref:`~PyQt6.QtCore.QDir.rootPath`.
