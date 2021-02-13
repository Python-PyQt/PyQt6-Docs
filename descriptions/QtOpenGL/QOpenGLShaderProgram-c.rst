.. sip:class-description::
    :status: todo
    :brief: Allows OpenGL shader programs to be linked and used
    :digest: 3433bc449fe7116aa7178278bb89e2a3

The :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram` class allows OpenGL shader programs to be linked and used.

.. _qopenglshaderprogram-introduction:

Introduction
------------

This class supports shader programs written in the OpenGL Shading Language (GLSL) and in the OpenGL/ES Shading Language (GLSL/ES).

:sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader` and :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram` shelter the programmer from the details of compiling and linking vertex and fragment shaders.

The following example creates a vertex shader program using the supplied source ``code``. Once compiled and linked, the shader program is activated in the current `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_ by calling :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.bind`:

.. literalinclude:: ../../../snippets/qtbase-src-opengl-doc-snippets-code-src_gui_qopenglshaderprogram.py
    :lines: 63-70

.. _qopenglshaderprogram-writing-portable-shaders:

Writing Portable Shaders
------------------------

Shader programs can be difficult to reuse across OpenGL implementations because of varying levels of support for standard vertex attributes and uniform variables. In particular, GLSL/ES lacks all of the standard variables that are present on desktop OpenGL systems: ``gl_Vertex``, ``gl_Normal``, ``gl_Color``, and so on. Desktop OpenGL lacks the variable qualifiers ``highp``, ``mediump``, and ``lowp``.

The :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram` class makes the process of writing portable shaders easier by prefixing all shader programs with the following lines on desktop OpenGL:

::

    #define highp
    #define mediump
    #define lowp

This makes it possible to run most GLSL/ES shader programs on desktop systems. The programmer should restrict themselves to just features that are present in GLSL/ES, and avoid standard variable names that only work on the desktop.

.. _qopenglshaderprogram-simple-shader-example:

Simple Shader Example
---------------------

.. literalinclude:: ../../../snippets/qtbase-src-opengl-doc-snippets-code-src_gui_qopenglshaderprogram.py
    :lines: 74-92

With the above shader program active, we can draw a green triangle as follows:

.. literalinclude:: ../../../snippets/qtbase-src-opengl-doc-snippets-code-src_gui_qopenglshaderprogram.py
    :lines: 96-114

.. _qopenglshaderprogram-binary-shaders-and-programs:

Binary Shaders and Programs
---------------------------

Binary shaders may be specified using ``glShaderBinary()`` on the return value from :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader.shaderId`. The :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader` instance containing the binary can then be added to the shader program with :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addShader` and linked in the usual fashion with :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.link`.

Binary programs may be specified using ``glProgramBinaryOES()`` on the return value from :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.programId`. Then the application should call :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.link`, which will notice that the program has already been specified and linked, allowing other operations to be performed on the shader program. The shader program's id can be explicitly created using the :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.create` function.

.. _qopenglshaderprogram-caching-program-binaries:

Caching Program Binaries
........................

As of Qt 5.9, support for caching program binaries on disk is built in. To enable this, switch to using :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addCacheableShaderFromSourceCode` and :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addCacheableShaderFromSourceFile`. With an OpenGL ES 3.x context or support for ``GL_ARB_get_program_binary``, this will transparently cache program binaries under :sip:ref:`~PyQt6.QtCore.QStandardPaths.StandardLocation.GenericCacheLocation` or :sip:ref:`~PyQt6.QtCore.QStandardPaths.StandardLocation.CacheLocation`. When support is not available, calling the cacheable function variants is equivalent to the normal ones.

**Note:** Some drivers do not have any binary formats available, even though they advertise the extension or offer OpenGL ES 3.0. In this case program binary support will be disabled.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader`.
