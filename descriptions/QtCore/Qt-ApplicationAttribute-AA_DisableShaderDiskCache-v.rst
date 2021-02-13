.. sip:enum-member-description::
    :status: todo
    :value: 27
    :digest: 9e1197e5f829eb4e94d0c67106cb5d95

Disables caching of shader program binaries on disk. By default Qt Quick, :sip:ref:`~PyQt6.QtGui.QPainter`'s OpenGL backend, and any application using :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram` with one of its *addCacheableShaderFromSource* overloads will employ a disk-based program binary cache in either the shared or per-process cache storage location, on systems that support *glProgramBinary()*. In the unlikely event of this being problematic, set this attribute to disable all disk-based caching of shaders.
