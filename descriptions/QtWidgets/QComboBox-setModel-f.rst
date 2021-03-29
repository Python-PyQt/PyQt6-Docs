.. sip:method-description::
    :status: todo
    :pysig: b1398307ea89da5fe868fb6740f9bc55
    :realsig: (QAbstractItemModel*)
    :digest: 68baf88a50f69941b410a42692489dd6

Sets the model to be *model*. *model* must not be ``nullptr``. If you want to clear the contents of a model, call :sip:ref:`~PyQt6.QtWidgets.QComboBox.clear`.

**Note:** If the combobox is editable, then the *model* will also be set on the completer of the line edit.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QComboBox.model`, :sip:ref:`~PyQt6.QtWidgets.QComboBox.clear`, :sip:ref:`~PyQt6.QtWidgets.QComboBox.setCompleter`.
