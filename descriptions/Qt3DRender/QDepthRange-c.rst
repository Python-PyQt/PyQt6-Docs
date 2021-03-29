.. sip:class-description::
    :status: todo
    :brief: Enables remapping depth values written into the depth buffer
    :realname: Qt3DRender::QDepthRange
    :digest: cc0d6c286cea62209ba49fc481edd131

Enables remapping depth values written into the depth buffer.

By default, OpenGL writes scene depth information into the depth buffer in the range [0.0, 1.0] with 0.0 corresponding to the near clip plane and 1.0 to the far clip plane. :sip:ref:`~PyQt6.Qt3DRender.QDepthRange` allows mapping these values into a different range so parts of the scene are always rendered in front of or behind other parts. Valid values for near and far are between 0 and 1.
