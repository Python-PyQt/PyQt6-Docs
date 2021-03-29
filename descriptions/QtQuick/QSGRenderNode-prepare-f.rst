.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: faf60edb2102144a6dc6396266d28135

Called from the frame preparation phase. There is a call to this function before each invocation of :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render`.

Unlike :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render`, this function is called before the scenegraph starts recording the render pass for the current frame on the underlying command buffer. This is useful when doing rendering with graphics APIs, such as Vulkan, where copy type of operations will need to be recorded before the render pass.

The default implementation is empty.
