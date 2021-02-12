.. sip:enum-member-description::
    :status: todo
    :value: 0x00000100
    :realname: Qt::ImageConversionFlag::NoOpaqueDetection
    :digest: e4665d76d52c428d0860edbf5b1a9768

Do not check whether the image contains non-opaque pixels. Use this if you know that the image is semi-transparent and you want to avoid the overhead of checking the pixels in the image until a non-opaque pixel is found, or if you want the pixmap to retain an alpha channel for some other reason. If the image has no alpha channel this flag has no effect.
