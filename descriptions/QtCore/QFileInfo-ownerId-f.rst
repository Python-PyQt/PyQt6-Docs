.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: ad805da3bc59f0fb64552bded782b9c1

Returns the id of the owner of the file.

On Windows and on systems where files do not have owners this function returns ((uint) -2).

If the file is a symlink, this function returns information about the target, not the symlink.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.owner`, :sip:ref:`~PyQt6.QtCore.QFileInfo.group`, :sip:ref:`~PyQt6.QtCore.QFileInfo.groupId`.
