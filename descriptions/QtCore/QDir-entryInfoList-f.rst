.. sip:method-description::
    :status: todo
    :pysig: 4f692b7fa8176afb546c34c72f2d842b
    :realsig: (QDir::Filters,QDir::SortFlags) const
    :digest: dea02e41e34768f01e7ff76ecb8e44c0

This is an overloaded function.

Returns a list of :sip:ref:`~PyQt6.QtCore.QFileInfo` objects for all the files and directories in the directory, ordered according to the name and attribute filters previously set with :sip:ref:`~PyQt6.QtCore.QDir.setNameFilters` and :sip:ref:`~PyQt6.QtCore.QDir.setFilter`, and sorted according to the flags set with :sip:ref:`~PyQt6.QtCore.QDir.setSorting`.

The attribute filter and sorting specifications can be overridden using the *filters* and *sort* arguments.

Returns an empty list if the directory is unreadable, does not exist, or if nothing matches the specification.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.entryList`, :sip:ref:`~PyQt6.QtCore.QDir.setNameFilters`, :sip:ref:`~PyQt6.QtCore.QDir.setSorting`, :sip:ref:`~PyQt6.QtCore.QDir.setFilter`, :sip:ref:`~PyQt6.QtCore.QDir.isReadable`, :sip:ref:`~PyQt6.QtCore.QDir.exists`.
