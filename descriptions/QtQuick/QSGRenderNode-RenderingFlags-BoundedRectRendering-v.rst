.. sip:enum-member-description::
    :status: todo
    :value: 0x01
    :realname: QSGRenderNode::RenderingFlag::BoundedRectRendering
    :digest: c5e30fae7ab8a4759b92ca7164e3cab7

Indicates that the implementation of :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render` does not render outside the area reported from :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.rect` in item coordinates. Such node implementations can lead to more efficient rendering, depending on the scenegraph backend. For example, the software backend can continue to use the more optimal partial update path when all render nodes in the scene have this flag set.
