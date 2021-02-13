.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: d216868c9319628402a6b8442177dfac

Sets how precise :sip:ref:`~PyQt6.QtWidgets.QHeaderView` should calculate the size when :sip:ref:`~PyQt6.QtWidgets.QHeaderView.ResizeMode.ResizeToContents` is used. A low value will provide a less accurate but fast auto resize while a higher value will provide a more accurate resize that however can be slow.

The number *precision* specifies how many sections that should be consider when calculating the preferred size.

The default value is 1000 meaning that a horizontal column with auto-resize will look at maximum 1000 rows on calculating when doing an auto resize.

Special value 0 means that it will look at only the visible area. Special value -1 will imply looking at all elements.

This value is used in :sip:ref:`~PyQt6.QtWidgets.QTableView.sizeHintForColumn`, :sip:ref:`~PyQt6.QtWidgets.QTableView.sizeHintForRow` and :sip:ref:`~PyQt6.QtWidgets.QTreeView.sizeHintForColumn`. Reimplementing these functions can make this function not having an effect.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QHeaderView.resizeContentsPrecision`, :sip:ref:`~PyQt6.QtWidgets.QHeaderView.setSectionResizeMode`, :sip:ref:`~PyQt6.QtWidgets.QHeaderView.resizeSections`, :sip:ref:`~PyQt6.QtWidgets.QTableView.sizeHintForColumn`, :sip:ref:`~PyQt6.QtWidgets.QTableView.sizeHintForRow`, :sip:ref:`~PyQt6.QtWidgets.QTreeView.sizeHintForColumn`.
