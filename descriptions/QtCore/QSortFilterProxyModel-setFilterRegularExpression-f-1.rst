.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: dea007e9ad1da14d94eaa8eb8a98e684

Sets the regular expression used to filter the contents of the source model to *pattern*.

This method should be preferred for new code as it will use :sip:ref:`~PyQt6.QtCore.QRegularExpression` internally.

This method will reset the regular expression options but respect case sensitivity.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.setFilterCaseSensitivity`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.setFilterWildcard`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.setFilterFixedString`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterRegularExpression`.
