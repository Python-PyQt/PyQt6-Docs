.. sip:method-description::
    :status: todo
    :pysig: 56b49ee09cd5bb686073d6baf0622c7e
    :realname: Qt3DRender::QRenderCapture::requestCapture
    :realsig: (const QRect&)
    :digest: 0bb5a14f51155377a4b9c1db7da56a70

Used to request render capture from a specified *rect*. Only one render capture result is produced per  call even if the frame graph has multiple leaf nodes. The function returns a QRenderCaptureReply object, which receives the captured image when it is done. The user is responsible for deallocating the returned object by calling deleteLater().
