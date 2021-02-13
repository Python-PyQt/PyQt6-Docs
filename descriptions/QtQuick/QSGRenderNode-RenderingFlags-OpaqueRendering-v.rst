.. sip:enum-member-description::
    :status: todo
    :value: 0x04
    :realname: QSGRenderNode::RenderingFlag::OpaqueRendering
    :digest: 0d3e4a0673fa757842a2c20b283df7b6

Indicates that the implementation of :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render` writes out opaque pixels for the entire area reported from :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.rect`. By default the renderers must assume that :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render` can also output semi or fully transparent pixels. Setting this flag can improve performance in some cases.
