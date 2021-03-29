.. sip:class-description::
    :status: todo
    :brief: Provides storage for a name and value pair. This maps to a shader uniform
    :realname: Qt3DRender::QParameter
    :digest: 7239d2e236d47a8951cc14168756c952

Provides storage for a name and value pair. This maps to a shader uniform.

A :sip:ref:`~PyQt6.Qt3DRender.QParameter` can be referenced by a QRenderPass, QTechnique, QEffect, QMaterial, QTechniqueFilter, QRenderPassFilter. At runtime, depending on which shader is selected for a given step of the rendering, the value contained in a :sip:ref:`~PyQt6.Qt3DRender.QParameter` will be converted and uploaded if the shader contains a uniform with a name matching that of the :sip:ref:`~PyQt6.Qt3DRender.QParameter`.

::

    QParameter *param = new QParameter();
    param->setName(QStringLiteral("diffuseColor"));
    param->setValue(QColor::fromRgbF(0.0f, 0.0f, 1.0f, 1.0f));

    // Alternatively you can create and set a QParameter this way
    QParameter *param2 = new QParameter(QStringLiteral("diffuseColor"), QColor::fromRgbF(0.0f, 0.0f, 1.0f, 1.0f));

    // Such QParameters will work with the following GLSL uniform shader declarations
    // uniform vec4 diffuseColor;
    // uniform vec3 diffuseColor;
    // uniform vec2 diffuseColor;
    // uniform float diffuseColor;

**Note:** some care must be taken to ensure the value wrapped by a :sip:ref:`~PyQt6.Qt3DRender.QParameter` can actually be converted to what the real uniform expect. Giving a value stored as an int where the actual shader uniform is of type float could result in undefined behaviors.

**Note:** when the targeted uniform is an array, the name should be the name of the uniform with [0] appended to it.

**Note:** :sip:ref:`~PyQt6.Qt3DRender.QParameter` node can not be disabled.

::

    QParameter *param = new QParameter();
    QVariantList values = QVariantList() << 0.0f << 1.0f << 2.0f << 3.0f << 4.0f << 883.0f << 1340.0f << 1584.0f;

    param->setName(QStringLiteral("diffuseValues[0]"));
    param->setValue(values);

    // Matching GLSL shader uniform  declaration
    // uniform float diffuseValues[8];

When it comes to texture support, the :sip:ref:`~PyQt6.Qt3DRender.QParameter` value should be set to the appropriate QAbstractTexture subclass that matches the sampler type of the shader uniform.

::

    QTexture2D *texture = new QTexture2D();
    ...
    QParameter *param = new QParameter();
    param->setName(QStringLiteral("diffuseTexture"));
    param->setValue(QVariant::fromValue(texture));

    // Works with the following GLSL uniform shader declaration
    // uniform sampler2D diffuseTexture

.. seealso:: QAbstractTexture.
