.. sip:class-description::
    :status: todo
    :brief: Abstract base class for all functors
    :realname: Qt3DCore::QAbstractFunctor
    :digest: dc5ab4f8b6a0277e9351cc8cb1f4ff19

:sip:ref:`~PyQt6.Qt3DCore.QAbstractFunctor` is an abstract base class for all functors.

The :sip:ref:`~PyQt6.Qt3DCore.QAbstractFunctor` is used as a base class for all functors and data generators in :sip:ref:`~PyQt6.Qt3DCore` module.

When user defines a new functor or generator, they need to implement the QAbstractFunctor::id() method, which should be done using the ``QT3D_FUNCTOR`` macro in the class definition.
