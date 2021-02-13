.. sip:method-description::
    :status: todo
    :pysig: 3cb521b1d03b1d28ef3fb20773d2b952
    :realsig: (float,float,float,float,float,float)
    :digest: 34744ad49ce3718b7bdb563ab5e23b2a

Multiplies this matrix by another that performs the scale and bias transformation used by OpenGL to transform from normalized device coordinates (NDC) to viewport (window) coordinates. That is it maps points from the cube ranging over [-1, 1] in each dimension to the viewport with it's near-lower-left corner at (\ *left*, *bottom*, *nearPlane*) and with size (\ *width*, *height*, *farPlane* - *nearPlane*).

This matches the transform used by the fixed function OpenGL viewport transform controlled by the functions glViewport() and glDepthRange().
