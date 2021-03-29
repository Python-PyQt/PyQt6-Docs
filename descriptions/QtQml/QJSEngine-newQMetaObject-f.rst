.. sip:method-description::
    :status: todo
    :pysig: 5c3f9ef7c2897eabe0a2975c87774b39
    :realsig: (const QMetaObject*)
    :digest: b5e48218ca77d3ee4567e8371f2fcb89

Creates a JavaScript object that wraps the given :sip:ref:`~PyQt6.QtCore.QMetaObject` The *metaObject* must outlive the script engine. It is recommended to only use this method with static metaobjects.

When called as a constructor, a new instance of the class will be created. Only constructors exposed by Q_INVOKABLE will be visible from the script engine.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSEngine.newQObject`, :ref:`qjsengine-qobject-integration`.
