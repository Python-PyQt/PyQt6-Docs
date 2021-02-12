.. sip:method-description::
    :status: todo
    :pysig: 59dcba40458209889f951d64f3f78280
    :realsig: (const QModelIndexList&) const
    :digest: 77d97cc11b5e64e44bee9677b9f76dd5

Returns an object that contains serialized items of data corresponding to the list of *indexes* specified. The format used to describe the encoded data is obtained from the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.mimeTypes` function. This default implementation uses the default MIME type returned by the default implementation of :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.mimeTypes`. If you reimplement :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.mimeTypes` in your custom model to return more MIME types, reimplement this function to make use of them.

If the list of *indexes* is empty, or there are no supported MIME types, ``nullptr`` is returned rather than a serialized empty list.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.mimeTypes`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.dropMimeData`.
