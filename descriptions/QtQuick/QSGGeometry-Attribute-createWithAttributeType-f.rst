.. sip:method-description::
    :status: todo
    :pysig: f8d21b3900b266815184b499d5206583
    :realsig: (int,int,int,QSGGeometry::AttributeType)
    :digest: 7b62abb794ebc3c6b264cb65bf11b55c

Creates a new :sip:ref:`~PyQt6.QtQuick.QSGGeometry.Attribute` for attribute register *pos* with *tupleSize*. The *primitiveType* can be any of the supported types from :sip:ref:`~PyQt6.QtQuick.QSGGeometry.Type`, such as :sip:ref:`~PyQt6.QtQuick.QSGGeometry.Type.FloatType` or :sip:ref:`~PyQt6.QtQuick.QSGGeometry.Type.UnsignedByteType`.

*attributeType* describes the intended use of the attribute.

Use the create function to construct the attribute, rather than an initialization list, to ensure that all fields are initialized.
