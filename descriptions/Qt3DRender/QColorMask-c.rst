.. sip:class-description::
    :status: todo
    :brief: Allows specifying which color components should be written to the currently bound frame buffer
    :realname: Qt3DRender::QColorMask
    :digest: 5bcfd5e92a18f61d6ea4bf53556e9603

Allows specifying which color components should be written to the currently bound frame buffer.

By default, the property for each color component (red, green, blue, alpha) is set to ``true`` which means they will be written to the frame buffer. Setting any of the color component to ``false`` will prevent it from being written into the frame buffer.
