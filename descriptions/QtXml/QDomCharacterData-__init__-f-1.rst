.. sip:method-description::
    :status: todo
    :pysig: 0bb8e0816b62d336c21e7d194e3f0990
    :realsig: (const QDomCharacterData&)
    :digest: 7745b52888363857df99f6f911008e90

Constructs a copy of *characterData*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use cloneNode().
