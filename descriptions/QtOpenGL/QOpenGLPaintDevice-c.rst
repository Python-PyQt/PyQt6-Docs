.. sip:class-description::
    :status: todo
    :brief: Enables painting to an OpenGL context using QPainter
    :digest: 1d8b3456343b5d95c56a813df12e10e9

The :sip:ref:`~PyQt6.QtOpenGL.QOpenGLPaintDevice` class enables painting to an OpenGL context using :sip:ref:`~PyQt6.QtGui.QPainter`.

The :sip:ref:`~PyQt6.QtOpenGL.QOpenGLPaintDevice` uses the **current** QOpenGL context to render :sip:ref:`~PyQt6.QtGui.QPainter` draw commands. The context is captured upon construction. It requires support for OpenGL (ES) 2.0 or higher.

.. _qopenglpaintdevice-performance:

Performance
-----------

The :sip:ref:`~PyQt6.QtOpenGL.QOpenGLPaintDevice` is almost always hardware accelerated and has the potential of being much faster than software rasterization. However, it is more sensitive to state changes, and therefore requires the drawing commands to be carefully ordered to achieve optimal performance.

.. _qopenglpaintdevice-antialiasing-and-quality:

Antialiasing and Quality
------------------------

Antialiasing in the OpenGL paint engine is done using multisampling. Most hardware require significantly more memory to do multisampling and the resulting quality is not on par with the quality of the software paint engine. The OpenGL paint engine's strength lies in its performance, not its visual rendering quality.

.. _qopenglpaintdevice-state-changes:

State Changes
-------------

When painting to a :sip:ref:`~PyQt6.QtOpenGL.QOpenGLPaintDevice` using :sip:ref:`~PyQt6.QtGui.QPainter`, the state of the current OpenGL context will be altered by the paint engine to reflect its needs. Applications should not rely upon the OpenGL state being reset to its original conditions, particularly the current shader program, OpenGL viewport, texture units, and drawing modes.

.. _qopenglpaintdevice-mixing-qpainter-and-opengl:

Mixing QPainter and OpenGL
--------------------------

When intermixing :sip:ref:`~PyQt6.QtGui.QPainter` and OpenGL, it is important to notify :sip:ref:`~PyQt6.QtGui.QPainter` that the OpenGL state may have been cluttered so it can restore its internal state. This is achieved by calling :sip:ref:`~PyQt6.QtGui.QPainter.beginNativePainting` before starting the OpenGL rendering and calling :sip:ref:`~PyQt6.QtGui.QPainter.endNativePainting` after finishing.

.. seealso:: `OpenGL Window Example <https://doc.qt.io/qt-6/qtopengl-openglwindow-example.html>`_.
