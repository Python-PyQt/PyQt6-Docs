.. sip:method-description::
    :status: todo
    :pysig: eaae71d15436c8d7ac2fa741d569ba58
    :realsig: (const QStringList&, QDir::Filters, QDir::SortFlags) const
    :digest: 78c22ae4134e38b34127267a2b93f73f

Returns a list of the names of all the files and directories in the directory, ordered according to the name and attribute filters previously set with :sip:ref:`~PyQt6.QtCore.QDir.setNameFilters` and :sip:ref:`~PyQt6.QtCore.QDir.setFilter`, and sorted according to the flags set with :sip:ref:`~PyQt6.QtCore.QDir.setSorting`.

The name filter, file attribute filter, and sorting specification can be overridden using the *nameFilters*, *filters*, and *sort* arguments.

Returns an empty list if the directory is unreadable, does not exist, or if nothing matches the specification.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.entryInfoList`, :sip:ref:`~PyQt6.QtCore.QDir.setNameFilters`, :sip:ref:`~PyQt6.QtCore.QDir.setSorting`, :sip:ref:`~PyQt6.QtCore.QDir.setFilter`.
