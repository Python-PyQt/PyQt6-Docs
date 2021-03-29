.. sip:method-description::
    :status: todo
    :pysig: 2b9057d9b4a06375acf76e6922f506e2
    :realsig: (QObject*)
    :digest: ad74708443b2e542dd55e7c29b49e2f9

Called after the *object* is first created, but before property bindings are evaluated and, if applicable, :sip:ref:`~PyQt6.QtQml.QQmlParserStatus.componentComplete` is called. This is equivalent to the point between :sip:ref:`~PyQt6.QtQml.QQmlComponent.beginCreate` and :sip:ref:`~PyQt6.QtQml.QQmlComponent.completeCreate`, and can be used to assign initial values to the object's properties.

The default implementation does nothing.
