.. sip:method-description::
    :status: todo
    :pysig: 992e8d0e5b57a6e4e940f41b84286512
    :realsig: ()
    :digest: 379134f36186af53bda0fa1d95c2affc

Returns the current system time zone IANA ID.

On Windows this ID is translated from the Windows ID using an internal translation table and the user's selected country. As a consequence there is a small chance any Windows install may have IDs not known by Qt, in which case "UTC" will be returned.

This method is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.systemTimeZone`.
