.. sip:method-description::
    :status: todo
    :pysig: efc8f8a34ef6f5d837035ec44fa99b83
    :realsig: (QObject*, const QString&, const QVariant&, QQmlContext*)
    :digest: e0ebdef35fd3cadf783739051379099c

Writes *value* to the *name* property of *object* using the :sip:ref:`~PyQt6.QtQml.QQmlContext` *ctxt*. This method is equivalent to:

::

    QQmlProperty p(object, name, ctxt);
    p.write(value);

Returns ``true`` on success, ``false`` otherwise.
