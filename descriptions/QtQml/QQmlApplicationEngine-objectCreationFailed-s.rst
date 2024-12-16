.. sip:signal-description::
    :status: todo
    :pysig: 46a7bdf6ff0ff3a292573662f7d8a6a2
    :realsig: (const QUrl&)
    :digest: 4ee00b45d165830c31aa300f8bdc56d3

This signal is emitted when loading finishes because an error occurred.

The *url* to the component that failed to load is provided as an argument.

::

    QGuiApplication app(argc, argv);
    QQmlApplicationEngine engine;

    // exit on error
    QObject::connect(&engine, &QQmlApplicationEngine::objectCreationFailed,
        &app, []() { QCoreApplication::exit(-1); }, Qt::QueuedConnection);
    engine.load(QUrl());
    return app.exec();

**Note:** If the path to the component was provided as a QString containing a relative path, the *url* will contain a fully resolved path to the file.

See also :sip:ref:`~PyQt6.QtQml.QQmlApplicationEngine.objectCreated`, which will be emitted in addition to this signal (even though creation failed).
