.. sip:method-description::
    :status: todo
    :pysig: fb51eb2740812f4466a824231ed4bce3
    :realsig: ()
    :digest: d4058299bdf2bc2d9aef7cb87c3c254d

Grabs the contents of the window and returns it as an image.

It is possible to call the grabWindow() function when the window is not visible. This requires that the window is :sip:ref:`~PyQt6.QtGui.QWindow.create` and has a valid size and that no other :sip:ref:`~PyQt6.QtQuick.QQuickWindow` instances are rendering in the same process.

**Note:** When using this window in combination with :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl`, the result of this function is an empty image, unless the ``software`` backend is in use. This is because when redirecting the output to an application-managed graphics resource (such as, a texture) by using :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl` and :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setRenderTarget`, the application is better suited for managing and executing an eventual read back operation, since it is in full control of the resource to begin with.

**Warning:** Calling this function will cause performance problems.

**Warning:** This function can only be called from the GUI thread.
