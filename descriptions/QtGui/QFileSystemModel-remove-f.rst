.. sip:method-description::
    :status: todo
    :pysig: 6fb4529d327b1b51fc62577b3656a5a6
    :realsig: (const QModelIndex&)
    :digest: b1b286e3085ebb21e17bf9528360635f

Removes the model item *index* from the file system model and **deletes the corresponding file from the file system**, returning true if successful. If the item cannot be removed, false is returned.

**Warning:** This function deletes files from the file system; it does **not** move them to a location where they can be recovered.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFileSystemModel.rmdir`.
