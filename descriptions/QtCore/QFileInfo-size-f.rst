.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 1690baa215ac27b7d62af3dd5bfcd411

Returns the file size in bytes. If the file does not exist or cannot be fetched, 0 is returned.

If the file is a symlink, this function returns information about the target, not the symlink.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.exists`.
