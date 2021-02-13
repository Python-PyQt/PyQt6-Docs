.. sip:method-description::
    :status: todo
    :pysig: 7cce74340329521a145f04963f5c9bd7
    :realsig: (QStyle*)
    :digest: 84e401dab602f9a05ecd2da3e9294629

Sets the base style that should be proxied.

Ownership of *style* is transferred to :sip:ref:`~PyQt6.QtWidgets.QProxyStyle`.

If style is ``nullptr``, a desktop-dependent style will be assigned automatically.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QProxyStyle.baseStyle`.
