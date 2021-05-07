.. sip:method-description::
    :status: todo
    :pysig: 41c7f47ed21b0380d7bef8d10e1cbb7b
    :realsig: (QDir::Filters)
    :digest: c60060e1d6ae6e5d456305a06ed60d8f

Sets the directory model's filter to that specified by *filters*.

Note that the filter you set should always include the :sip:ref:`~PyQt6.QtCore.QDir.Filter.AllDirs` enum value, otherwise :sip:ref:`~PyQt6.QtGui.QFileSystemModel` won't be able to read the directory structure.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFileSystemModel.filter`, QDir::Filters.
