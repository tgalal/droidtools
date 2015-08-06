# Android tools for python

Python implementations or C extensions of some android tools

## Tools:

### mkbootimg

#### mkbootimg

```python
from droidtools import mkbootimg

mkbootimg.build(
            "out.img"
            board,
            base,
            cmdline,
            page_size,
            kernel_offset,
            ramdisk_offset,
            second_offset,
            tags_offset,
            kernel,
            ramdisk,
            second,
            dt
            )
```

#### unpackbootimg

```python
from droidtools import unpackbootimg

bootImg = unpackbootimg.extract("/path/to/file.img", out_dir)
# to repack:
# bootImg.build("out.img")

```

### ext4fs_utils

#### make_ext4fs

```python
from droidtools import ext4fs_utils

ext4fs_utils.make_ext4fs("cache.img",
                         "/path/to/cache_dir",
                         length=33554432,
                         mountPoint="cache",
                         mode=ext4fs_utils.MODE_SPARSED
                         )

```

## Installation

```bash
pip install droidtools
```

## License 

droidtools is licensed under the GPLv3+: http://www.gnu.org/licenses/gpl-3.0.html.
