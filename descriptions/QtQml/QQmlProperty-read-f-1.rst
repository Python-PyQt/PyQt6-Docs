.. sip:method-description::
    :status: todo
    :pysig: 0291089dbdde18e0f145153df9bf6ddb
    :realsig: (const QObject*, const QString&)
    :digest: 620f77019a089c2cd10edaa90fb2dbb5

Return the *name* property value of *object*. This method is equivalent to:

::

    QQmlProperty p(object, name);
    p.read();
