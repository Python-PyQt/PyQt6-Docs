.. sip:method-description::
    :status: todo
    :pysig: b63f4089ef456f745598cdb11e18425a
    :realsig: (QObject*, const QString&, const QVariant&)
    :digest: 04aa3497ec2253a05850e5bbfab04d5b

Writes *value* to the *name* property of *object*. This method is equivalent to:

::

    QQmlProperty p(object, name);
    p.write(value);

Returns ``true`` on success, ``false`` otherwise.
