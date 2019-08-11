# memcacher

memcacher is a minimalistic C++ implementation of [Memcache Binary Protocol](https://cloud.github.com/downloads/memcached/memcached/protocol-binary.txt). Set/Delete (with CAS) and Get commands are currently supported.
This project has a somewhat interesting history. It was submitted as my response to a coding exercise given to me by Slack.
The implementation uses the C++11 move semantic heavily that minimizes the number of required data copying while keeping the code clean. The RAII idiom
helps with a clean code as well as making it exception "safer". The cache uses LRU to reclaim memory when needed.
The performance is comparable with the standard memcached that is implemented in C, and has customized memory allocators.

## Build

### Requirements
C++11 and a system that support kqueue (OSX, FreeBSD) or epoll (Linux). Actually we abstract kqueue as epoll api's (see kqepoll.cpp for details).

### Steps
* Suppose you have the source in [HOME]/work/memcacher
* Create a build folder in [HOME]/work, and go there.

    $mkdir build

	$cd build


* Run cmake.

    $cmake ../memcacher

* Build it.     

    $make

* Your binary will bin in [HOME]/work/build


## Testing


* I used https://github.com/jaysonsantos/python-binary-memcached

* pytest, mock, pytest-cov and flake8 are required
  
  sudo pip install pytest

  sudo pip install pytest-cov

  sudo pip install mock

  sudo pip install flake8

* You can find a simple test script under [HOME]/work/memcacher/test.

  cd [HOME]/work/memcacher/test

  sudo pytest -v test_set_get.py

* If you built in another location, please make sure to point to you binary in conftest.py.

## Project notes

* I used the following open source codes.
   - protocol_binary.h from memcached that contains definitions for the binary protocol data types.
   - murmur3 hash, binary hasher.
* Command line options.

	memcacher [options]
	
		-l IP address of the listening socket, default 127.0.0.1
		-d run as daemon
		-p Port number, default is 11211
		-t Number of threads, default is 1 (just the main thread)
		-c Max number of simultaneous connections, default is 1024
		-m Max cache memory (MB), default is 500

* Example: memcacher -p 5000 -t 2 -m 100

* The following obvious parameters can be configured in config.h

	static const size_t MAX_KEYLEN = 250; //bytes

	static const size_t MAX_VALUELEN = 1024*1024; //1Mb

	static const size_t MAX_WRITE_SIZE = 4*1204; //max size of one write on connections


## Performance notes

* By default all processing happens on the main thread, it could be a good
  idea to set it to the number of cores (option -t). For example if there are
  4 cores, set the option to -t4. In any case, if there is a need to handle a lot 
  of concurrent connections, this is the option to look at. All parallel connections
  are distributed among available thread in round-robin.

## TODO

* Remaining of the protocol
* SASL authentication
* Custom memory allocators
* Support for socket files
* Thread-safe logging
* Test various hasher's
* Stats/profiling


