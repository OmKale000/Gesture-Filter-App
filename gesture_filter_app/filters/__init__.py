# Package initialization
# Import right side filters (existing)
from .grayscale import apply_filter as grayscale_filter
from .cartoon import apply_filter as cartoon_filter
from .negative import apply_filter as negative_filter
from .sepia import apply_filter as sepia_filter
from .blur import apply_filter as blur_filter

# Import left side filters (new)
from .left_blur import apply_filter as left_blur_filter
from .left_edges import apply_filter as left_edges_filter
from .left_emboss import apply_filter as left_emboss_filter
from .left_sharpen import apply_filter as left_sharpen_filter
from .left_smooth import apply_filter as left_smooth_filter
