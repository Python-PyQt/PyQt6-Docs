.. sip:class-description::
    :status: todo
    :brief: Encapsulates an OpenGL texture object
    :digest: 738f11a54af20a49b5d12f234b12857a

The :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture` class encapsulates an OpenGL texture object.

:sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture` makes it easy to work with OpenGL textures and the myriad features and targets that they offer depending upon the capabilities of your OpenGL implementation.

The typical usage pattern for :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture` is

* Instantiate the object specifying the texture target type

* Set properties that affect the storage requirements e.g. storage format, dimensions

* Allocate the server-side storage

* Optionally upload pixel data

* Optionally set any additional properties e.g. filtering and border options

* Render with texture or render to texture

In the common case of simply using a :sip:ref:`~PyQt6.QtGui.QImage` as the source of texture pixel data most of the above steps are performed automatically.

::

    // Prepare texture
    QOpenGLTexture *texture = new QOpenGLTexture(QImage(fileName).mirrored());
    texture->setMinificationFilter(QOpenGLTexture::LinearMipMapLinear);
    texture->setMagnificationFilter(QOpenGLTexture::Linear);
    ...
    // Render with texture
    texture->bind();
    glDrawArrays(...);

Note that the :sip:ref:`~PyQt6.QtGui.QImage` is mirrored vertically to account for the fact that OpenGL and :sip:ref:`~PyQt6.QtGui.QImage` use opposite directions for the y axis. Another option would be to transform your texture coordinates.
