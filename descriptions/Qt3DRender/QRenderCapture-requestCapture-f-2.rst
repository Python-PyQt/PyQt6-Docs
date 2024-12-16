.. sip:method-description::
    :status: todo
    :pysig: 56b49ee09cd5bb686073d6baf0622c7e
    :realname: Qt3DRender::QRenderCapture::requestCapture
    :realsig: (const QRect&)
    :digest: da7085c42df3d08bb3120930c9b5f999

Used to request render capture from a specified *rect*. Only one render capture result is produced per :sip:ref:`~PyQt6.Qt3DRender.QRenderCapture.requestCapture` call even if the frame graph has multiple leaf nodes. The function returns a QRenderCaptureReply object, which receives the captured image when it is done. The user is responsible for deallocating the returned object by calling deleteLater().
