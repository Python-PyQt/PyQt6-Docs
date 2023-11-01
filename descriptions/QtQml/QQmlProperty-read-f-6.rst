.. sip:method-description::
    :status: todo
    :pysig: 002f858234e3b49ee7f04ab384f6d44b
    :realsig: (const QObject*, const QString&, QQmlEngine*)
    :digest: c8a077b14ab6f01754a31cdec1c06887

Return the *name* property value of *object* using the environment for instantiating QML components that is provided by *engine*. . This method is equivalent to:

::

    QQmlProperty p(object, name, engine);
    p.read();
