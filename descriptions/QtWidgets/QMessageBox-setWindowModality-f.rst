.. sip:method-description::
    :status: todo
    :pysig: 9eab771927fa4a102e69fe10a2c2a408
    :realsig: (Qt::WindowModality)
    :digest: 68f066fb7b020edc5ed9624cc664e75e

This function shadows :sip:ref:`~PyQt6.QtWidgets.QWidget.setWindowModality`.

Sets the modality of the message box to *windowModality*.

On macOS, if the modality is set to :sip:ref:`~PyQt6.QtCore.Qt.WindowModality.WindowModal` and the message box has a parent, then the message box will be a :sip:ref:`~PyQt6.QtCore.Qt.WindowFlags.Sheet`, otherwise the message box will be a standard dialog.
