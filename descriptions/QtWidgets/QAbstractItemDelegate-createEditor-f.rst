.. sip:method-description::
    :status: todo
    :pysig: 3c88d0599793f3bcb2fd2e61089ee0b2
    :realsig: (QWidget*,const QStyleOptionViewItem&,const QModelIndex&) const
    :digest: 164b77eac63db5c844fd4f3b8d69359f

Returns the editor to be used for editing the data item with the given *index*. Note that the index contains information about the model being used. The editor's parent widget is specified by *parent*, and the item options by *option*.

The base implementation returns ``nullptr``. If you want custom editing you will need to reimplement this function.

The returned editor widget should have :sip:ref:`~PyQt6.QtCore.Qt.FocusPolicy.StrongFocus`; otherwise, :sip:ref:`~PyQt6.QtGui.QMouseEvent`\ s received by the widget will propagate to the view. The view's background will shine through unless the editor paints its own background (e.g., with :sip:ref:`~PyQt6.QtWidgets.QWidget.setAutoFillBackground`).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.destroyEditor`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.setModelData`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.setEditorData`.
