.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: ()
    :digest: 312b6f38fa6f106e30ae1bfd9ada25d8

Returns the release version of the operating system kernel. On Windows, it returns the version of the NT kernel. On Unix systems, including Android and macOS, it returns the same as the ``uname -r`` command would return.

If the version could not be determined, this function may return an empty string.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSysInfo.kernelType`, :sip:ref:`~PyQt6.QtCore.QSysInfo.productType`, :sip:ref:`~PyQt6.QtCore.QSysInfo.productVersion`, :sip:ref:`~PyQt6.QtCore.QSysInfo.prettyProductName`.
