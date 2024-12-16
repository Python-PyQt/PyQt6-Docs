.. sip:method-description::
    :status: todo
    :pysig: 3c9a938a1e983dbe538fd869f2db5e67
    :realsig: () const
    :digest: 1dd037eb4f5aadbabe1a8101f5ecf6f8

Returns the list of allowed MIME types. By default, the built-in models and views use an internal MIME type: ``application/x-qabstractitemmodeldatalist``.

When implementing drag and drop support in a custom model, if you will return data in formats other than the default internal MIME type, reimplement this function to return your list of MIME types.

If you reimplement this function in your custom model, you must also reimplement the member functions that call it: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.mimeData` and :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.dropMimeData`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.mimeData`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.dropMimeData`.
