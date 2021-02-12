.. sip:class-description::
    :status: todo
    :brief: Keeps track of a view's selected items
    :digest: 7037cf374318054639bff7a1326ef8d7

The :sip:ref:`~PyQt6.QtCore.QItemSelectionModel` class keeps track of a view's selected items.

A :sip:ref:`~PyQt6.QtCore.QItemSelectionModel` keeps track of the selected items in a view, or in several views onto the same model. It also keeps track of the currently selected item in a view.

The :sip:ref:`~PyQt6.QtCore.QItemSelectionModel` class is one of the Model/View Classes and is part of Qt's model/view framework.

The selected items are stored using ranges. Whenever you want to modify the selected items use :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.select` and provide either a :sip:ref:`~PyQt6.QtCore.QItemSelection`, or a :sip:ref:`~PyQt6.QtCore.QModelIndex` and a :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.SelectionFlags`.

The :sip:ref:`~PyQt6.QtCore.QItemSelectionModel` takes a two layer approach to selection management, dealing with both selected items that have been committed and items that are part of the current selection. The current selected items are part of the current interactive selection (for example with rubber-band selection or keyboard-shift selections).

To update the currently selected items, use the bitwise OR of :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.SelectionFlags.Current` and any of the other SelectionFlags. If you omit the :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.SelectionFlags.Current` command, a new current selection will be created, and the previous one added to the whole selection. All functions operate on both layers; for example, selecteditems() will return items from both layers.

**Note:** Since 5.5, :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.model`, :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.hasSelection`, and :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.currentIndex` are meta-object properties.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`, Model/View Programming.
