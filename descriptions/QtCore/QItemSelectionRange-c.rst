.. sip:class-description::
    :status: todo
    :brief: Manages information about a range of selected items in a model
    :digest: 6dcc930ab5494e55a611fa62de5e7236

The :sip:ref:`~PyQt6.QtCore.QItemSelectionRange` class manages information about a range of selected items in a model.

A :sip:ref:`~PyQt6.QtCore.QItemSelectionRange` contains information about a range of selected items in a model. A range of items is a contiguous array of model items, extending to cover a number of adjacent rows and columns with a common parent item; this can be visualized as a two-dimensional block of cells in a table. A selection range has a :sip:ref:`~PyQt6.QtCore.QItemSelectionRange.top`, :sip:ref:`~PyQt6.QtCore.QItemSelectionRange.left` a :sip:ref:`~PyQt6.QtCore.QItemSelectionRange.bottom`, :sip:ref:`~PyQt6.QtCore.QItemSelectionRange.right` and a :sip:ref:`~PyQt6.QtCore.QItemSelectionRange.parent`.

The :sip:ref:`~PyQt6.QtCore.QItemSelectionRange` class is one of the Model/View Classes and is part of Qt's model/view framework.

The model items contained in the selection range can be obtained using the :sip:ref:`~PyQt6.QtCore.QItemSelectionRange.indexes` function. Use :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.selectedIndexes` to get a list of all selected items for a view.

You can determine whether a given model item lies within a particular range by using the :sip:ref:`~PyQt6.QtCore.QItemSelectionRange.contains` function. Ranges can also be compared using the overloaded operators for equality and inequality, and the :sip:ref:`~PyQt6.QtCore.QItemSelectionRange.intersects` function allows you to determine whether two ranges overlap.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`, :sip:ref:`~PyQt6.QtCore.QItemSelection`, :sip:ref:`~PyQt6.QtCore.QItemSelectionModel`, Model/View Programming.
