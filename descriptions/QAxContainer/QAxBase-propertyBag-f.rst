.. sip:method-description::
    :status: todo
    :pysig: 02686623c57a80e2957e02cfef8f775a
    :realsig: () const
    :digest: 0c919f795f5d96305b0fda7e1fa5bc97

Returns a name:value map of all the properties exposed by the COM object.

This is more efficient than getting multiple properties individually if the COM object supports property bags.

**Warning:** It is not guaranteed that the property bag implementation of the COM object returns all properties, or that the properties returned are the same as those available through the IDispatch interface.

.. seealso:: :sip:ref:`~PyQt6.QAxContainer.QAxBase.setPropertyBag`.
