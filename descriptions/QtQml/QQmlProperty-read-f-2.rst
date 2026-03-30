.. sip:method-description::
    :status: todo
    :pysig: b817d83b8c735c239c5d2497e9737e51
    :realsig: (const QObject*, const QString&, QQmlContext*)
    :digest: 146843ea3a67068cb58c487a70d69230

Return the *name* property value of *object* using the :sip:ref:`~PyQt6.QtQml.QQmlContext` *ctxt*. This method is equivalent to:

::

    QQmlProperty p(object, name, context);
    p.read();
