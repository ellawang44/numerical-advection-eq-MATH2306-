def ftbs(jn1, j, C_r):
    """Forward Time Backwards Space Scheme"""

    return j - C_r*(j - jn1)

def ftcs(jn1, j, j1, C_r):
    """Forward Time Centered Space Scheme"""

    return j - C_r/2*(j1 - jn1)

def ftfs(j, j1, C_r):
    """Forwards Time Forwards Space Scheme"""

    return j - C_r*(j1 - j)

def lax_wendroff(jn1, j, j1, C_r):
    """Lax Wendroff Scheme"""

    return j - C_r/2*(j1 - jn1) + C_r**2/2*(j1 - 2*j + jn1)

def beam_warming(jn2, jn1, j, C_r):
    """Beam Warming Scheme"""

    return j - C_r/2*(3*j - 4*jn1 + jn2) + C_r**2/2*(j - 2*jn1 + jn2)
