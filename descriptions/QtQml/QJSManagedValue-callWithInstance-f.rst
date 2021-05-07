.. sip:method-description::
    :status: todo
    :pysig: cf3a1132f17b8740a4a6d62364ac0d88
    :realsig: (const QJSValue&,const QJSValueList&) const
    :digest: 1b51728d8aec79e581a852c74a8880c5

If this :sip:ref:`~PyQt6.QtQml.QJSManagedValue` represents a JavaScript FunctionObject, calls it on *instance* with the given *arguments*, and returns the result. Otherwise returns a JavaScript ``undefined`` value.

The *arguments* and the *instance* have to be either primitive values or belong to the same :sip:ref:`~PyQt6.QtQml.QJSEngine` as this :sip:ref:`~PyQt6.QtQml.QJSManagedValue`. Otherwise the call is not carried out and a JavaScript ``undefined`` value is returned.
