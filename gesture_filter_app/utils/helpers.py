def midpoint(pt1, pt2):
    """Calculate midpoint between two points (x, y) tuples."""
    return ((pt1[0] + pt2[0]) // 2, (pt1[1] + pt2[1]) // 2)


def clamp(value, min_value, max_value):
    """Clamp the value within min and max limits."""
    return max(min_value, min(value, max_value))
