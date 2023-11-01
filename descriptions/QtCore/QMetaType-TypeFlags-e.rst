.. sip:enum-description::
    :status: todo
    :realname: QMetaType::TypeFlag
    :digest: 7b7daa58da1f6d535e4005e32db2510f

The enum describes attributes of a type supported by :sip:ref:`~PyQt6.QtCore.QMetaType`.

**Note:** Before Qt 6.5, both the NeedsConstruction and NeedsDestruction flags were incorrectly set if the either copy construtor or destructor were non-trivial (that is, if the type was not trivial).

Note that the Needs flags may be set but the meta type may not have a publicly-accessible constructor of the relevant type or a publicly-accessible destructor.
