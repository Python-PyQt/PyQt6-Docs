.. sip:method-description::
    :status: todo
    :pysig: 5bf43686fc64e83f37d14845c850ae74
    :realsig: (const QItemSelection&,QItemSelectionModel::SelectionFlags)
    :digest: 3e8d3d61b57d3bfcb4178c13651e1aab

Merges the *other* selection with this :sip:ref:`~PyQt6.QtCore.QItemSelection` using the *command* given. This method guarantees that no ranges are overlapping.

Note that only :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.SelectionFlags.Select`, :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.SelectionFlags.Deselect`, and :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.SelectionFlags.Toggle` are supported.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QItemSelection.split`.
