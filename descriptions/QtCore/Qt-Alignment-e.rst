.. sip:enum-description::
    :status: todo
    :realname: Qt::AlignmentFlag
    :digest: 9e6c43699fb6d29974da871da89d517e

This enum type is used to describe alignment. It contains horizontal and vertical flags that can be combined to produce the required effect.

The :sip:ref:`~PyQt6.QtCore.Qt.TextElideMode.TextElideMode` enum can also be used in many situations to fine-tune the appearance of aligned text.

The horizontal flags are:

The vertical flags are:

You can use only one of the horizontal flags at a time. There is one two-dimensional flag:

You can use at most one horizontal and one vertical flag at a time. Qt::AlignCenter counts as both horizontal and vertical.

Three enum values are useful in applications that can be run in right-to-left mode:

Masks:

Conflicting combinations of flags have undefined meanings.
