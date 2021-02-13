.. sip:method-description::
    :status: todo
    :pysig: 6f9bd443efc69d5fb85e04b6ca205057
    :realsig: (const QDomNode&)
    :digest: 61022c17cc1de5fbfaecabb4ebfa4c6f

Constructs a copy of *n*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use :sip:ref:`~PyQt6.QtXml.QDomNode.cloneNode`.
