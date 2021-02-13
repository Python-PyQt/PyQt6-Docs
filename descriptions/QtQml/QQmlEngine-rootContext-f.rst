.. sip:method-description::
    :status: todo
    :pysig: 8f717fe66026b183c6711f4f27af6bbb
    :realsig: () const
    :digest: 2969ca6e4ba8b40b928db282f98b26b7

Returns the engine's root context.

The root context is automatically created by the :sip:ref:`~PyQt6.QtQml.QQmlEngine`. Data that should be available to all QML component instances instantiated by the engine should be put in the root context.

Additional data that should only be available to a subset of component instances should be added to sub-contexts parented to the root context.
