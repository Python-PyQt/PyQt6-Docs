.. sip:method-description::
    :status: todo
    :pysig: 70ce07b225801abde2cb8f5bcae9bb3a
    :realsig: (const QString&, int)
    :digest: c774e73e2e330be2cbafeb09193cb6d0

Binds the attribute *name* to the specified *location*. This function can be called before or after the program has been linked. Any attributes that have not been explicitly bound when the program is linked will be assigned locations automatically.

When this function is called after the program has been linked, the program will need to be relinked for the change to take effect.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.attributeLocation`.
