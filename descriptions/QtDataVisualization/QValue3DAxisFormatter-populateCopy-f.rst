.. sip:method-description::
    :status: todo
    :pysig: aa50c4c5971d53a90c08e74206d90beb
    :realsig: (QValue3DAxisFormatter&) const
    :digest: badb986512ad1421d55557e27e5ba021

Copies all the values necessary for resolving positions, values, and strings with this formatter to the *copy* of the formatter. When reimplementing this method in a subclass, call the superclass version at some point. The renderer uses this method to cache a copy of the formatter.

Returns the new copy. The ownership of the new copy transfers to the caller.
