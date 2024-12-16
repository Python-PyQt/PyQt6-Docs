.. sip:method-description::
    :status: todo
    :pysig: 0868429363d3607fc9a9133b8e48d233
    :realsig: (QValue3DAxisFormatter&)
    :digest: badb986512ad1421d55557e27e5ba021

Copies all the values necessary for resolving positions, values, and strings with this formatter to the *copy* of the formatter. When reimplementing this method in a subclass, call the superclass version at some point. The renderer uses this method to cache a copy of the formatter.

Returns the new copy. The ownership of the new copy transfers to the caller.
