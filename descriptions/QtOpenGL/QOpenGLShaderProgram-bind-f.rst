.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 2d57bbc3d24ca108f1a54b85729799dc

Binds this shader program to the active `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_ and makes it the current shader program. Any previously bound shader program is released. This is equivalent to calling ``glUseProgram()`` on :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.programId`. Returns ``true`` if the program was successfully bound; false otherwise. If the shader program has not yet been linked, or it needs to be re-linked, this function will call :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.link`.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.link`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.release`.
