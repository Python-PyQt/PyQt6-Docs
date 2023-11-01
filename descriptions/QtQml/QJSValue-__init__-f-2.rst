.. sip:method-description::
    :status: todo
    :pysig: b5652daead3ff123a571c1f942c3a9a6
    :realsig: (const QJSValue&)
    :digest: 51c8ecc2ba72837bb6da8491c6a5c8bb

Constructs a new :sip:ref:`~PyQt6.QtQml.QJSValue` that is a copy of *other*.

Note that if *other* is an object (i.e., :sip:ref:`~PyQt6.QtQml.QJSValue.isObject` would return true), then only a reference to the underlying object is copied into the new script value (i.e., the object itself is not copied).
