.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: a98b149afa49bd0ce13e7dbfdfae25bb

Binds this vertex array object to the OpenGL binding point. From this point on and until :sip:ref:`~PyQt6.QtOpenGL.QOpenGLVertexArrayObject.release` is called or another vertex array object is bound, any modifications made to vertex data state are stored inside this vertex array object.

If another vertex array object is then bound you can later restore the set of state associated with this object by calling  on this object once again. This allows efficient changes between vertex data states in rendering functions.
