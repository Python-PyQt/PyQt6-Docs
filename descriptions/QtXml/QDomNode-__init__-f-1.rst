.. sip:method-description::
    :status: todo
    :pysig: 6f9bd443efc69d5fb85e04b6ca205057
    :realsig: (const QDomNode&)
    :digest: f9f20380e6ce98ca970646aeec30f5ae

Constructs a copy of *node*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use :sip:ref:`~PyQt6.QtXml.QDomNode.cloneNode`.
