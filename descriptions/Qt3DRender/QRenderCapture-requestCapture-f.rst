.. sip:method-description::
    :status: todo
    :pysig: 5dc66b078b6f37b5e65a7e116c6bf6a8
    :realname: Qt3DRender::QRenderCapture::requestCapture
    :realsig: ()
    :digest: 44fb36af0b183a6f0a1eb6918f259d96

Used to request render capture. Only one render capture result is produced per :sip:ref:`~PyQt6.Qt3DRender.QRenderCapture.requestCapture` call even if the frame graph has multiple leaf nodes. The function returns a QRenderCaptureReply object, which receives the captured image when it is done. The user is responsible for deallocating the returned object by calling deleterLater().
