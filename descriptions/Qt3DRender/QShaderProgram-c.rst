.. sip:class-description::
    :status: todo
    :brief: Encapsulates a Shader Program
    :realname: Qt3DRender::QShaderProgram
    :digest: bda226d6826d90419a1bb33405457b9d

Encapsulates a Shader Program.

A shader program consists of several different shaders, such as vertex and fragment shaders.

Qt3D will automatically populate a set of default uniforms if they are encountered during the shader instrospection phase.

+-----------------------------------------------+--------------------------------+----------------------------------------------------------------------+
| Default Uniform                               | Associated Qt3D Parameter name | GLSL declaration                                                     |
+===============================================+================================+======================================================================+
| ModelMatrix                                   | modelMatrix                    | uniform mat4 modelMatrix;                                            |
+-----------------------------------------------+--------------------------------+----------------------------------------------------------------------+
| ViewMatrix                                    | viewMatrix                     | uniform mat4 viewMatrix;                                             |
+-----------------------------------------------+--------------------------------+----------------------------------------------------------------------+
| ProjectionMatrix                              | projectionMatrix               | uniform mat4 projectionMatrix;                                       |
+-----------------------------------------------+--------------------------------+----------------------------------------------------------------------+
| ModelViewMatrix                               | modelView                      | uniform mat4 modelView;                                              |
+-----------------------------------------------+--------------------------------+----------------------------------------------------------------------+
| ViewProjectionMatrix                          | viewProjectionMatrix           | uniform mat4 viewProjectionMatrix;                                   |
+-----------------------------------------------+--------------------------------+----------------------------------------------------------------------+
| ModelViewProjectionMatrix                     | modelViewProjection  mvp       | uniform mat4 modelViewProjection;  uniform mat4 mvp;                 |
+-----------------------------------------------+--------------------------------+----------------------------------------------------------------------+
| InverseModelMatrix                            | inverseModelMatrix             | uniform mat4 inverseModelMatrix;                                     |
+-----------------------------------------------+--------------------------------+----------------------------------------------------------------------+
| InverseViewMatrix                             | inverseViewMatrix              | uniform mat4 inverseViewMatrix;                                      |
+-----------------------------------------------+--------------------------------+----------------------------------------------------------------------+
| InverseProjectionMatrix                       | inverseProjectionMatrix        | uniform mat4 inverseProjectionMatrix;                                |
+-----------------------------------------------+--------------------------------+----------------------------------------------------------------------+
| InverseModelViewMatrix                        | inverseModelView               | uniform mat4 inverseModelView;                                       |
+-----------------------------------------------+--------------------------------+----------------------------------------------------------------------+
| InverseViewProjectionMatrix                   | inverseViewProjectionMatrix    | uniform mat4 inverseViewProjectionMatrix;                            |
+-----------------------------------------------+--------------------------------+----------------------------------------------------------------------+
| InverseModelViewProjectionMatrix              | inverseModelViewProjection     | uniform mat4 inverseModelViewProjection;                             |
+-----------------------------------------------+--------------------------------+----------------------------------------------------------------------+
| ModelNormalMatrix                             | modelNormalMatrix              | uniform mat3 modelNormalMatrix;                                      |
+-----------------------------------------------+--------------------------------+----------------------------------------------------------------------+
| ModelViewNormalMatrix                         | modelViewNormal                | uniform mat3 modelViewNormal;                                        |
+-----------------------------------------------+--------------------------------+----------------------------------------------------------------------+
| ViewportMatrix                                | viewportMatrix                 | uniform mat4 viewportMatrix;                                         |
+-----------------------------------------------+--------------------------------+----------------------------------------------------------------------+
| InverseViewportMatrix                         | inverseViewportMatrix          | uniform mat4 inverseViewportMatrix;                                  |
+-----------------------------------------------+--------------------------------+----------------------------------------------------------------------+
| AspectRatio  (surface width / surface height) | aspectRatio                    | uniform float aspectRatio;                                           |
+-----------------------------------------------+--------------------------------+----------------------------------------------------------------------+
| Exposure                                      | exposure                       | uniform float exposure;                                              |
+-----------------------------------------------+--------------------------------+----------------------------------------------------------------------+
| Gamma                                         | gamma                          | uniform float gamma;                                                 |
+-----------------------------------------------+--------------------------------+----------------------------------------------------------------------+
| Time  (in nano seconds)                       | time                           | uniform float time;                                                  |
+-----------------------------------------------+--------------------------------+----------------------------------------------------------------------+
| EyePosition                                   | eyePosition                    | uniform vec3 eyePosition;                                            |
+-----------------------------------------------+--------------------------------+----------------------------------------------------------------------+
| SkinningPalette                               | skinningPalette[0]             | const int maxJoints = 100;  uniform mat4 skinningPalette[maxJoints]; |
+-----------------------------------------------+--------------------------------+----------------------------------------------------------------------+

.. _qt3drender-qshaderprogram-rhi-support:

RHI Support
-----------

When writing GLSL 450 shader code to use with Qt 3D's RHI backend, the default uniforms will be provided as 2 uniform buffer objects.

The binding locations for these is set to bindings 0 for RenderView uniforms and 1 for Command uniforms.

::

    #version 450 core

    layout(location = 0) in vec3 vertexPosition;

    layout(std140, binding = 0) uniform qt3d_render_view_uniforms {
      mat4 viewMatrix;
      mat4 projectionMatrix;
      mat4 uncorrectedProjectionMatrix;
      mat4 clipCorrectionMatrix;
      mat4 viewProjectionMatrix;
      mat4 inverseViewMatrix;
      mat4 inverseProjectionMatrix;
      mat4 inverseViewProjectionMatrix;
      mat4 viewportMatrix;
      mat4 inverseViewportMatrix;
      vec4 textureTransformMatrix;
      vec3 eyePosition;
      float aspectRatio;
      float gamma;
      float exposure;
      float time;
      float yUpInNDC;
      float yUpInFBO;
    };

    layout(std140, binding = 1) uniform qt3d_command_uniforms {
      mat4 modelMatrix;
      mat4 inverseModelMatrix;
      mat4 modelViewMatrix;
      mat3 modelNormalMatrix;
      mat4 inverseModelViewMatrix;
      mat4 modelViewProjection;
      mat4 inverseModelViewProjectionMatrix;
    };

    void main()
    {
        gl_Position = (projectionMatrix * viewMatrix * modelMatrix * vertexPosition);
    }

For user defined uniform buffer object, use binding starting at 2 or auto to let Qt 3D work out the binding automatically. Make sure to remain consistent between the different shader stages.

::

    #version 450 core

    layout(std140, binding = auto) uniform my_uniforms {
      vec4 myColor;
    };

    layout(location=0) out vec4 fragColor;

    void main()
    {
        fragColor = myColor;
    }

There is no change involved when it comes to feeding values to uniforms.

For the above example, setting myColor could be done with:

::

    QParameter *parameter = new QParameter();
    parameter->setName("myColor");
    parameter->setValue(QVariant::fromValue(QColor(Qt::blue)));

Textures still have to be defined as standalone uniforms.

::

    #version 450 core

    layout(binding=0) uniform sampler2D source;

    layout(location=0) out vec4 fragColor;

    void main()
    {
        fragColor = texture(source, vec2(0.5, 0.5));
    }
