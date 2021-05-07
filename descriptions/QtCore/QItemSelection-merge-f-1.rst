.. sip:method-description::
    :status: todo
    :pysig: 9b4022f31ca120cfb49df671cbcdaa6b
    :realsig: (const QItemSelection&,QItemSelectionModel::SelectionFlags)
    :digest: 3e8d3d61b57d3bfcb4178c13651e1aab

Merges the *other* selection with this :sip:ref:`~PyQt6.QtCore.QItemSelection` using the *command* given. This method guarantees that no ranges are overlapping.

Note that only :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.SelectionFlag.Select`, :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.SelectionFlag.Deselect`, and :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.SelectionFlag.Toggle` are supported.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QItemSelection.split`.
