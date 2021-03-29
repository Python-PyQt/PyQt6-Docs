.. sip:method-description::
    :status: todo
    :pysig: 08736f47c8e802a0d3b82fecfcd930b6
    :realsig: (const QObject*,const QString&)
    :digest: 620f77019a089c2cd10edaa90fb2dbb5

Return the *name* property value of *object*. This method is equivalent to:

::

    QQmlProperty p(object, name);
    p.read();
