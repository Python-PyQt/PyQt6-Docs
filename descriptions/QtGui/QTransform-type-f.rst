.. sip:method-description::
    :status: todo
    :pysig: ec2fc950846c68ab8bf194645bae309b
    :realsig: () const
    :digest: 88cb801fb1f5ce9b31642db4f67c8137

Returns the transformation type of this matrix.

The transformation type is the highest enumeration value capturing all of the matrix's transformations. For example, if the matrix both scales and shears, the type would be ``TxShear``, because ``TxShear`` has a higher enumeration value than ``TxScale``.

Knowing the transformation type of a matrix is useful for optimization: you can often handle specific types more optimally than handling the generic case.
