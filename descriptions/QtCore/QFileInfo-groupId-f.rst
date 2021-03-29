.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 832d6041c315efb3c802b1f802abcd33

Returns the id of the group the file belongs to.

On Windows and on systems where files do not have groups this function always returns (uint) -2.

If the file is a symlink, this function returns the id of the group owning the target (not the symlink).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.group`, :sip:ref:`~PyQt6.QtCore.QFileInfo.owner`, :sip:ref:`~PyQt6.QtCore.QFileInfo.ownerId`.
