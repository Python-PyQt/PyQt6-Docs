.. sip:method-description::
    :status: todo
    :pysig: 4b99ff73a8a869319570237b5c57ab03
    :realsig: (QString&) const
    :digest: f5c9018a641b0f0126ac9e3bbf39028a

This virtual function is called by the :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox` if the *input* is not validated to :sip:ref:`~PyQt6.QtGui.QValidator.State.Acceptable` when Return is pressed or :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox.interpretText` is called. It will try to change the text so it is valid. Reimplemented in the various subclasses.
