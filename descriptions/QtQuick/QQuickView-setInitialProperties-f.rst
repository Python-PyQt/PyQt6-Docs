.. sip:method-description::
    :status: todo
    :pysig: 02686623c57a80e2957e02cfef8f775a
    :realsig: (const QVariantMap&)
    :digest: 58c23f65e16330e2c24974ea3b562c2e

Sets the initial properties *initialProperties* with which the QML component gets initialized after calling :sip:ref:`~PyQt6.QtQuick.QQuickView.setSource`.

.. literalinclude:: ../../../snippets/qtdeclarative-src-quick-doc-snippets-qquickview-ex.py

**Note:** You can only use this function to initialize top-level properties.

**Note:** This function should always be called before :sip:ref:`~PyQt6.QtQuick.QQuickView.setSource`, as it has no effect once the component has become ``Ready``.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlComponent.createWithInitialProperties`.
