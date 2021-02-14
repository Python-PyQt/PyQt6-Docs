.. sip:class-description::
    :status: todo
    :brief: Enables an additional OpenGL clipping plane that can be in shaders using gl_ClipDistance
    :realname: Qt3DRender::QClipPlane
    :digest: dfdab15850a97e14b2438bcf048fd809

Enables an additional OpenGL clipping plane that can be in shaders using gl_ClipDistance.

By default, OpenGL supports up to 8 additional clipping planes. Qt3DCore::QClipPlane allows to enable one of these additional planes. These planes can then be manipulated in the shaders using gl_ClipDistance[i] where i varies between 0 and 7. The underlying implementation may support more than 8 clip planes, but it is not guaranteed.
