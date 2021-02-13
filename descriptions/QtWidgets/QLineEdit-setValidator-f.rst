.. sip:method-description::
    :status: todo
    :pysig: 95ffcd03961616094eaee0ed59713003
    :realsig: (const QValidator*)
    :digest: 5ea4bbf7031fefda11d826ce13903765

Sets the validator for values of line edit to *v*.

The line edit's :sip:ref:`~PyQt6.QtWidgets.QLineEdit.returnPressed` and :sip:ref:`~PyQt6.QtWidgets.QLineEdit.editingFinished` signals will only be emitted if *v* validates the line edit's content as :sip:ref:`~PyQt6.QtGui.QValidator.State.Acceptable`. The user may change the content to any :sip:ref:`~PyQt6.QtGui.QValidator.State.Intermediate` value during editing, but will be prevented from editing the text to a value that *v* validates as :sip:ref:`~PyQt6.QtGui.QValidator.State.Invalid`.

This allows you to constrain the text that shall finally be entered when editing is done, while leaving users with enough freedom to edit the text from one valid state to another.

If *v* == 0,  removes the current input validator. The initial setting is to have no input validator (i.e. any input is accepted up to :sip:ref:`~PyQt6.QtWidgets.QLineEdit.maxLength`).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QLineEdit.validator`, :sip:ref:`~PyQt6.QtWidgets.QLineEdit.hasAcceptableInput`, :sip:ref:`~PyQt6.QtGui.QIntValidator`, :sip:ref:`~PyQt6.QtGui.QDoubleValidator`, :sip:ref:`~PyQt6.QtGui.QRegularExpressionValidator`.
