.. sip:method-description::
    :status: todo
    :pysig: 069a30a9e24ae506574af9817557a41c
    :realsig: (const QVariantMap&)
    :digest: 3dcdb098034faf26affafec6e8146c91

Sets the initial properties *initialProperties* with which the QML component gets initialized after calling :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.setSource`.

**Note:** You can only use this function to initialize top-level properties.

**Note:** This function should always be called before :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.setSource`, as it has no effect once the component has become ``Ready``.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlComponent.createWithInitialProperties`.
