.. sip:method-description::
    :status: todo
    :pysig: 3817872e51f557cb25e8fc29e228dfb6
    :realsig: (QObject*, const QString&, const QVariant&)
    :digest: 04aa3497ec2253a05850e5bbfab04d5b

Writes *value* to the *name* property of *object*. This method is equivalent to:

::

    QQmlProperty p(object, name);
    p.write(value);

Returns ``true`` on success, ``false`` otherwise.
