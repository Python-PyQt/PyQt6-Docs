.. sip:method-description::
    :status: todo
    :pysig: d0846ee3d37e010437eeff65a74015a7
    :realsig: (QOpenGLShader::ShaderType,QOpenGLContext*)
    :digest: d5b701bfd6b121bc13687316c53738c2

Returns ``true`` if shader programs of type *type* are supported on this system; false otherwise.

The *context* is used to resolve the GLSL extensions. If *context* is ``nullptr``, then :sip:ref:`~PyQt6.QtGui.QOpenGLContext.currentContext` is used.
