.. sip:method-description::
    :status: todo
    :pysig: b2a1c3086695add31455bfea8040aff8
    :realsig: (const char*)
    :digest: b0b1d9f0728ba8877f1472863c6d7c06

Normalizes the signature of the given *method*.

Qt uses normalized signatures to decide whether two given signals and slots are compatible. Normalization reduces whitespace to a minimum, moves 'const' to the front where appropriate, removes 'const' from value types and replaces const references with values.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMetaObject.checkConnectArgs`, :sip:ref:`~PyQt6.QtCore.QMetaObject.normalizedType`.
