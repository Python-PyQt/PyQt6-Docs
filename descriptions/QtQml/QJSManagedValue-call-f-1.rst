.. sip:method-description::
    :status: todo
    :pysig: ec282d497c0b8f2ecb9299f5cd1c60a4
    :realsig: (const QJSValueList&) const
    :digest: 03282d27f2a19e870f4d79ce4ffdfcd2

If this :sip:ref:`~PyQt6.QtQml.QJSManagedValue` represents a JavaScript FunctionObject, calls it with the given *arguments*, and returns the result. Otherwise returns a JavaScript ``undefined`` value.

The *arguments* have to be either primitive values or belong to the same :sip:ref:`~PyQt6.QtQml.QJSEngine` as this :sip:ref:`~PyQt6.QtQml.QJSManagedValue`. Otherwise the call is not carried out and a JavaScript ``undefined`` value is returned.
