.. sip:method-description::
    :status: todo
    :pysig: 9e21ab2f0507a2b6f49f9b255e190ffb
    :realsig: (const QVariantMap&)
    :digest: 1e1005c1d1910e9c179d84d17b3b0dce

Sets the *initialProperties* with which the QML component gets initialized after it gets loaded.

::

    QQmlApplicationEngine engine;

    EventDatabase eventDatabase;
    EventMonitor eventMonitor;

    engine.setInitialProperties({
        { "eventDatabase", QVariant::fromValue(&eventDatabase) },
        { "eventMonitor", QVariant::fromValue(&eventMonitor) }
    });

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlComponent.setInitialProperties`, :sip:ref:`~PyQt6.QtQml.QQmlApplicationEngine.load`, :sip:ref:`~PyQt6.QtQml.QQmlApplicationEngine.loadData`.
