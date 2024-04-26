.. sip:method-description::
    :status: todo
    :pysig: 95ffcd03961616094eaee0ed59713003
    :realsig: (const QValidator*)
    :digest: 711510ea2b48d3f5dc9ada15719f219b

Sets the validator for values of line edit to *v*.

The line edit's :sip:ref:`~PyQt6.QtWidgets.QLineEdit.returnPressed` and :sip:ref:`~PyQt6.QtWidgets.QLineEdit.editingFinished` signals will only be emitted if *v* validates the line edit's content as :sip:ref:`~PyQt6.QtGui.QValidator.State.Acceptable`. The user may change the content to any :sip:ref:`~PyQt6.QtGui.QValidator.State.Intermediate` value during editing, but will be prevented from editing the text to a value that *v* validates as :sip:ref:`~PyQt6.QtGui.QValidator.State.Invalid`.

This allows you to constrain the text that will be stored when editing is done while leaving users with enough freedom to edit the text from one valid state to another.

To remove the current input validator, pass ``nullptr``. The initial setting is to have no input validator (any input is accepted up to :sip:ref:`~PyQt6.QtWidgets.QLineEdit.maxLength`).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QLineEdit.validator`, :sip:ref:`~PyQt6.QtWidgets.QLineEdit.hasAcceptableInput`, :sip:ref:`~PyQt6.QtGui.QIntValidator`, :sip:ref:`~PyQt6.QtGui.QDoubleValidator`, :sip:ref:`~PyQt6.QtGui.QRegularExpressionValidator`.
