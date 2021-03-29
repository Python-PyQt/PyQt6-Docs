.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: ac83016236549b14da4a3eb97ec90d1b

Notifies that this transform operation has changed its parameters in such a way that :sip:ref:`~PyQt6.QtWidgets.QGraphicsTransform.applyTo` will return a different result than before.

When implementing you own custom graphics transform, you must call this function every time you change a parameter, to let :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` know that its transformation needs to be updated.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsTransform.applyTo`.
