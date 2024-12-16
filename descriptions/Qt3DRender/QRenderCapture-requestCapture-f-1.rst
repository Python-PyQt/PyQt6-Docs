.. sip:method-description::
    :status: todo
    :pysig: c8a8477456baa52634d120c5f56b418b
    :realname: Qt3DRender::QRenderCapture::requestCapture
    :realsig: (int)
    :digest: 6ad2c83e195101705bed020a98ea4c42

Used to request render capture. User can specify a *captureId* to identify the request. The requestId does not have to be unique. Only one render capture result is produced per :sip:ref:`~PyQt6.Qt3DRender.QRenderCapture.requestCapture` call even if the frame graph has multiple leaf nodes. The function returns a QRenderCaptureReply object, which receives the captured image when it is done. The user is responsible for deallocating the returned object by calling deleteLater().
