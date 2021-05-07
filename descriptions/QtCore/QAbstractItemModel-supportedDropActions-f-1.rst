.. sip:method-description::
    :status: todo
    :pysig: f96f3c238b7a27038ccd0c6e71900feb
    :realsig: () const
    :digest: 0cca8c0bb5958fe233bf7bd3a60c757a

Returns the drop actions supported by this model.

The default implementation returns :sip:ref:`~PyQt6.QtCore.Qt.DropAction.CopyAction`. Reimplement this function if you wish to support additional actions. You must also reimplement the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.dropMimeData` function to handle the additional operations.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.dropMimeData`, Qt::DropActions, `Using drag and drop with item views <https://doc.qt.io/qt-6/model-view-programming.html#using-drag-and-drop-with-item-views>`_.
