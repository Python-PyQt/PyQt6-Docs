.. sip:method-description::
    :status: todo
    :pysig: 8f2adb7188e25d6b1c3defb90144db64
    :realsig: (QDir::Filters, QDir::SortFlags) const
    :digest: 4fccd206f43bd5422c52e4d71429d24c

This is an overloaded function.

Returns a list of the names of all the files and directories in the directory, ordered according to the name and attribute filters previously set with :sip:ref:`~PyQt6.QtCore.QDir.setNameFilters` and :sip:ref:`~PyQt6.QtCore.QDir.setFilter`, and sorted according to the flags set with :sip:ref:`~PyQt6.QtCore.QDir.setSorting`.

The attribute filter and sorting specifications can be overridden using the *filters* and *sort* arguments.

Returns an empty list if the directory is unreadable, does not exist, or if nothing matches the specification.

**Note:** To list symlinks that point to non existing files, :sip:ref:`~PyQt6.QtCore.QDir.Filter.System` must be passed to the filter.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.entryInfoList`, :sip:ref:`~PyQt6.QtCore.QDir.setNameFilters`, :sip:ref:`~PyQt6.QtCore.QDir.setSorting`, :sip:ref:`~PyQt6.QtCore.QDir.setFilter`.
