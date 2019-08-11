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
command script import ~/vplot/src/vplot.py
```

or you can add the line to ~/.lldbinit

## vplot commands from lldb

* Show std::vector variable ```test_vector``` from lldb at a breakpoint.
```
fr v --summary vplot test_vector
```

* Set the graph color.
``` 
vplot color (red|blue|black|green|rgb(r,g,b))
```

* Clear the graph.
```
vplot clear
```

## Notes
Only std::vector is supported at this time


