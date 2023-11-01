.. sip:method-description::
    :status: todo
    :pysig: 4142990049bd75d48a0d6e100fd9bfd2
    :realsig: (const QObject*, const QString&, QQmlContext*)
    :digest: 146843ea3a67068cb58c487a70d69230

Return the *name* property value of *object* using the :sip:ref:`~PyQt6.QtQml.QQmlContext` *ctxt*. This method is equivalent to:

::

    QQmlProperty p(object, name, context);
    p.read();
