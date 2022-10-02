.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: fe7ef5839002400263f4c7485aee87e1

Sets the size of the render target contents should be mirrored vertically to *enable* when drawing. This allows easy integration of third-party rendering code that does not follow the standard expectations.

**Note:** This function should not be used when using the ``software`` backend.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget.mirrorVertically`.
