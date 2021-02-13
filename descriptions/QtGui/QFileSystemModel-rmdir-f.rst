.. sip:method-description::
    :status: todo
    :pysig: 6fb4529d327b1b51fc62577b3656a5a6
    :realsig: (const QModelIndex&)
    :digest: 6907ad788ad891ed9b372039f55dac11

Removes the directory corresponding to the model item *index* in the file system model and **deletes the corresponding directory from the file system**, returning true if successful. If the directory cannot be removed, false is returned.

**Warning:** This function deletes directories from the file system; it does **not** move them to a location where they can be recovered.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFileSystemModel.remove`.
