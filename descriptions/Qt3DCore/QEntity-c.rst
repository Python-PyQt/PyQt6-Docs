.. sip:class-description::
    :status: todo
    :brief: Qt3DCore::QEntity is a Qt3DCore::QNode subclass that can aggregate several Qt3DCore::QComponent instances that will specify its behavior
    :realname: Qt3DCore::QEntity
    :digest: ccdceb5cdbabac1f45427c298b03855b

:sip:ref:`~PyQt6.Qt3DCore.QEntity` is a :sip:ref:`~PyQt6.Qt3DCore.QNode` subclass that can aggregate several :sip:ref:`~PyQt6.Qt3DCore.QComponent` instances that will specify its behavior.

By itself a :sip:ref:`~PyQt6.Qt3DCore.QEntity` is an empty shell. The behavior of a :sip:ref:`~PyQt6.Qt3DCore.QEntity` object is defined by the :sip:ref:`~PyQt6.Qt3DCore.QComponent` objects it references. Each Qt3D backend aspect will be able to interpret and process an Entity by recognizing which components it is made up of. One aspect may decide to only process entities composed of a single :sip:ref:`~PyQt6.Qt3DCore.QTransform` component whilst another may focus on :sip:ref:`~PyQt6.Qt3DInput.QMouseHandler`.

.. seealso:: :sip:ref:`~PyQt6.Qt3DCore.QComponent`, :sip:ref:`~PyQt6.Qt3DCore.QTransform`.
