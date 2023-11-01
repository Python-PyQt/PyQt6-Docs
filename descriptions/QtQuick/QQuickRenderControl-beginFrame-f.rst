.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 991978e5a7094d13ab190ff1c5139a35

Specifies the start of a graphics frame. Calls to :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.sync` or :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.render` must be enclosed by calls to beginFrame() and :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.endFrame`.

Unlike the earlier OpenGL-only world of Qt 5, rendering with other graphics APIs requires more well-defined points of starting and ending a frame. When manually driving the rendering loop via :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl`, it now falls to the user of :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl` to specify these points.

A typical update step, including initialization of rendering into an existing texture, could look like the following. The example snippet assumes Direct3D 11 but the same concepts apply other graphics APIs as well.

::

    if (!m_quickInitialized) {
        m_quickWindow->setGraphicsDevice(QQuickGraphicsDevice::fromDeviceAndContext(m_engine->device(), m_engine->context()));

        if (!m_renderControl->initialize())
            qWarning("Failed to initialize redirected Qt Quick rendering");

        m_quickWindow->setRenderTarget(QQuickRenderTarget::fromNativeTexture({ quint64(m_res.texture), 0 },
                                                                             QSize(QML_WIDTH, QML_HEIGHT),
                                                                             SAMPLE_COUNT));

        m_quickInitialized = true;
    }

    m_renderControl->polishItems();

    m_renderControl->beginFrame();
    m_renderControl->sync();
    m_renderControl->render();
    m_renderControl->endFrame(); // Qt Quick's rendering commands are submitted to the device context here

**Note:** This function does not need to be, and must not be, called when using the ``software`` adaptation of Qt Quick.

**Note:** Internally beginFrame() and :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.endFrame` invoke QRhi::beginOffscreenFrame() and QRhi::endOffscreenFrame(), respectively. This implies that there must not be a frame (neither offscreen, nor swapchain-based) being recorded on the QRhi when this function is called.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.endFrame`, :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.initialize`, :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.sync`, :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.render`, :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsDevice`, :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget`.
