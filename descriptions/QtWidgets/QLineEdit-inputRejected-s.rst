.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: a2770d8e102e83472304aa4f2c70e152

This signal is emitted when the user uses a key that is not considered to be valid input. For example, if using a key results in a validator's :sip:ref:`~PyQt6.QtGui.QValidator.validate` call to return :sip:ref:`~PyQt6.QtGui.QValidator.State.Invalid`. Another case is when trying to enter more characters beyond the maximum length of the line edit.

**Note:** This signal will still be emitted when only a part of the text is accepted. For example, if there is a maximum length set and the clipboard text is longer than the maximum length when it is pasted.
