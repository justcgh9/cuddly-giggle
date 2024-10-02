from filters.blur import BlurFilter
from filters.bnw import GrayScaleFilter
from filters.mirror import MirrorFilter
from filters.resize import ResizeFilter

filters_seq = [ResizeFilter, MirrorFilter, BlurFilter, GrayScaleFilter]
