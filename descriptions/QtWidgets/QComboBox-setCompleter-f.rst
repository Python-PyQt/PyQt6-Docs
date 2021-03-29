.. sip:method-description::
    :status: todo
    :pysig: 03ee2d73dd36a577acb2780acc6eeb36
    :realsig: (QCompleter*)
    :digest: b820c18446ec7f26bc083e96652b4f15

Sets the *completer* to use instead of the current completer. If *completer* is ``nullptr``, auto completion is disabled.

By default, for an editable combo box, a :sip:ref:`~PyQt6.QtWidgets.QCompleter` that performs case insensitive inline completion is automatically created.

**Note:** The completer is removed when the editable property becomes ``false``, or when the line edit is replaced by a call to :sip:ref:`~PyQt6.QtWidgets.QComboBox.setLineEdit`. Setting a completer on a `QComboBox <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qcombobox>`_ that is not editable will be ignored.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QComboBox.completer`.
