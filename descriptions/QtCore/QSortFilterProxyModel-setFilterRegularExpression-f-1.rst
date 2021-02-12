.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 881ab013c6b6f5de6e27eeff738c233c

Sets the regular expression used to filter the contents of the source model to *pattern*.

This method should be preferred for new code as it will use `QRegularExpression <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qregularexpression>`_ internally.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.setFilterCaseSensitivity`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.setFilterWildcard`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.setFilterFixedString`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterRegularExpression`.
