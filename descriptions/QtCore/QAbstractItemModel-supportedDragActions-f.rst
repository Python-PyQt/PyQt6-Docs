.. sip:method-description::
    :status: todo
    :pysig: b730747ccdc682ff41f5a1b741c1a110
    :realsig: () const
    :digest: 100af785916e08505fc3fbd3bf9c635d

Returns the actions supported by the data in this model.

The default implementation returns :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.supportedDropActions`. Reimplement this function if you wish to support additional actions.

supportedDragActions() is used by :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.startDrag` as the default values when a drag occurs.

.. seealso:: Qt::DropActions, `Using drag and drop with item views <https://doc.qt.io/qt-6/model-view-programming.html#using-drag-and-drop-with-item-views>`_.
