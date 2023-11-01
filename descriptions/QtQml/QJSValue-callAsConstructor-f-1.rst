.. sip:method-description::
    :status: todo
    :pysig: 0d50be52828c61db04272fc1574ba393
    :realsig: (const QJSValueList&) const
    :digest: c09f55b1b8ddc7c4af26b7fe194f338a

Creates a new ``Object`` and calls this :sip:ref:`~PyQt6.QtQml.QJSValue` as a constructor, using the created object as the `this' object and passing *args* as arguments. If the return value from the constructor call is an object, then that object is returned; otherwise the default constructed object is returned.

If this :sip:ref:`~PyQt6.QtQml.QJSValue` is not a function, callAsConstructor() does nothing and returns an undefined :sip:ref:`~PyQt6.QtQml.QJSValue`.

Calling this function can cause an exception to occur in the script engine; in that case, the value that was thrown (typically an ``Error`` object) is returned. You can call :sip:ref:`~PyQt6.QtQml.QJSValue.isError` on the return value to determine whether an exception occurred.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSValue.call`, :sip:ref:`~PyQt6.QtQml.QJSEngine.newObject`.
