.. sip:method-description::
    :status: todo
    :pysig: aed80aeda6ddfe5299bd437707dcf1bc
    :realsig: (const QJSValueList&) const
    :digest: a3a1a1710b70ee030607ad22883524e8

Calls this :sip:ref:`~PyQt6.QtQml.QJSValue` as a function, passing *args* as arguments to the function, and using the globalObject() as the "this"-object. Returns the value returned from the function.

If this :sip:ref:`~PyQt6.QtQml.QJSValue` is not callable, call() does nothing and returns an undefined :sip:ref:`~PyQt6.QtQml.QJSValue`.

Calling call() can cause an exception to occur in the script engine; in that case, call() returns the value that was thrown (typically an ``Error`` object). You can call :sip:ref:`~PyQt6.QtQml.QJSValue.isError` on the return value to determine whether an exception occurred.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSValue.isCallable`, :sip:ref:`~PyQt6.QtQml.QJSValue.callWithInstance`, :sip:ref:`~PyQt6.QtQml.QJSValue.callAsConstructor`.
