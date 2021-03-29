.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 324e86b128749a7c37adc04860e6e7af

Constructs an opacity node with a default opacity of 1.

Opacity accumulates downwards in the scene graph so a node with two :sip:ref:`~PyQt6.QtQuick.QSGOpacityNode` instances above it, both with opacity of 0.5, will have effective opacity of 0.25.

The default opacity of nodes is 1.
