.. sip:method-description::
    :status: todo
    :pysig: abc8395ac988b73ae58e9cbd6136c7ae
    :realsig: (const QModelIndex&)
    :digest: a9a6fb2225953c7e4675a089a7fa06f6

To use a custom widget for the final column when you select an item overload this function and return a widget. *index* is the root index that will be assigned to the view.

Return the new view. :sip:ref:`~PyQt6.QtWidgets.QColumnView` will automatically take ownership of the widget.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QColumnView.setPreviewWidget`.
