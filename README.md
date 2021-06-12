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

2. Generate makefiles

```bash
cmake .
```

[*Hey it fails!*](#troubleshooting)

3. Build the program

```bash
make
```

4. Enjoy

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

This part took me a TON of time.

If you're on Mac and have [homebrew](https://brew.sh) (and you can run it), run

```bash
brew upgrade
brew update
brew install openssl
```

Should fix your problems. I forgot what worked for me but at some point, re-installing OpenSSL was all that I needed.
