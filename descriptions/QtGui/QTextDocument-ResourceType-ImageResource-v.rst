.. sip:enum-member-description::
    :status: todo
    :value: 2
    :digest: 5152ad7f375e6fbaf71b58a01b3b3195

The resource contains image data. Currently supported data types are :sip:ref:`~PyQt6.QtCore.QMetaType.Type.QPixmap` and :sip:ref:`~PyQt6.QtCore.QMetaType.Type.QImage`. If the corresponding variant is of type :sip:ref:`~PyQt6.QtCore.QMetaType.Type.QByteArray` then Qt attempts to load the image using :sip:ref:`~PyQt6.QtGui.QImage.loadFromData`. :sip:ref:`~PyQt6.QtCore.QMetaType.Type.QIcon` is currently not supported. The icon needs to be converted to one of the supported types first, for example using :sip:ref:`~PyQt6.QtGui.QIcon.pixmap`.
