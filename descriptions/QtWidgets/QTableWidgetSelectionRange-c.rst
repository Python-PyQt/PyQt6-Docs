.. sip:class-description::
    :status: todo
    :brief: Way to interact with selection in a model without using model indexes and a selection model
    :digest: 6af0c82ba0b67775d18d7bd7d235764e

The :sip:ref:`~PyQt6.QtWidgets.QTableWidgetSelectionRange` class provides a way to interact with selection in a model without using model indexes and a selection model.

The :sip:ref:`~PyQt6.QtWidgets.QTableWidgetSelectionRange` class stores the top left and bottom right rows and columns of a selection range in a table. The selections in the table may consist of several selection ranges.

**Note:** If the item within the selection range is marked as not selectable, e.g., ``itemFlags() & Qt::ItemIsSelectable == 0`` then it will not appear in the selection range.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTableWidget`.
