.. sip:method-description::
    :status: todo
    :pysig: df1fa7163c54e2002dbb7944ebef160e
    :realsig: () const
    :digest: 7c59003abd06127d3b5ad4680099bbfc

Returns the access specification of this method (private, protected, or public).

**Note:** Signals are always public, but you should regard that as an implementation detail. It is almost always a bad idea to emit a signal from outside its class.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMetaMethod.methodType`.
