.. sip:method-description::
    :status: todo
    :pysig: 34a3f8799e86679f9124acab800847d0
    :realsig: (const QObject*, const QString&)
    :digest: 620f77019a089c2cd10edaa90fb2dbb5

Return the *name* property value of *object*. This method is equivalent to:

::

    QQmlProperty p(object, name);
    p.read();
