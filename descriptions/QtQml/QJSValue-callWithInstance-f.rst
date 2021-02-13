.. sip:method-description::
    :status: todo
    :pysig: ac78974286707e65f40b203f63eb879c
    :realsig: (const QJSValue&,const QJSValueList&) const
    :digest: 6fbac52fc64c7ad060f25b2b56143188

Calls this :sip:ref:`~PyQt6.QtQml.QJSValue` as a function, using *instance* as the `this' object in the function call, and passing *args* as arguments to the function. Returns the value returned from the function.

If this :sip:ref:`~PyQt6.QtQml.QJSValue` is not a function, :sip:ref:`~PyQt6.QtQml.QJSValue.call` does nothing and returns an undefined :sip:ref:`~PyQt6.QtQml.QJSValue`.

Note that if *instance* is not an object, the global object (see :sip:ref:`~PyQt6.QtQml.QJSEngine.globalObject`) will be used as the `this' object.

Calling :sip:ref:`~PyQt6.QtQml.QJSValue.call` can cause an exception to occur in the script engine; in that case, :sip:ref:`~PyQt6.QtQml.QJSValue.call` returns the value that was thrown (typically an ``Error`` object). You can call :sip:ref:`~PyQt6.QtQml.QJSValue.isError` on the return value to determine whether an exception occurred.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSValue.call`.
