.. sip:enum-member-description::
    :status: todo
    :value: 11
    :digest: abf88f93dda1dbb17597a3c7b5d19be9

The resource is a pointer to the currently active render command encoder object used by the scenegraph, when applicable. For example, a ``MTLRenderCommandEncoder \*``. This object has limited validity, and is only valid while the scene graph is recording a render pass for the next frame. This value was introduced in Qt 5.14.
