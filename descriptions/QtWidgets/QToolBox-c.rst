.. sip:class-description::
    :status: todo
    :brief: Column of tabbed widget items
    :digest: d724950bfe31e7e6333ea56f8ca66ac4

The :sip:ref:`~PyQt6.QtWidgets.QToolBox` class provides a column of tabbed widget items.

A toolbox is a widget that displays a column of tabs one above the other, with the current item displayed below the current tab. Every tab has an index position within the column of tabs. A tab's item is a `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_.

Each item has an :sip:ref:`~PyQt6.QtWidgets.QToolBox.itemText`, an optional :sip:ref:`~PyQt6.QtWidgets.QToolBox.itemIcon`, an optional :sip:ref:`~PyQt6.QtWidgets.QToolBox.itemToolTip`, and a :sip:ref:`~PyQt6.QtWidgets.QToolBox.widget`. The item's attributes can be changed with :sip:ref:`~PyQt6.QtWidgets.QToolBox.setItemText`, :sip:ref:`~PyQt6.QtWidgets.QToolBox.setItemIcon`, and :sip:ref:`~PyQt6.QtWidgets.QToolBox.setItemToolTip`. Each item can be enabled or disabled individually with :sip:ref:`~PyQt6.QtWidgets.QToolBox.setItemEnabled`.

Items are added using :sip:ref:`~PyQt6.QtWidgets.QToolBox.addItem`, or inserted at particular positions using :sip:ref:`~PyQt6.QtWidgets.QToolBox.insertItem`. The total number of items is given by :sip:ref:`~PyQt6.QtWidgets.QToolBox.count`. Items can be deleted with delete, or removed from the toolbox with :sip:ref:`~PyQt6.QtWidgets.QToolBox.removeItem`. Combining :sip:ref:`~PyQt6.QtWidgets.QToolBox.removeItem` and :sip:ref:`~PyQt6.QtWidgets.QToolBox.insertItem` allows you to move items to different positions.

The index of the current item widget is returned by :sip:ref:`~PyQt6.QtWidgets.QToolBox.currentIndex`, and set with :sip:ref:`~PyQt6.QtWidgets.QToolBox.setCurrentIndex`. The index of a particular item can be found using :sip:ref:`~PyQt6.QtWidgets.QToolBox.indexOf`, and the item at a given index is returned by item().

The :sip:ref:`~PyQt6.QtWidgets.QToolBox.currentChanged` signal is emitted when the current item is changed.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTabWidget`.
