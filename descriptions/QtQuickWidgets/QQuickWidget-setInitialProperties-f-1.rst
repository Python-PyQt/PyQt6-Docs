.. sip:method-description::
    :status: todo
    :pysig: 9e21ab2f0507a2b6f49f9b255e190ffb
    :realsig: (const QVariantMap&)
    :digest: 3dcdb098034faf26affafec6e8146c91

Sets the initial properties *initialProperties* with which the QML component gets initialized after calling :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.setSource`.

**Note:** You can only use this function to initialize top-level properties.

**Note:** This function should always be called before :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.setSource`, as it has no effect once the component has become ``Ready``.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlComponent.createWithInitialProperties`.
