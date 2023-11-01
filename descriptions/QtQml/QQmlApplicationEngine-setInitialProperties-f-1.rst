.. sip:method-description::
    :status: todo
    :pysig: d724b549ee2faa81b61b29cf2e8443ba
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
