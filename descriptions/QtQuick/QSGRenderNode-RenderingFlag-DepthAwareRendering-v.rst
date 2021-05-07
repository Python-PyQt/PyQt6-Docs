.. sip:enum-member-description::
    :status: todo
    :value: 0x02
    :digest: 0ecbe56a461ca5103669c19582463795

Indicates that the implementations of :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render` conforms to scenegraph expectations by only generating a Z value of 0 in scene coordinates which is then transformed by the matrices retrieved from :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.RenderState.projectionMatrix` and :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.matrix`, as described in the notes for :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render`. Such node implementations can lead to more efficient rendering, depending on the scenegraph backend. For example, the batching OpenGL renderer can continue to use a more optimal path when all render nodes in the scene have this flag set.
