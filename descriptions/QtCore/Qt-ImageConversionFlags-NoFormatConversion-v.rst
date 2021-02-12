.. sip:enum-member-description::
    :status: todo
    :value: 0x00000200
    :realname: Qt::ImageConversionFlag::NoFormatConversion
    :digest: dce808cb6cb3266b0fd82ed5e5d94dcb

Don't do any format conversions on the image. Can be useful when converting a QImage to a QPixmap for a one-time rendering operation for example. Note that a QPixmap not in the preferred format will be much slower as a paint device.
