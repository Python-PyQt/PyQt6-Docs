.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 1600fdd9fcd3b5e1924677bc061878e8

Returns ``true`` if the OpenGL context of the graph has been successfully initialized. Trying to use a graph when the context initialization has failed typically results in a crash. A common reason for a context initialization failure is lack of sufficient platform support for OpenGL.
