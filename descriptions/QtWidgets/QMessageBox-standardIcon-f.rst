.. sip:method-description::
    :status: todo
    :pysig: 9486ccc22be90a3e67c77ab2a0f802b7
    :realsig: (QMessageBox::Icon)
    :digest: 48a102fe97365ec2e1969e772c6cfe77

Returns the pixmap used for a standard icon. This allows the pixmaps to be used in more complex message boxes. *icon* specifies the required icon, e.g. :sip:ref:`~PyQt6.QtWidgets.QMessageBox.Icon.Question`, :sip:ref:`~PyQt6.QtWidgets.QMessageBox.Icon.Information`, :sip:ref:`~PyQt6.QtWidgets.QMessageBox.Icon.Warning` or :sip:ref:`~PyQt6.QtWidgets.QMessageBox.Icon.Critical`.

Call :sip:ref:`~PyQt6.QtWidgets.QStyle.standardIcon` with :sip:ref:`~PyQt6.QtWidgets.QStyle.StandardPixmap.SP_MessageBoxInformation` etc. instead.
