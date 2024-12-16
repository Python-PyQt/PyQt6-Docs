.. sip:method-description::
    :status: todo
    :pysig: 95f638a622b85b602a16440390dad171
    :realsig: (const QFormDataPartBuilder&)
    :digest: 5c645e1c2b8f373b099ef850bfd333d4

Constructs a copy of *other*. The object is valid for as long as the associated :sip:ref:`~PyQt6.QtNetwork.QFormDataBuilder` has not been destroyed.

The data of the copy is shared (shallow copy): modifying one part will also change the other.

::

    QFormDataPartBuilder foo()
    {
        QFormDataBuilder builder;
        auto qfdpb1 = builder.part("First"_L1);
        auto qfdpb2 = qfdpb1; // this creates a shallow copy

        qfdpb2.setBodyDevice(&image, "cutecat.jpg"); // qfdpb1 is also modified

        return qfdbp2;  // invalid, builder is destroyed at the end of the scope
    }
