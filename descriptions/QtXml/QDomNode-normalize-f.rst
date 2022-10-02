.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 2cdda63cf4c5f985966ba6fa7c044cdc

Calling normalize() on an element converts all its children into a standard form. This means that adjacent :sip:ref:`~PyQt6.QtXml.QDomText` objects will be merged into a single text object (\ :sip:ref:`~PyQt6.QtXml.QDomCDATASection` nodes are not merged).
