.. sip:method-description::
    :status: todo
    :pysig: 38464ba45ee82d6b24359e182b063ec8
    :realsig: (QJSValue,QJSEngine*)
    :digest: 80adbaf90c0bdaaedd237f8f53797396

Creates a :sip:ref:`~PyQt6.QtQml.QJSManagedValue` from *value*, using the heap of *engine*. If *value* is itself managed and the engine it belongs to is not *engine*, the result is an ``undefined`` value, and a warning is generated.
