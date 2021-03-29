.. sip:class-description::
    :status: todo
    :brief: Encapsulates blending information: specifies how the incoming values (what's going to be drawn) are going to affect the existing values (what is already drawn)
    :realname: Qt3DRender::QBlendEquationArguments
    :digest: e53d3ddef3a36cf2f659d7d031b5ba65

Encapsulates blending information: specifies how the incoming values (what's going to be drawn) are going to affect the existing values (what is already drawn).

OpenGL pre-3.0: Set the same blend state for all draw buffers (one :sip:ref:`~PyQt6.Qt3DRender.QBlendEquationArguments`) OpenGL 3.0-pre4.0: Set the same blend state for all draw buffers, but can disable blending for particular buffers (one :sip:ref:`~PyQt6.Qt3DRender.QBlendEquationArguments` for setting glBlendFunc, n QBlendEquationArgumentss for enabling/disabling Draw Buffers) OpenGL 4.0+: Can set blend state individually for each draw buffer.
