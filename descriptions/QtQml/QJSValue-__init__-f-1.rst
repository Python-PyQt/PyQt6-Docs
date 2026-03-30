.. sip:method-description::
    :status: todo
    :pysig: 7746aa916ef9ee0d5376c9a6223dc1a3
    :realsig: (const QJSValue&)
    :digest: 51c8ecc2ba72837bb6da8491c6a5c8bb

Constructs a new :sip:ref:`~PyQt6.QtQml.QJSValue` that is a copy of *other*.

Note that if *other* is an object (i.e., :sip:ref:`~PyQt6.QtQml.QJSValue.isObject` would return true), then only a reference to the underlying object is copied into the new script value (i.e., the object itself is not copied).
