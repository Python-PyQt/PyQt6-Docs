.. sip:method-description::
    :status: todo
    :pysig: 344a6f60a58aae12595c4742b0d0c376
    :realsig: (const QModelIndex&,QAbstractItemView::EditTrigger,QEvent*)
    :digest: cb6d3957318e4e994a22284ea90a4c8b

Starts editing the item at *index*, creating an editor if necessary, and returns ``true`` if the view's :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.State.State` is now :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.State.EditingState`; otherwise returns ``false``.

The action that caused the editing process is described by *trigger*, and the associated event is specified by *event*.

Editing can be forced by specifying the *trigger* to be :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.EditTrigger.AllEditTriggers`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.closeEditor`.
