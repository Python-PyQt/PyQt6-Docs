.. sip:method-description::
    :status: todo
    :pysig: da86c4de85c219517df1794596a44dfa
    :realsig: (const QSize&)
    :digest: e061f7f6e78e0969ecbaa9dadbf6f991

Grabs the item into an in-memory image.

The grab happens asynchronously and the signal :sip:ref:`~PyQt6.QtQuick.QQuickItemGrabResult.ready` is emitted when the grab has been completed.

Use *targetSize* to specify the size of the target image. By default, the result will have the same size as item.

If the grab could not be initiated, the function returns ``null``.

**Note:** This function will render the item to an offscreen surface and copy that surface from the GPU's memory into the CPU's memory, which can be quite costly. For "live" preview, use `layers <https://doc.qt.io/qt-6/qml-qtquick-item.html#layer.enabled-prop>`_ or `ShaderEffectSource <https://doc.qt.io/qt-6/qml-qtquick-shadereffectsource.html>`_.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.grabWindow`.
