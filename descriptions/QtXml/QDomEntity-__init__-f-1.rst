.. sip:method-description::
    :status: todo
    :pysig: ca4f07698e27c2c7ba0a5e3a51735ac0
    :realsig: (const QDomEntity&)
    :digest: f14295577a8e81e3795d8ee35cf765a5

Constructs a copy of *entity*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use cloneNode().
