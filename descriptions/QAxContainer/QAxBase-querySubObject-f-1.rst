.. sip:method-description::
    :status: todo
    :pysig: 686a9fb2195498d09fb58b180de29e2a
    :realsig: (const char*,const QVariant&,const QVariant&,const QVariant&,const QVariant&,const QVariant&,const QVariant&,const QVariant&,const QVariant&)
    :digest: 4bba862ee4987ed53a436ed9ba9b3655

Returns a pointer to a :sip:ref:`~PyQt6.QAxContainer.QAxObject` wrapping the COM object provided by the method or property *name*, passing passing the parameters *var1*, *var1*, *var2*, *var3*, *var4*, *var5*, *var6*, *var7* and *var8*.

If *name* is provided by a method the string must include the full function prototype.

If *name* is a property the string must be the name of the property, and *var1*, ... *var8* are ignored.

The returned :sip:ref:`~PyQt6.QAxContainer.QAxObject` is a child of this object (which is either of type :sip:ref:`~PyQt6.QAxContainer.QAxObject` or :sip:ref:`~PyQt6.QAxContainer.QAxWidget`), and is deleted when this object is deleted. It is however safe to delete the returned object yourself, and you should do so when you iterate over lists of subobjects.

COM enabled applications usually have an object model publishing certain elements of the application as dispatch interfaces. Use this method to navigate the hierarchy of the object model, e.g.

.. literalinclude:: ../../../snippets/qtactiveqt-src-activeqt-doc-snippets-src_activeqt_container_qaxbase.py
    :lines: 186-193
