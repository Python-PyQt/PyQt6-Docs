.. sip:class-description::
    :status: todo
    :brief: This proxy transposes the source model
    :digest: 2cca4676cd77d8942c203f1dc837dd4e

This proxy transposes the source model.

This model will make the rows of the source model become columns of the proxy model and vice-versa.

If the model is a tree, the parents will be transposed as well. For example, if an index in the source model had parent `index(2,0)`, it will have parent `index(0,2)` in the proxy.
