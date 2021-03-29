.. sip:class-description::
    :status: todo
    :brief: Enable multisample antialiasing
    :realname: Qt3DRender::QMultiSampleAntiAliasing
    :digest: 1a78e93368d13d26ad4eca849824ac26

Enable multisample antialiasing.

A :sip:ref:`~PyQt6.Qt3DRender.QMultiSampleAntiAliasing` class enables multisample antialiasing.

It can be added to a QRenderPass by calling QRenderPass::addRenderState():

::

    QRenderPass *renderPass = new QRenderPass();

    QMultiSampleAntiAliasing *msaa = new QMultiSampleAntiAliasing();
    renderPass->addRenderState(msaa);

Or a QRenderStateSet by calling QRenderStateSet::addRenderState():

::

    QRenderStateSet *renderStateSet = new QRenderStateSet();

    QMultiSampleAntiAliasing *msaa = new QMultiSampleAntiAliasing();
    renderStateSet->addRenderState(msaa);

For multisampling to take effect, the render target must have been allocated with multisampling enabled:

::

    QTexture2DMultisample *colorTex = new QTexture2DMultisample;
    colorTex->setFormat(QAbstractTexture::RGBA8_UNorm);
    colorTex->setWidth(1024);
    colorTex->setHeight(1024);

    QRenderTargetOutput *color = new QRenderTargetOutput;
    color->setAttachmentPoint(QRenderTargetOutput::Color0);
    color->setTexture(colorTex);

    QTexture2DMultisample *depthStencilTex = new QTexture2DMultisample;
    depthStencilTex->setFormat(QAbstractTexture::RGBA8_UNorm);
    depthStencilTex->setWidth(1024);
    depthStencilTex->setHeight(1024);

    QRenderTargetOutput *depthStencil = new QRenderTargetOutput;
    depthStencil->setAttachmentPoint(QRenderTargetOutput::DepthStencil);
    depthStencil->setTexture(depthStencilTex);

    Qt3DRender::QRenderTarget *renderTarget = new Qt3DRender::QRenderTarget;
    renderTarget->addOutput(color);
    renderTarget->addOutput(depthStencil);

Further, the shader code must use multisampling sampler types and texelFetch() instead of texture().

For example, if you have code like

::

    #version 150

    uniform sampler2D colorTexture;
    in vec2 texCoord;
    out vec4 fragColor;

    void main()
    {
        fragColor = texture(colorTexture, texCoord);
    }

you can rewrite it as

::

    #version 150

    uniform sampler2DMS colorTexture;
    in vec2 texCoord;
    out vec4 fragColor;

    void main()
    {
        ivec2 tc = ivec2(floor(textureSize(colorTexture) * texCoord));
        vec4 c = texelFetch(colorTexture, tc, 0) +
                    texelFetch(colorTexture, tc, 1) +
                    texelFetch(colorTexture, tc, 2) +
                    texelFetch(colorTexture, tc, 3);
        fragColor = c / 4.0;
    }

**Note:** When using OpenGL as the graphics API, glEnable(GL_MULTISAMPLE) will be called if :sip:ref:`~PyQt6.Qt3DRender.QMultiSampleAntiAliasing` has been added to the render states.
