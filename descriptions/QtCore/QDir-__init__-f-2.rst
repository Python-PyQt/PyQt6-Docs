.. sip:method-description::
    :status: todo
    :pysig: 920a189a10ec1fe6f3d25084ac3c514b
    :realsig: (const QString&,const QString&,QDir::SortFlags,QDir::Filters)
    :digest: 98c3111f84d9badc13eb740147f67b49

Constructs a :sip:ref:`~PyQt6.QtCore.QDir` with path *path*, that filters its entries by name using *nameFilter* and by attributes using *filters*. It also sorts the names using *sort*.

The default *nameFilter* is an empty string, which excludes nothing; the default *filters* is :sip:ref:`~PyQt6.QtCore.QDir.Filters.AllEntries`, which also excludes nothing. The default *sort* is :sip:ref:`~PyQt6.QtCore.QDir.SortFlags.Name` | :sip:ref:`~PyQt6.QtCore.QDir.SortFlags.IgnoreCase`, i.e. sort by name case-insensitively.

If *path* is an empty string, :sip:ref:`~PyQt6.QtCore.QDir` uses "." (the current directory). If *nameFilter* is an empty string, :sip:ref:`~PyQt6.QtCore.QDir` uses the name filter "\*" (all files).

**Note:** *path* need not exist.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.exists`, :sip:ref:`~PyQt6.QtCore.QDir.setPath`, :sip:ref:`~PyQt6.QtCore.QDir.setNameFilters`, :sip:ref:`~PyQt6.QtCore.QDir.setFilter`, :sip:ref:`~PyQt6.QtCore.QDir.setSorting`.
