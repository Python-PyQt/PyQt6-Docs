.. sip:method-description::
    :status: todo
    :pysig: 03ee2d73dd36a577acb2780acc6eeb36
    :realsig: (QCompleter*)
    :digest: 807fdeb0a6d50774a68c5310ea2136c4

Sets this line edit to provide auto completions from the completer, *c*. The completion mode is set using :sip:ref:`~PyQt6.QtWidgets.QCompleter.setCompletionMode`.

To use a :sip:ref:`~PyQt6.QtWidgets.QCompleter` with a :sip:ref:`~PyQt6.QtGui.QValidator` or :sip:ref:`~PyQt6.QtWidgets.QLineEdit.inputMask`, you need to ensure that the model provided to :sip:ref:`~PyQt6.QtWidgets.QCompleter` contains valid entries. You can use the :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel` to ensure that the :sip:ref:`~PyQt6.QtWidgets.QCompleter`'s model contains only valid entries.

If *c* == 0,  removes the current completer, effectively disabling auto completion.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QLineEdit.completer`, :sip:ref:`~PyQt6.QtWidgets.QCompleter`.
