.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 8d4ef159d6da0dc95b8c493a512401c6

Links together the shaders that were added to this program with :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addShader`. Returns ``true`` if the link was successful or false otherwise. If the link failed, the error messages can be retrieved with :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.log`.

Subclasses can override this function to initialize attributes and uniform variables for use in specific shader programs.

If the shader program was already linked, calling this function again will force it to be re-linked.

When shaders were added to this program via :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addCacheableShaderFromSourceCode` or :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addCacheableShaderFromSourceFile`, program binaries are supported, and a cached binary is available on disk, actual compilation and linking are skipped. Instead,  will initialize the program with the binary blob via glProgramBinary(). If there is no cached version of the program or it was generated with a different driver version, the shaders will be compiled from source and the program will get linked normally. This allows seamless upgrading of the graphics drivers, without having to worry about potentially incompatible binary formats.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addShader`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.log`.
