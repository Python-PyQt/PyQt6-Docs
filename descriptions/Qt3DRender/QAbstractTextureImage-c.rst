.. sip:class-description::
    :status: todo
    :brief: Encapsulates the necessary information to create an OpenGL texture image
    :realname: Qt3DRender::QAbstractTextureImage
    :digest: b4a50a133ca787cef6b78c5deaf072ed

Encapsulates the necessary information to create an OpenGL texture image.

:sip:ref:`~PyQt6.Qt3DRender.QAbstractTextureImage` should be used as the means of providing image data to a QAbstractTexture. It contains the necessary information: mipmap level, layer, cube face load at the proper place data into an OpenGL texture.

The actual data is provided through a QTextureImageDataGenerator that will be executed by Aspect jobs in the backend. :sip:ref:`~PyQt6.Qt3DRender.QAbstractTextureImage` should be subclassed to provide a functor and eventual additional properties needed by the functor to load actual data.

**Note:** : :sip:ref:`~PyQt6.Qt3DRender.QAbstractTextureImage` should never be shared. Expect crashes, undefined behavior at best if this rule is not respected.
