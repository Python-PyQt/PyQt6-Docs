.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 90d9e0cddd5c08cffe98209ae752bedb

This virtual function is called whenever the window contents needs to be painted. Reimplement it in a subclass.

There is no need to call :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.makeCurrent` because this has already been done when this function is called.

Before invoking this function, the context and the framebuffer, if there is one, are bound, and the viewport is set up by a call to glViewport(). No other state is set and no clearing or drawing is performed by the framework.

**Note:** When using a partial update behavior, like ``PartialUpdateBlend``, the output of the previous  call is preserved and, after the additional drawing perfomed in the current invocation of the function, the content is blitted or blended over the content drawn directly to the window in :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintUnderGL`.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.initializeGL`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.resizeGL`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintUnderGL`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintOverGL`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.UpdateBehavior.UpdateBehavior`.
