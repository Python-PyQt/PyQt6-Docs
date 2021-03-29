.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: b858876c13819018c1f03e1977cf41df

Override this function to do processing on the node before it is rendered.

Preprocessing needs to be explicitly enabled by setting the flag :sip:ref:`~PyQt6.QtQuick.QSGNode.Flags.UsePreprocess`. The flag needs to be set before the node is added to the scene graph and will cause the  function to be called for every frame the node is rendered.

**Warning:** Beware of deleting nodes while they are being preprocessed. It is possible, with a small performance hit, to delete a single node during its own preprocess call. Deleting a subtree which has nodes that also use preprocessing may result in a segmentation fault. This is done for performance reasons.
