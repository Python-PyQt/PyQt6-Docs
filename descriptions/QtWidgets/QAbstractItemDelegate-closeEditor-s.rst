.. sip:signal-description::
    :status: todo
    :pysig: 92a810d976ec906d82e096c6a5e0f7a0
    :realsig: (QWidget*,QAbstractItemDelegate::EndEditHint)
    :digest: 5098009746732d5d5d37c14a67742dd2

This signal is emitted when the user has finished editing an item using the specified *editor*.

The *hint* provides a way for the delegate to influence how the model and view behave after editing is completed. It indicates to these components what action should be performed next to provide a comfortable editing experience for the user. For example, if ``EditNextItem`` is specified, the view should use a delegate to open an editor on the next item in the model.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.EndEditHint.EndEditHint`.
