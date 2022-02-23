# exit_hijack
auto find the offset for exploiting _rtld_global structure to hijack exit()


### manually find the offset in gdb
```
gdb-peda$ p (struct rtld_global *)_rtld_global
$3 = (struct rtld_global *) 0x7ffff7ffe170
gdb-peda$ p ((struct rtld_global *)_rtld_global)._dl_rtld_lock_recursive
Cannot access memory at address 0x7ffff7fff070
```
offset is 0x7ffff7fff070-0x7ffff7ffe170=3840
```
gdb-peda$ p ((struct rtld_global *)(_rtld_global-500))
$6 = (struct rtld_global *) 0x7ffff7ffdf7c <_rtld_global+3868>
```
tuning the number 500 until it reaches _rtld_global+3840

this number is the offset we need in .c file
