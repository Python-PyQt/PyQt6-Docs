.. sip:class-description::
    :status: todo
    :brief: Provides Image access to shader programs
    :realname: Qt3DRender::QShaderImage
    :digest: 3b0777fff303d08a0cd5443f91232202

Provides Image access to shader programs.

To make the content of textures available for read and write operations in a shader, they need to exposed as :sip:ref:`~PyQt6.Qt3DRender.QShaderImage`. Textures can be composed of several mip levels, layers and faces. Additionally declaring a :sip:ref:`~PyQt6.Qt3DRender.QShaderImage` allows specifying which level, layer or face of the texture content we want to access.

:sip:ref:`~PyQt6.Qt3DRender.QShaderImage` has to be assigned as a QParameter's value and reference a valid :sip:ref:`~PyQt6.Qt3DRender.QAbstractTexture` to work properly.

If the referenced texture is a one-dimensional array, two-dimensional array, three-dimensional, cube map, cube map array, or two-dimensional multisample array texture, it is possible to bind either the entire texture level or a single layer or face of the texture level. This can be controlled with the :sip:ref:`~PyQt6.Qt3DRender.QShaderImage.layered` property.

Support for :sip:ref:`~PyQt6.Qt3DRender.QShaderImage` is only supported with OpenGL 4 and partially with OpenGL ES 3.1 and 3.2.

OpenGL 4 supports the following image types:

+-----------------+--------------------------------------------+----------------------------+
| GLSL Type       | OpenGL Type Enum                           | Texture Type               |
+=================+============================================+============================+
| image1D         | GL_IMAGE_1D                                | QTexture1D                 |
+-----------------+--------------------------------------------+----------------------------+
| image2D         | GL_IMAGE_2D                                | QTexture2D                 |
+-----------------+--------------------------------------------+----------------------------+
| image3D         | GL_IMAGE_3D                                | QTexture3D                 |
+-----------------+--------------------------------------------+----------------------------+
| image2DRect     | GL_IMAGE_2D_RECT                           | QTextureRectangle          |
+-----------------+--------------------------------------------+----------------------------+
| imageCube       | GL_IMAGE_CUBE                              | QTextureCubeMap            |
+-----------------+--------------------------------------------+----------------------------+
| imageBuffer     | GL_IMAGE_BUFFER                            | QTextureBuffer             |
+-----------------+--------------------------------------------+----------------------------+
| image1DArray    | GL_IMAGE_1D_ARRAY                          | QTexture1DArray            |
+-----------------+--------------------------------------------+----------------------------+
| image2DArray    | GL_IMAGE_2D_ARRAY                          | QTexture2DArray            |
+-----------------+--------------------------------------------+----------------------------+
| imageCubeArray  | GL_IMAGE_CUBE_MAP_ARRAY                    | QTextureCubeMapArray       |
+-----------------+--------------------------------------------+----------------------------+
| image2DMS       | GL_IMAGE_2D_MULTISAMPLE                    | QTexture2DMultisample      |
+-----------------+--------------------------------------------+----------------------------+
| image2DMSArray  | GL_IMAGE_2D_MULTISAMPLE_ARRAY              | QTexture2DMultisampleArray |
+-----------------+--------------------------------------------+----------------------------+
| iimage1D        | GL_INT_IMAGE_1D                            | QTexture1D                 |
+-----------------+--------------------------------------------+----------------------------+
| iimage2D        | GL_INT_IMAGE_2D                            | QTexture2D                 |
+-----------------+--------------------------------------------+----------------------------+
| iimage3D        | GL_INT_IMAGE_3D                            | QTexture3D                 |
+-----------------+--------------------------------------------+----------------------------+
| iimage2DRect    | GL_INT_IMAGE_2D_RECT                       | QTextureRectangle          |
+-----------------+--------------------------------------------+----------------------------+
| iimageCube      | GL_INT_IMAGE_CUBE                          | QTextureCubeMap            |
+-----------------+--------------------------------------------+----------------------------+
| iimageBuffer    | GL_INT_IMAGE_BUFFER                        | QTextureBuffer             |
+-----------------+--------------------------------------------+----------------------------+
| iimage1DArray   | GL_INT_IMAGE_1D_ARRAY                      | QTexture1DArray            |
+-----------------+--------------------------------------------+----------------------------+
| iimage2DArray   | GL_INT_IMAGE_2D_ARRAY                      | QTexture2DArray            |
+-----------------+--------------------------------------------+----------------------------+
| iimageCubeArray | GL_INT_IMAGE_CUBE_MAP_ARRAY                | QTextureCubeMapArray       |
+-----------------+--------------------------------------------+----------------------------+
| iimage2DMS      | GL_INT_IMAGE_2D_MULTISAMPLE                | QTexture2DMultisample      |
+-----------------+--------------------------------------------+----------------------------+
| iimage2DMSArray | GL_INT_IMAGE_2D_MULTISAMPLE_ARRAY          | QTexture2DMultisampleArray |
+-----------------+--------------------------------------------+----------------------------+
| uimage1D        | GL_UNSIGNED_INT_IMAGE_1D                   | QTexture1D                 |
+-----------------+--------------------------------------------+----------------------------+
| uimage2D        | GL_UNSIGNED_INT_IMAGE_2D                   | QTexture2D                 |
+-----------------+--------------------------------------------+----------------------------+
| uimage3D        | GL_UNSIGNED_INT_IMAGE_3D                   | QTexture3D                 |
+-----------------+--------------------------------------------+----------------------------+
| uimage2DRect    | GL_UNSIGNED_INT_IMAGE_2D_RECT              | QTextureRectangle          |
+-----------------+--------------------------------------------+----------------------------+
| uimageCube      | GL_UNSIGNED_INT_IMAGE_CUBE                 | QTextureCubeMap            |
+-----------------+--------------------------------------------+----------------------------+
| uimageBuffer    | GL_UNSIGNED_INT_IMAGE_BUFFER               | QTextureBuffer             |
+-----------------+--------------------------------------------+----------------------------+
| uimage1DArray   | GL_UNSIGNED_INT_IMAGE_1D_ARRAY             | QTexture1DArray            |
+-----------------+--------------------------------------------+----------------------------+
| uimage2DArray   | GL_UNSIGNED_INT_IMAGE_2D_ARRAY             | QTexture2DArray            |
+-----------------+--------------------------------------------+----------------------------+
| uimageCubeArray | GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY       | QTextureCubeMapArray       |
+-----------------+--------------------------------------------+----------------------------+
| uimage2DMS      | GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE       | QTexture2DMultisample      |
+-----------------+--------------------------------------------+----------------------------+
| uimage2DMSArray | GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_ARRAY | QTexture2DMultisampleArray |
+-----------------+--------------------------------------------+----------------------------+

