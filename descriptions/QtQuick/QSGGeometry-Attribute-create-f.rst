.. sip:method-description::
    :status: todo
    :pysig: ba1b4b1b9aa516fe54717e57ceb704ca
    :realsig: (int,int,int,bool)
    :digest: 9c41398b4e286be33db1acc430873147

Creates a new :sip:ref:`~PyQt6.QtQuick.QSGGeometry.Attribute` for attribute register *pos* with *tupleSize*. The *primitiveType* can be any of the supported types from :sip:ref:`~PyQt6.QtQuick.QSGGeometry.Type`, such as :sip:ref:`~PyQt6.QtQuick.QSGGeometry.Type.FloatType` or :sip:ref:`~PyQt6.QtQuick.QSGGeometry.Type.UnsignedByteType`.

If the attribute describes the position for the vertex, the *isPosition* hint should be set to ``true``. The scene graph renderer may use this information to perform optimizations.

Use the create function to construct the attribute, rather than an initialization list, to ensure that all fields are initialized.
