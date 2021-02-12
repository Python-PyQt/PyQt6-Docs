.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: ab4e9bb2dee393af2df163a4e10314b8

Returns the file size in bytes. If the file does not exist or cannot be fetched, 0 is returned.

If the file is a symlink, the size of the target file is returned (not the symlink).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.exists`.
