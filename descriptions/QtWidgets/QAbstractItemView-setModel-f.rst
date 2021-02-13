.. sip:method-description::
    :status: todo
    :pysig: b1398307ea89da5fe868fb6740f9bc55
    :realsig: (QAbstractItemModel*)
    :digest: cc06dc06f032dd64630d8aa46dc1c02a

Sets the *model* for the view to present.

This function will create and set a new selection model, replacing any model that was previously set with :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.setSelectionModel`. However, the old selection model will not be deleted as it may be shared between several views. We recommend that you delete the old selection model if it is no longer required. This is done with the following code:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_itemviews_qabstractitemview.py
    :lines: 67-69

If both the old model and the old selection model do not have parents, or if their parents are long-lived objects, it may be preferable to call their deleteLater() functions to explicitly delete them.

The view *does not* take ownership of the model unless it is the model's parent object because the model may be shared between many different views.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.model`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.selectionModel`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.setSelectionModel`.
