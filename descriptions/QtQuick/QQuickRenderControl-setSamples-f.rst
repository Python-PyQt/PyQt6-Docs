.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 6191ca5ea11870e57b6803decce77371

Sets the number of samples to use for multisampling. When *sampleCount* is 0 or 1, multisampling is disabled.

**Note:** This function is always used in combination with a multisample render target, which means *sampleCount* must match the sample count passed to QQuickRenderTarget::fromNativeTexture(), which in turn must match the sample count of the native texture.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.samples`, :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.initialize`, :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget`.
