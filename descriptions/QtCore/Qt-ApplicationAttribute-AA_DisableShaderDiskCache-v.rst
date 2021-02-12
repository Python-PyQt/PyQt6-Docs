.. sip:enum-member-description::
    :status: todo
    :value: 27
    :digest: 5a69470da7390880eafd12caa4dcb579

Disables caching of shader program binaries on disk. By default Qt Quick, QPainter's OpenGL backend, and any application using QOpenGLShaderProgram with one of its *addCacheableShaderFromSource* overloads will employ a disk-based program binary cache in either the shared or per-process cache storage location, on systems that support *glProgramBinary()*. In the unlikely event of this being problematic, set this attribute to disable all disk-based caching of shaders.
