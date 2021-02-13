.. sip:method-description::
    :status: todo
    :pysig: 9be2e04d2c0fa9fc604535ada4979af1
    :realsig: (QObject*,const QString&,const QVariant&)
    :digest: 04aa3497ec2253a05850e5bbfab04d5b

Writes *value* to the *name* property of *object*. This method is equivalent to:

::

    QQmlProperty p(object, name);
    p.write(value);

Returns ``true`` on success, ``false`` otherwise.
