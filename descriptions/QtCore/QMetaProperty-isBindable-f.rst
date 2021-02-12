.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 0e2dc23deb3524052bd06895f6dc0776

Returns ``true`` if the ``Q_PROPERTY()`` exposes binding functionality; otherwise returns false.

This implies that you can create bindings that use this property as a dependency or install QPropertyObserver objects on this property. Unless the property is readonly, you can also set a binding on this property.

.. seealso:: QProperty, :sip:ref:`~PyQt6.QtCore.QMetaProperty.isWritable`, bindable().
