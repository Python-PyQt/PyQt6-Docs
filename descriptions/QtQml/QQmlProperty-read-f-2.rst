.. sip:method-description::
    :status: todo
    :pysig: 7a935be1be801ebb640796be00743f41
    :realsig: (const QObject*,const QString&,QQmlContext*)
    :digest: 146843ea3a67068cb58c487a70d69230

Return the *name* property value of *object* using the :sip:ref:`~PyQt6.QtQml.QQmlContext` *ctxt*. This method is equivalent to:

::

    QQmlProperty p(object, name, context);
    p.read();
