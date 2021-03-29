.. sip:enum-description::
    :status: todo
    :realname: Qt3DRender::QAbstractTexture::CubeMapFace
    :digest: 237dfecf947d482254990c42ea2c5b96

This enum identifies the faces of a cube map texture

**Note:**  should only be used when a behavior needs to be applied to all the faces of a cubemap. This is the case for example when using a cube map as a texture attachment. Using  in the attachment specfication would result in all faces being bound to the attachment point. On the other hand, if a specific face is specified, the attachment would only be using the specified face.
