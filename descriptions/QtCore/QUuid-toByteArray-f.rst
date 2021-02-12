.. sip:method-description::
    :status: todo
    :pysig: 5fe67601350b3adde06033769fdb7319
    :realsig: (QUuid::StringFormat) const
    :digest: 033f81846c222712f7f9a852176e092e

Returns the string representation of this :sip:ref:`~PyQt6.QtCore.QUuid`, with the formattiong controlled by the *mode* parameter. From left to right, the five hex fields are obtained from the four public data members in :sip:ref:`~PyQt6.QtCore.QUuid` as follows:

+---------+----------------------+
| Field # | Source               |
+=========+======================+
| 1       | data1                |
+---------+----------------------+
| 2       | data2                |
+---------+----------------------+
| 3       | data3                |
+---------+----------------------+
| 4       | data4[0] .. data4[1] |
+---------+----------------------+
| 5       | data4[2] .. data4[7] |
+---------+----------------------+
