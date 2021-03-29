.. sip:method-description::
    :status: todo
    :pysig: 1a927944e65c74e5da10919cbe7ffedd
    :realsig: () const
    :digest: 91a221c1edcadeaf6ff46fa5d58189bb

Returns either :sip:ref:`~PyQt6.QtCore.QCborStreamReader.Type.Array` or :sip:ref:`~PyQt6.QtCore.QCborStreamReader.Type.Map`, indicating whether the container that contains the current item was an array or map, respectively. If we're currently parsing the root element, this function returns :sip:ref:`~PyQt6.QtCore.QCborStreamReader.Type.Invalid`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.containerDepth`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.enterContainer`.
