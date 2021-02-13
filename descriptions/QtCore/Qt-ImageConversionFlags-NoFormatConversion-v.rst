.. sip:enum-member-description::
    :status: todo
    :value: 0x00000200
    :realname: Qt::ImageConversionFlag::NoFormatConversion
    :digest: 21a3d475746e521773e01b7cd0ec2fff

Don't do any format conversions on the image. Can be useful when converting a :sip:ref:`~PyQt6.QtGui.QImage` to a :sip:ref:`~PyQt6.QtGui.QPixmap` for a one-time rendering operation for example. Note that a :sip:ref:`~PyQt6.QtGui.QPixmap` not in the preferred format will be much slower as a paint device.
