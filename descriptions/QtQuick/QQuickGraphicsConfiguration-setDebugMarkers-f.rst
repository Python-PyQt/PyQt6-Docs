.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: af115ec2c8813a45d294c902bd7da254

Where applicable, *enable* controls inserting debug markers and object names into the graphics command stream.

Some frameworks, such as Qt Quick 3D, have the ability to annotate the graphics objects they create (buffers, textures) with names and also indicate the beginning and end of render passes in the command buffer. These are then visible in frame captures made with tools like `RenderDoc <https://renderdoc.org/>`_ or XCode.

Graphics APIs where this can be expected to be supported are Vulkan (if VK_EXT_debug_utils is available), Direct 3D 11, and Metal.

Calling this function with *enable* set to true is equivalent to setting the environment variable ``QSG_RHI_PROFILE`` to a non-zero value.

The default value is false.

**Note:** Enabling debug markers may have a performance impact. Shipping applications to production with the flag enabled is not recommended.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration.isDebugMarkersEnabled`.
