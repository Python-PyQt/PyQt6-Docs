.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 239562cc0061b2eb4a2b96dc2bd466cb

Returns ``true`` if the color space is valid. For a color space with ``TransformModel::ThreeComponentMatrix`` that means both primaries and transfer functions set, and implies :sip:ref:`~PyQt6.QtGui.QColorSpace.isValidTarget`. For a color space with ``TransformModel::ElementListProcessing`` it means it has a valid source transform, to check if it also a valid target color space use :sip:ref:`~PyQt6.QtGui.QColorSpace.isValidTarget`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QColorSpace.isValidTarget`.
