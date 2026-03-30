.. sip:method-description::
    :status: todo
    :pysig: 7746aa916ef9ee0d5376c9a6223dc1a3
    :realsig: (const QJSValue&)
    :digest: 64ecf2a0c27ae22a167e7eb0b0dbb3e0

If this :sip:ref:`~PyQt6.QtQml.QJSValue` is an object, sets the internal prototype (``__proto__`` property) of this object to be *prototype*; if the :sip:ref:`~PyQt6.QtQml.QJSValue` is null, it sets the prototype to null; otherwise does nothing.

The internal prototype should not be confused with the public property with name "prototype"; the public prototype is usually only set on functions that act as constructors.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSValue.prototype`, :sip:ref:`~PyQt6.QtQml.QJSValue.isObject`.
