# RRD

[**R**ick **R**oll](https://www.youtube.com/watch?v=dQw4w9WgXcQ "Rickrolling - Wikipedia") **D**etector

---

### Why

I wanted to learn C++. I already know the syntax (mostly) and I wanted to test myself with using C++ and external libraries

#### Why not Python

The entire program can be written in **1 line of Python**:
```python
import re,urllib.request,sys;print("Usage: rrd URL" if len(sys.argv) < 2 else "Possible rickroll detected" (if re.search(r"((rick\s*roll)|(never\s*gonna\s*(give\s*you\s*up)?)|(dQw4w9WgXcQ))", urllib.request.urlopen(sys.argv[1]).read().decode()) else "No rickroll detected"));sys.exit(1 if len(sys.argv) < 2 else 0)
```

or 4 lines, conforming very closely to my C++ program

```python
import re, urllib.request, sys

REGEX = re.compile(r"((rick\s*roll)|(never\s*gonna\s*(give\s*you\s*up)?)|(dQw4w9WgXcQ))")

if len(sys.argv) < 2:
    print("Usage: rrd URL")
    sys.exit(1)
with urllib.request.urlopen(sys.argv[1]) as f:
    print(
        "Possible rickroll detected"
        if REGEX.search(f.read().decode())
        else "No rickroll detected"
    )
```

But come on, that defeats the purpose of this project.

### Installation

1. Download source

```bash
git clone https://github.com/ThatXliner/rrd.git
cd rrd
```

2. Install a current libcurl development package with HTTPS support and updated CA trust.

On Debian or Ubuntu, install `libcurl4-openssl-dev` and `ca-certificates`. On macOS with Homebrew, install or upgrade `curl` and `ca-certificates`. RRD uses the system libcurl by default so its TLS implementation can receive system updates.

3. Generate makefiles

```bash
cmake .
```

[*Hey it fails!*](#troubleshooting)

4. Build the program

```bash
make
```

5. Enjoy

```bash
./rrd 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
```
(or, on Windows)
```powershell
.\rrd 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
```

### Help

#### Troubleshooting

**Running `cmake .` doesn't work!**

Install the libcurl development package for your operating system. If CMake selects Apple's built-in libcurl instead of Homebrew's curl, configure a fresh build with Homebrew's package metadata:

```bash
PKG_CONFIG_PATH="$(brew --prefix curl)/lib/pkgconfig" cmake -S . -B build \
    -DCMAKE_PREFIX_PATH="$(brew --prefix curl)"
cmake --build build
```

Test `build/rrd` when using this build directory.

### Verify HTTPS trust

RRD uses CPR, which delegates HTTPS certificate verification to libcurl and its configured TLS backend and CA trust store. Keep that trust store and libcurl current. A CPR update alone does not update certificate trust. See the [eMudhra incident guidance](https://emudhra.we-have-a-problem.com/) and [Cloudflare developer guidance](https://blog.cloudflare.com/emudhra-certificate-compromise/).

After updating, build RRD again and test the actual executable:

```bash
./rrd https://dv-g3b-emudhra.we-have-a-problem.com/
./rrd https://dv-g3b-aaa-emudhra.we-have-a-problem.com/
./rrd https://example.com
```

Both eMudhra requests must exit with code 1 and report a certificate validation error. DNS failures and timeouts do not prove rejection. The example.com request must succeed. Results apply to the libcurl and trust configuration used by that build. Keep certificate verification enabled.

RRD reports request errors and HTTP error responses on standard error and exits with code 1. It only prints a detection result after a successful HTTP response.

To run the local CLI regression tests, install Python 3 and run `ctest --output-on-failure` from the build directory. Use `-DBUILD_TESTING=OFF` when configuring a build without Python.
