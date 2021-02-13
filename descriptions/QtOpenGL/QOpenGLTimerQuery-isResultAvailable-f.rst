.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 2cf0d460cb2852a385459cc66a850555

Returns ``true`` if the OpenGL timer query result is available.

This function is non-blocking and ideally should be used to check for the availability of the query result before calling :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery.waitForResult`.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery.waitForResult`.
