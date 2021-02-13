.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: fa8be860ae8ce9b011921d0558e7894c

Call this function when the FBO should be rendered again.

This function can be called from :sip:ref:`~PyQt6.QtQuick.QQuickFramebufferObject.Renderer.render` to force the FBO to be rendered again before the next frame.

**Note:** This function should be used from inside the renderer. To update the item on the GUI thread, use QQuickFramebufferObject::update().
