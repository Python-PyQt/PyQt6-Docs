.. sip:method-description::
    :status: todo
    :pysig: 49d5b65fd529405b4bc552e8933680b8
    :realsig: () const
    :digest: 3d890033b919eeb2b25c82c236ffb936

Returns the value in the :ref:`variant field<quuid-variant-field>` of the UUID. If the return value is :sip:ref:`~PyQt6.QtCore.QUuid.Variant.DCE`, call :sip:ref:`~PyQt6.QtCore.QUuid.version` to see which layout it uses. The null UUID is considered to be of an unknown variant.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUuid.version`.
