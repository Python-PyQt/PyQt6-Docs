.. sip:class-description::
    :status: todo
    :brief: Wraps an OpenGL Vertex Array Object
    :digest: 2464e430ec697c60b1a729cd9525550f

The :sip:ref:`~PyQt6.QtOpenGL.QOpenGLVertexArrayObject` class wraps an OpenGL Vertex Array Object.

A Vertex Array Object (VAO) is an OpenGL container object that encapsulates the state needed to specify per-vertex attribute data to the OpenGL pipeline. To put it another way, a VAO remembers the states of buffer objects (see :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer`) and their associated state (e.g. vertex attribute divisors). This allows a very easy and efficient method of switching between OpenGL buffer states for rendering different "objects" in a scene. The :sip:ref:`~PyQt6.QtOpenGL.QOpenGLVertexArrayObject` class is a thin wrapper around an OpenGL VAO.

For the desktop, VAOs are supported as a core feature in OpenGL 3.0 or newer and by the GL_ARB_vertex_array_object for older versions. On OpenGL ES 2, VAOs are provided by the optional GL_OES_vertex_array_object extension. You can check the version of OpenGL with QOpenGLContext::surfaceFormat() and check for the presence of extensions with :sip:ref:`~PyQt6.QtGui.QOpenGLContext.hasExtension`.

As with the other Qt OpenGL classes, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLVertexArrayObject` has a :sip:ref:`~PyQt6.QtOpenGL.QOpenGLVertexArrayObject.create` function to create the underlying OpenGL object. This is to allow the developer to ensure that there is a valid current OpenGL context at the time.

Once you have successfully created a VAO the typical usage pattern is:

* In scene initialization function, for each visual object:

  * Bind the VAO

  * Set vertex data state for this visual object (vertices, normals, texture coordinates etc.)

  * Unbind (\ :sip:ref:`~PyQt6.QtOpenGL.QOpenGLVertexArrayObject.release`) the VAO

* In render function, for each visual object:

  * Bind the VAO (and shader program if needed)

  * Call a glDraw\*() function

  * Unbind (\ :sip:ref:`~PyQt6.QtOpenGL.QOpenGLVertexArrayObject.release`) the VAO

The act of binding the VAO in the render function has the effect of restoring all of the vertex data state setup in the initialization phase. In this way we can set a great deal of state when setting up a VAO and efficiently switch between state sets of objects to be rendered. Using VAOs also allows the OpenGL driver to amortise the validation checks of the vertex data.

**Note:** Vertex Array Objects, like all other OpenGL container objects, are specific to the context for which they were created and cannot be shared amongst a context group.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLVertexArrayObject.Binder`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer`.
