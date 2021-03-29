.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: fabcb8b6396cac33d187804a9a9d6016

Optimize the usage of this matrix from its current elements.

Some operations such as :sip:ref:`~PyQt6.QtGui.QMatrix4x4.translate`, :sip:ref:`~PyQt6.QtGui.QMatrix4x4.scale`, and :sip:ref:`~PyQt6.QtGui.QMatrix4x4.rotate` can be performed more efficiently if the matrix being modified is already known to be the identity, a previous :sip:ref:`~PyQt6.QtGui.QMatrix4x4.translate`, a previous :sip:ref:`~PyQt6.QtGui.QMatrix4x4.scale`, etc.

Normally the :sip:ref:`~PyQt6.QtGui.QMatrix4x4` class keeps track of this special type internally as operations are performed. However, if the matrix is modified directly with operator()() or :sip:ref:`~PyQt6.QtGui.QMatrix4x4.data`, then :sip:ref:`~PyQt6.QtGui.QMatrix4x4` will lose track of the special type and will revert to the safest but least efficient operations thereafter.

By calling  after directly modifying the matrix, the programmer can force :sip:ref:`~PyQt6.QtGui.QMatrix4x4` to recover the special type if the elements appear to conform to one of the known optimized types.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QMatrix4x4.data`, :sip:ref:`~PyQt6.QtGui.QMatrix4x4.translate`, operator()().
