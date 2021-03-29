.. sip:class-description::
    :status: todo
    :brief: Frame graph node for render capture
    :realname: Qt3DRender::QRenderCapture
    :digest: e3e304b4be3b88140afe70348dbff8ee

Frame graph node for render capture.

The :sip:ref:`~PyQt6.Qt3DRender.QRenderCapture` is used to capture rendering into an image at any render stage. Capturing must be initiated by the user and one image is returned per capture request. User can issue multiple render capture requests simultaniously, but only one request is served per :sip:ref:`~PyQt6.Qt3DRender.QRenderCapture` instance per frame.
