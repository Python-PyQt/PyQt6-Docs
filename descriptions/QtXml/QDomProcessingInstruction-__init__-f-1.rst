.. sip:method-description::
    :status: todo
    :pysig: 68d2b59f49956c495d0375847fbe281e
    :realsig: (const QDomProcessingInstruction&)
    :digest: 5be77a1831d92b5efa01a3f95d3f6e5d

Constructs a copy of *processingInstruction*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use cloneNode().
