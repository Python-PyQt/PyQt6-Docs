.. sip:method-description::
    :status: todo
    :pysig: dd9861cc8684c775152f94a62ebafc36
    :realsig: (QAbstractItemView*)
    :digest: 7249652b5956136b9196a44eb2961ffb

Sets the view to be used in the combobox popup to the given *itemView*. The combobox takes ownership of the view.

Note: If you want to use the convenience views (like :sip:ref:`~PyQt6.QtWidgets.QListWidget`, :sip:ref:`~PyQt6.QtWidgets.QTableWidget` or :sip:ref:`~PyQt6.QtWidgets.QTreeWidget`), make sure to call :sip:ref:`~PyQt6.QtWidgets.QComboBox.setModel` on the combobox with the convenience widgets model before calling this function.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QComboBox.view`.
