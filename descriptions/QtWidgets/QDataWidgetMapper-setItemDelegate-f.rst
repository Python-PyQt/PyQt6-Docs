.. sip:method-description::
    :status: todo
    :pysig: 0a9c57ae6d41cc71509c5686744bb861
    :realsig: (QAbstractItemDelegate*)
    :digest: 06876cfa8268e84797138677ef8bc379

Sets the item delegate to *delegate*. The delegate will be used to write data from the model into the widget and from the widget to the model, using :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.setEditorData` and :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.setModelData`.

Any existing delegate will be removed, but not deleted. :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper` does not take ownership of *delegate*.

The delegate also decides when to apply data and when to change the editor, using :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.commitData` and :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.closeEditor`.

**Warning:** You should not share the same instance of a delegate between widget mappers or views. Doing so can cause incorrect or unintuitive editing behavior since each view connected to a given delegate may receive the :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.closeEditor` signal, and attempt to access, modify or close an editor that has already been closed.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper.itemDelegate`.
