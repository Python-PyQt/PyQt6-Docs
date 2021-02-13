.. sip:class-description::
    :status: todo
    :brief: Keeps track of a view's selected items
    :digest: 26c33118a81bae2e284f51ab33e8fb18

The :sip:ref:`~PyQt6.QtCore.QItemSelectionModel` class keeps track of a view's selected items.

A :sip:ref:`~PyQt6.QtCore.QItemSelectionModel` keeps track of the selected items in a view, or in several views onto the same model. It also keeps track of the currently selected item in a view.

The :sip:ref:`~PyQt6.QtCore.QItemSelectionModel` class is one of the `Model/View Classes <https://doc.qt.io/qt-6/model-view-programming.html#model-view-classes>`_ and is part of Qt's `model/view framework <https://doc.qt.io/qt-6/model-view-programming.html>`_.

The selected items are stored using ranges. Whenever you want to modify the selected items use :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.select` and provide either a :sip:ref:`~PyQt6.QtCore.QItemSelection`, or a :sip:ref:`~PyQt6.QtCore.QModelIndex` and a :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.SelectionFlags`.

The :sip:ref:`~PyQt6.QtCore.QItemSelectionModel` takes a two layer approach to selection management, dealing with both selected items that have been committed and items that are part of the current selection. The current selected items are part of the current interactive selection (for example with rubber-band selection or keyboard-shift selections).

To update the currently selected items, use the bitwise OR of :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.SelectionFlags.Current` and any of the other SelectionFlags. If you omit the :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.SelectionFlags.Current` command, a new current selection will be created, and the previous one added to the whole selection. All functions operate on both layers; for example, :sip:ref:`~PyQt6.QtWidgets.QTableWidget.selectedItems` will return items from both layers.

**Note:** Since 5.5, :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.model`, :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.hasSelection`, and :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.currentIndex` are meta-object properties.

.. seealso:: `Model/View Programming <https://doc.qt.io/qt-6/model-view-programming.html>`_, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`, `Chart Example <https://doc.qt.io/qt-6/qtwidgets-itemviews-chart-example.html>`_.
