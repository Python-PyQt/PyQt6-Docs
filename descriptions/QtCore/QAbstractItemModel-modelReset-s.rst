.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 728d5ce396c51053b611ee5045830027

This signal is emitted when :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.endResetModel` is called, after the model's internal state (e.g. persistent model indexes) has been invalidated.

Note that if a model is reset it should be considered that all information previously retrieved from it is invalid. This includes but is not limited to the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.rowCount` and :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.columnCount`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.flags`, data retrieved through :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.data`, and :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.roleNames`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.endResetModel`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.modelAboutToBeReset`.
