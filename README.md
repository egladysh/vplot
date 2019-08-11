# vplot

vplot is a python extension to lldb for visualization of C++ containers as [plotly](https://plot.ly/python/) graphs from the debugger.
![vector graph](/plot.png?raw=true)


## Installation

The following text assumes that you cloned vplot to ~/vplot. If not, adjust accordingly.

### Install plotly and other dependencies. I use pip.

```sh
$ pip install plotly
$ pip install numpy
$ pip install pandas
```

### Install vplot extension for lldb

To do that you can enter the following in lldb everytime you start it.

```
command script import ~/vplot.py
```

or you can add the line to ~/.lldbinit

## vplot commands

* Set the graph color.
```vplot color (red|blue|black|green|rgb(r,g,b))```

* Clear the graph.
```vplot clear```

## Testing