OpenGL ES 3.1 supports the following image types:

+---------------+--------------------------------+-----------------+
| GLSL Type     | OpenGL Type Enum               | Texture Type    |
+===============+================================+=================+
| image2D       | GL_IMAGE_2D                    | QTexture2D      |
+---------------+--------------------------------+-----------------+
| image3D       | GL_IMAGE_3D                    | QTexture3D      |
+---------------+--------------------------------+-----------------+
| imageCube     | GL_IMAGE_CUBE                  | QTextureCubeMap |
+---------------+--------------------------------+-----------------+
| image2DArray  | GL_IMAGE_2D_ARRAY              | QTexture2DArray |
+---------------+--------------------------------+-----------------+
| iimage2D      | GL_INT_IMAGE_2D                | QTexture2D      |
+---------------+--------------------------------+-----------------+
| iimage3D      | GL_INT_IMAGE_3D                | QTexture3D      |
+---------------+--------------------------------+-----------------+
| iimageCube    | GL_INT_IMAGE_CUBE              | QTextureCubeMap |
+---------------+--------------------------------+-----------------+
| iimage2DArray | GL_INT_IMAGE_2D_ARRAY          | QTexture2DArray |
+---------------+--------------------------------+-----------------+
| uimage2D      | GL_UNSIGNED_INT_IMAGE_2D       | QTexture2D      |
+---------------+--------------------------------+-----------------+
| uimage3D      | GL_UNSIGNED_INT_IMAGE_3D       | QTexture3D      |
+---------------+--------------------------------+-----------------+
| uimageCube    | GL_UNSIGNED_INT_IMAGE_CUBE     | QTextureCubeMap |
+---------------+--------------------------------+-----------------+
| uimage2DArray | GL_UNSIGNED_INT_IMAGE_2D_ARRAY | QTexture2DArray |
+---------------+--------------------------------+-----------------+

OpenGL ES 3.2 supports all of the OpenGL ES 3.1 image types as well as the following:

+-----------------+--------------------------------------+----------------------+
| GLSL Type       | OpenGL Type Enum                     | Texture Type         |
+=================+======================================+======================+
| imageBuffer     | GL_IMAGE_BUFFER                      | QTextureBuffer       |
+-----------------+--------------------------------------+----------------------+
| imageCubeArray  | GL_IMAGE_CUBE_MAP_ARRAY              | QTextureCubeMapArray |
+-----------------+--------------------------------------+----------------------+
| iimageBuffer    | GL_IMAGE_BUFFER                      | QTextureBuffer       |
+-----------------+--------------------------------------+----------------------+
| iimageCubeArray | GL_INT_IMAGE_CUBE_MAP_ARRAY          | QTextureCubeMapArray |
+-----------------+--------------------------------------+----------------------+
| uimageBuffer    | GL_UNSIGNED_INT_IMAGE_BUFFER         | QTextureBuffer       |
+-----------------+--------------------------------------+----------------------+
| uimageCubeArray | GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY | QTextureCubeMapArray |
+-----------------+--------------------------------------+----------------------+

Expected use would look like:

::

    Qt3DRender::QTexture2D *tex2D = new Qt3DRender::QTexture2D();
    ...
    Qt3DRender::QMaterial *material = new Qt3DRender::QMaterial();
    ...
    Qt3DRender::QParameter *imageParameter = new Qt3DRender::QParameter();
    Qt3DRender::QShaderImage *shaderImage = new Qt3DRender::QShaderImage();

    shaderImage->setTexture(tex2D);

    imageParameter->setName("imageUniformName");
    imageParameter->setValue(QVariant::fromValue(shaderImage));

    material->addParameter(imageParamenter);
