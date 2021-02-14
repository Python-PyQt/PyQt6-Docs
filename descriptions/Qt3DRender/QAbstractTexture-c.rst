.. sip:class-description::
    :status: todo
    :brief: A base class to be used to provide textures
    :realname: Qt3DRender::QAbstractTexture
    :digest: 1da7320c30ff6b84d766d46457172bef

A base class to be used to provide textures.

The :sip:ref:`~PyQt6.Qt3DRender.QAbstractTexture` class shouldn't be used directly but rather through one of its subclasses. Each subclass implements a given texture target (2D, 2DArray, 3D, CubeMap ...) Each subclass provides a set of functors for each layer, cube map face and mipmap level. In turn the backend uses those functor to properly fill a corresponding OpenGL texture with data. It is expected the functor does as minimal processing as possible so as not to slow down textures generation and upload. If the content of a texture is the result of a slow procedural generation process, it is recommended not to implement this directly in a functor.

All textures are unique. If you instantiate twice the same texture this will create 2 identical textures on the GPU, no sharing will take place.
