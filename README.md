# vplot

vplot is a python extension for lldb for visualization of C++ containers as [plotly](https://plot.ly/python/) graphs from the debugger.
![vector graph](/plot.png?raw=true)


## Installation

The following text assumes that you cloned vplot to ~/vplot.

### Install plotly and other dependencies. I use pip.

```sh
$ pip install plotly
$ pip install numpy
$ pip install pandas
```

### Install vplot extension for lldb 

To do that you can enter the following in lldb everytime you start it.

```
(lldb) command script import ~/vplot/src/vplot.py
```

or you can add the line to ~/.lldbinit

## vplot commands from lldb

* Show std::vector variable ```test_vector``` from lldb at a breakpoint.
```
(lldb) fr v --summary vplot test_vector
```

* Set the graph color.
``` 
(lldb) vplot color (red|blue|black|green|rgb(r,g,b))
```

* Clear the graph.
```
(lldb) vplot clear
```

## Example

To generate the image at the beginning, you can use example. To build it:

``` sh
$ cd ~/
$ mkdir build
$ cd build
$ cmake ../vplot/example
$ make
```

Start debugging:

``` sh
$ lldb vplot_example
```

In the debugger:

```
(lldb) br s -f main.cpp -l 14 
(lldb) br s -f main.cpp -l 19
(lldb) run 
(lldb) fr v --summary vplot test_vect 
```
You should see the first graph.

```
(lldb) vplot color red 
(lldb) cont
(lldb) fr v --summary vplot test_vect1
```
The second graph should be in red.

## Notes
Only std::vector is supported at this time


